# Make Your Pass (Sanitaire) Fun Again
Customize your Pass Sanitaire (French name for EU digital Covide19 Certificate) with colors and images, thus make it **Fun** again.

## Usage

    usage: passfun.py [-h] [--pos POS] [--trans [TRANS]] [--test [TEST]] inputfile backgroundfile outputfile

    Make your EU digital COVID certificate fun again.

    positional arguments:
      inputfile        The original qrcode
      backgroundfile   Background image, can start with 'http'
      outputfile       The new qrcode

    optional arguments:
      -h, --help       show this help message and exit
      --pos POS        Generated qrcode horizontal position, 0=left, 100=right
      --trans [TRANS]  Background transparency, 0=white, 100=original image
      --test [TEST]    Download random test data from dgc-testdata instead of inputfile

## Example

Here's some examples generated by demo.py:

![1.png](1.png)

![2.png](2.png)

![3.png](3.png)

![4.png](4.png)

![5.png](5.png)

![6.png](6.png)

![7.png](7.png)

![8.png](8.png)

![9.png](9.png)

![10.png](10.png)
