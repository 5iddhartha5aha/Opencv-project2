#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img = cv2.imread('lde.png')


# In[3]:


hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# In[4]:


lower_purple = np.array([129, 50, 70])
upper_purple = np.array([158, 255, 255])


# In[5]:


lower_red = np.array([0, 50, 70])
upper_red = np.array([9, 255, 255])


# In[6]:


mask_purple = cv2.inRange(hsv_img, lower_purple, upper_purple)


# In[7]:


mask_red = cv2.inRange(hsv_img, lower_red, upper_red)


# In[8]:


contours1, hierarchy1 = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img2 = np.copy(img)

# green contours for purple fruits
c = 0
for i in range(len(contours1)):
    if cv2.contourArea(contours1[i]) > 10:
        cv2.drawContours(img2, contours1[i], -1, (0, 255, 0), 2)
        cv2.putText(img2, 'PURPLE', contours1[i][0][0], 1, 1, (255, 0, 255), 2)
        c += 1


# In[9]:


contours2, hierarchy2 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# yellow contours for red fruits
d = 0
for i in range(len(contours2)):
    if cv2.contourArea(contours2[i]) > 10 and cv2.contourArea(contours2[i]) < 10000:
        cv2.drawContours(img2, contours2[i], -1, (0, 255, 255), 2)
        cv2.putText(img2, 'RED', contours2[i][0][0], 1, 1, (0, 0, 255), 2)
        d += 1


# In[10]:


cv2.imshow('original',img)
cv2.imshow('fruits_detected',img2)
cv2.waitKey(0)  
cv2.destroyAllWindows()


# In[11]:


#print(len(contours1))
print("Number of Purple fruits detected : ",c)


# In[12]:


#print(len(contours2))
print("Number of Red fruits detected : ",d)

