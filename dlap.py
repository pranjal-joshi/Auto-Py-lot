#!/usr/bin/env python
# coding: utf-8

# In[1]:


import d3dshot
import tensorflow as tf
import cv2
from PIL import Image, ImageGrab
import numpy as np
import win32gui as w
import win32api, win32con
from ctypes import windll
from time import sleep


# In[2]:


keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.":
	keyList.append(char)

def checkKeys():
	keys = []
	for key in keyList:
		if win32api.GetAsyncKeyState(ord(key)):
			keys.append(key)
	return keys


# In[3]:


# Grab game screenshot
def getScreenshot():
    while True:
        sleep(2)
        win32api.keybd_event(win32con.VK_SNAPSHOT,1)
        i = ImageGrab.grabclipboard()
        i = np.array(i,dtype='uint8')
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        #i.show()
        cv2.imshow("ss",i)
        cv2.waitKey(500)


# In[4]:


if __name__ == "__main__":
    sleep(2)
    user32 = windll.user32
    user32.SetProcessDPIAware()
    getScreenshot()


# In[ ]:


get_ipython().system('^x')