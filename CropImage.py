# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:15:44 2022

@author: cakir
"""
import numpy as np
import cv2

class cropImage:
    def __init__(self,img):
        self.img = img
        
    def corpSize(self):
        x, y = self.img.shape[:2]
        
        value = np.array([
            [(x * 0.2, x),#SOL ALT NOKTA
            ((int((y * 3.2) / 20)), int(x * 0.75)), #SOL ÜST NOKTA
            (int((y * 5 ) / 5.8), int(x * 0.75)), #SAĞ ÜST NOKTA
            (y * 0.9, x)]], np.int32) #SAĞ ALT NOKTA
        
            #BURDA YAPILAN ŞEY GEREKSİZ KISIMLARIN ÇIKARTILMASI SADECE BELİRLENEN
            #4 NOKTA ARASINDA KALAN YERE BAKILMASI
            
        return value

    def crop_image(self, matris):
        x, y = self.img.shape[:2]
        
        mask = np.zeros(shape = (x, y), dtype = np.uint8)
        
        mask = cv2.fillPoly(mask, matris, 255)
        
        mask = cv2.bitwise_and(self.img, self.img, mask = mask)
        
        return mask
        #BU FONKSİYON BELİRLENEN 4 NOKTANIN DIŞINDA KALAN BÖLGEYİ SİYAH
        #YAPMAMIZA YARIYOR