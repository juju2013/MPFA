#! /usr/bin/env python3

# Copyright (c) 2021, juju2013@github
# All rights reserved
# This file is under BSD 2-Clause License, see LICENSE file

import subprocess as sp

test_data=[
    "https://improveyourdrawings.com/wp-content/uploads/2019/01/Step-9-Lights-914x914.jpg"
  , "http://www.clipartbest.com/cliparts/4T9/LE8/4T9LE8Kbc.jpg"
  , "http://1.bp.blogspot.com/-uL69HJIUEqI/Up9l2y6hRyI/AAAAAAAAAxQ/6qPnmjwDrcs/s1600/Bad+Piggies.png"
  , "https://3.bp.blogspot.com/-Au7LolzzUZ0/WmCr991vrxI/AAAAAAAAAfQ/UNyp15ozACYl684MXAERba6aG5BrqImjACEwYBhgL/w1200-h630-p-k-no-nu/minion-2687629_1920.png"
  , "https://i.ytimg.com/vi/KYvxtr4t7jM/hqdefault.jpg"
  , "https://cdn.dribbble.com/users/228963/screenshots/2333285/darth_vader.jpg"
  , "https://l-express.ca/wp-content/uploads/2020/10/tintin2.jpg"
  , "https://ih0.redbubble.net/image.29820104.8237/pp,550x550.u2.jpg"
  , "https://i.pinimg.com/originals/43/0c/f7/430cf76e9f105ad8dae71385e2de82f4.png"
  , "http://wallpapercave.com/wp/lTbIIzI.jpg"
]

i=0
for u in test_data:
  i+=1
  sp.run(["./passfun.py", "null.png", u, "%s.png"%i, "--pos", "50", "--trans", "80", "--test"])

