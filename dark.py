import cv2
import numpy as np
import pyautogui
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import sys
from pynput.mouse import Button,Controller
mouse = Controller()
import time
import random


def manipulation(image):
    image = cv2.imread(image) #Load image
    for i in range(4):
        image[:70:] = (0,0,0)
        image =cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


    center_coordinates = (683,384)
    radius = (150)
    color = (0,0,0)
    thickness = -1
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
    cv2.imwrite("filename.png", image)


    #Pixels higher than this will be 1. Otherwise 0.
    THRESHOLD_VALUE = 250


    img = Image.open('filename.png')
    thresh = 235
    fn = lambda x : 0 if x > thresh else 255
    r = img.convert('L').point(fn, mode='1')
    r.save('example.png')


def box_coordinates(image):
    image = cv2.imread(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    thresh = cv2.threshold(sharpen,160,255, cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 100
    max_area = 1500
    image_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)
            return (x+w/2,y+h/2)











def introDemo(x,y):
    counter = 0

    while 1:


        counter +=1



        if counter == 15 :
            xvalue = random.randint(100,200)
            yvalue = random.randint(30,150)
            mouse.position = (1366-xvalue,768-yvalue)
            time.sleep(1)
            mouse.click(Button.left,2)
            counter = 0



        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('example.png')

        manipulation('example.png')
        while box_coordinates('example.png') != None:
            x,y = box_coordinates('example.png')
            mouse.position = (x,y)
            time.sleep(0.1)
            mouse.click(Button.left,2)
            time.sleep(1)

            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('example.png')
            manipulation('example.png')
            if box_coordinates('example.png') != None:
                x,y = box_coordinates('example.png')
                mouse.position = (x,y)
                time.sleep(0.1)
                mouse.click(Button.left,2)
                time.sleep(1.5)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('example.png')
                manipulation('example.png')
                if box_coordinates('example.png') == None :
                    mouse.position = (1366-xvalue,768-yvalue)
                    time.sleep(0.5)
                    mouse.click(Button.left,2)
                    time.sleep(2)











introDemo(1366,768)
