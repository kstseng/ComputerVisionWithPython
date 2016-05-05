# -*- coding: utf-8 -*-
"""
Created on Thu May 05 10:25:52 2016

@author: David79.Tseng
"""

from PIL import Image
pil_im = Image.open('C:\Users\David79.Tseng\Dropbox\python_cv\grachten-hotels-amsterdam.jpg').convert('L')

pil_im.thumbnail((256, 256))

box = (100, 100, 400, 400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)

pil_im.paste(region,box)

#--- resize
pil_im.size
out = pil_im.resize((128, 60))