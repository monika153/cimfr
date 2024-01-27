# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:01:42 2019

@author: Lenovo
"""

import cv2
import numpy as np
import math
#import imutils
class Enhance:
    global apply_mask,apply_threshold
    def Enhance(img):
        contrast = 1.3
        clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))
        #img =cv2.resize(img,(640,480))
        img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        H,S,V = cv2.split(img_hsv)
        #print(min(V))
        #vf=V.flatten()
       # print(min(vf))
        #print(max(vf))
        V_C = clahe.apply(V)
        def loop(R):
            height_R=R.shape[0]
            width_R=R.shape[1]
            for i in np.arange(height_R):
                for j in np.arange(width_R):
                    a = R.item(i,j)
                    b = math.ceil(a * contrast)
                    if b > 255:
                        b = 255
                    R.itemset((i,j), b)
            return R
        HSV = cv2.merge((H,S,V_C))
        output= cv2.cvtColor(HSV , cv2.COLOR_HSV2BGR)
        #B,G,R = cv2.split(output)
        #B=loop(B)
        #G=loop(G)
        #R=loop(R)
        #OUTPUT1 = cv2.merge((B,G,R))
        return output
    def Edge_light(self,frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _,thresh1 = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
          
        mask_edge=cv2.bitwise_not(thresh1)
        image=cv2.bitwise_and(frame,frame,mask=mask_edge)
        return image
    def apply_mask(matrix, mask, fill_value):
        masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
        return masked.filled()
        #print(masked)
       
    def apply_threshold(matrix, low_value, high_value):
        low_mask = matrix < low_value
        matrix = apply_mask(matrix, low_mask, low_value)
    
        high_mask = matrix > high_value
        matrix = apply_mask(matrix, high_mask, high_value)
        #print('...........aaaa')
        #print(matrix)
        return matrix
    
    def simplest_cb(img, percent):
        assert img.shape[2] == 3
        assert percent > 0 and percent < 100
    
        half_percent = percent / 200.0
        #img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        channels = cv2.split(img)
    
        out_channels = []
        for channel in channels:
            assert len(channel.shape) == 2
            # find the low and high precentile values (based on the input percentile)
            height, width = channel.shape
            vec_size = width * height
            flat = channel.reshape(vec_size)
    
            assert len(flat.shape) == 1
    
            flat = np.sort(flat)
    
            n_cols = flat.shape[0]
    
            low_val  = flat[math.floor(n_cols * half_percent)]
            high_val = flat[math.ceil( n_cols * (1.0 - half_percent))]
    
            #print "Lowval: ", low_val
            #print "Highval: ", high_val
    
            # saturate below the low percentile and above the high percentile
            thresholded = apply_threshold(channel, low_val, high_val)
            # scale the channel
            normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
            out_channels.append(normalized)
    
        return cv2.merge(out_channels)


            
            
                