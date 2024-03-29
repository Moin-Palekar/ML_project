#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[4]:


config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'


# In[5]:


model = cv2.dnn_DetectionModel(frozen_model, config_file)


# In[6]:


classLabels = []
file_name = 'labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')


# In[7]:


print(classLabels)


# In[9]:


model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127,5,127.5))
model.setInputSwapRB(True)


# In[19]:


img = cv2.imread('img.PNG')
plt.imshow(img)


# In[20]:


ClassIndex, confidece, bbox = model.detect(img, confThreshold = 0.5)


# In[21]:


print(ClassIndex)


# In[22]:


font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
    cv2.rectangle(img, boxes, (255,0,0), 2)
    cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40), font, fontScale = font_scale, color = (0,255,0), thickness = 3)


# In[23]:


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


# In[ ]:




