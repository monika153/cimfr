# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:21:08 2020

@author: Lenovo
"""
import cv2
import numpy as np
import math
from Enhance import Enhance

Stream = cv2.VideoCapture(r'input\Fog.mp4')

ret = True
while (ret):
   r,image_np = Stream.read()
   image_np = cv2.resize(image_np, (640,360))
   image_np1=Enhance.Enhance(image_np)
   #image_np=func.Edge_light(image_np)
   image_np1=Enhance.simplest_cb(image_np1,10)
   #cv2.imshow('image',cv2.resize(image_np1,(1280,960)))
   cv2.imshow('image',image_np1)
   cv2.imshow('image1',image_np)
   if cv2.waitKey(25) & 0xFF == ord('q'):
      
      break
Stream.release()
cv2.destroyAllWindows()
