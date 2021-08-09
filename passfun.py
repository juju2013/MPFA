#! /usr/bin/env python3

# Copyright (c) 2021, juju2013@github
# All rights reserved
# This file is under BSD 2-Clause License, see LICENSE file


import os,sys, random, io
import argparse
from pyzbar import pyzbar
from PIL import Image, ImageDraw
from datetime import datetime
from urllib import request
import qrcode

# Some constants
ccardy=2 # in inch
ccardx=3 # in inch
DPI=600 # print DPI
MAXY = int(ccardy * DPI)
MAXX = int(ccardx * DPI)

class EUDCC:
  def __init__(self, inf=None):
    self.data=None
    self.img = None
    self.mask1 = None
    self.mask2 = None
    self.mask3 = None
    if inf:
      self.ReadImage(inf)
    
  def Decode(self, im):
    d = pyzbar.decode(im)
    if len(d) != 1:
      raise Exception("%s must contain 1 and only 1 qrcode!"%inf)
    self.data=d[0].data
    
  def ReadImage(self, inf):
    with Image.open(inf) as im:
      self.Decode(im)

  # load a random test data
  def TestData(self, uri="https://github.com/eu-digital-green-certificates/dgc-testdata/raw/main/CH/png/", tf=15):
    random.seed(str(datetime.now()))
    n = random.randint(1, tf)
    ib = request.urlopen("%s%s.png"%(uri, n)).read()
    im = Image.open(io.BytesIO(ib))
    self.Decode(im)
    
  def NewQRCode(self):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=1)
    qr.add_data(self.data)
    qr.make(fit=True)
    im = qr.make_image(back_color="transparent")
    # FIXME :  bug from PIL ??? erroneous width without convert
    self.img = maxImage(im.convert("RGBA"))

  def Debug(self):
    self.img.save("dbug-qrcode.png")
    self.mask1.save("dbug-mask1.png")
    self.mask2.save("dbug-mask2.png")
    self.mask3.save("dbug-mask3.png")
    
  # compute masks with size (x,y) and qrcode at pos% from left
  # mask1 is only with qrcode
  # mask2 is mask1 + border
  # mask3 is fade mask
  def SetMasks(self, x, y, pos=0, trans=0):
    fg=(0,0,0)
    fa=int(trans*255/100)
    im = Image.new("RGBA",(x,y))
    xs = int((x-self.img.width)/100*pos)
    im.paste(self.img,(xs,0))
    self.mask1=im.copy()

    dr = ImageDraw.Draw(im)
    dr.rectangle([0,0,xs,y], fill=fg)
    dr.rectangle([self.img.width+xs,0,x,y], fill=fg)
    self.mask2=im.copy()

    self.mask3=self.mask1.copy().convert("L")
    dr = ImageDraw.Draw(self.mask3)
    dr.rectangle([xs,0,xs+self.img.width,y], fill=fa)
    
class DstImage:
  def __init__(self, inf=None):
    self.img = None
    if inf:
      if inf.lower().startswith("http"):
        self.ReadImageUrl(inf)
      else:
        self.ReadImage(inf)
  
  def ReadImage(self, inf):
    with Image.open(inf) as im:
      self.img = maxImage(im)

  def ReadImageUrl(self, url):
    r = request.Request(
      url,
      data    = None,
      headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0'
      }
    )
    ib = request.urlopen(r).read()
    im = Image.open(io.BytesIO(ib))
    self.img = maxImage(im)

def maxImage(img):
  rx = MAXX/img.width
  ry = MAXY/img.height
  r = min(rx,ry)
  return img.resize((int(ry*img.width), int(ry*img.height))) # only resize on Y


      
def main():
  apar = argparse.ArgumentParser(description="Make your EU digital COVID certificate fun again.")
  apar.add_argument("inputfile", help="The original qrcode")
  apar.add_argument("backgroundfile", help="Background image, can start with 'http'")
  apar.add_argument("outputfile", help="The new qrcode")
  apar.add_argument("--pos", type=int, help="Generated qrcode horizontal position, 0=left, 100=right")
  apar.add_argument("--trans", type=int, const=50, default=50, nargs='?', help="Background transparency, 0=white, 100=original image")
  apar.add_argument("--test", default=False, nargs='?', const=True, help="Download random test data from dgc-testdata instead of inputfile")

  args = apar.parse_args()

  cert = EUDCC()
  if args.test:
    cert.TestData()
  else:
    cert.ReadImage(args.inputfile)
  cert.NewQRCode()
  
  bimg = DstImage(args.backgroundfile)
  if bimg.img.width < cert.img.width:
    raise Exception("Background image is smaller then QRcode")
  # place qrcode
  cert.SetMasks(bimg.img.width, bimg.img.height, args.pos, args.trans)
  #cert.Debug()

  im = bimg.img.copy()
  # use mask3 to faded background
  bimg.img.paste((255,255,255), mask=cert.mask3)
  # use past mask1 over
  bimg.img.paste(im, mask=cert.mask1)
  
  # fill transparent with black
  if bimg.img.mode=="RGBA":
    bg = Image.new("RGBA", im.size, (0,0,0))
    bimg.img=Image.alpha_composite(bg, bimg.img)
  # save the finale work
  bimg.img.save(args.outputfile)
  
if __name__ == "__main__":
  main()
