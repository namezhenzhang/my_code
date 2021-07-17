import os
import h5py
import numpy as np
import cv2
import re
import random
gender_dict={}
with open("male_names.txt","r",encoding="utf-8") as f:
    for userline in f:
        userline=str(userline).replace('\n','')
        gender_dict[userline] = 1
with open("female_names.txt","r",encoding="utf-8") as f:
    for userline in f:
        userline=str(userline).replace('\n','')
        gender_dict[userline] = 0

def saveinone(path,fi):
    if cv2.imread(path) is None:
        print(path,"is not a picture.")
        return
    if fi in gender_dict.keys():
      p = random.random()
      dir = ''
      if 0<=p<0.5:
        dir = 'train'
      elif 0.5<=p<0.9:
        dir ='test'
      else:
        dir ='valid'
      cv2.imwrite(r"C:\Users\Zz\Desktop\cv\dataset\{}\{}\{}".format(dir,gender_dict[fi],fi), cv2.imread(path))

def gci(filepath):
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    #isdir和isfile参数必须跟绝对路径
    if os.path.isdir(fi_d):
      gci(fi_d)
    else:
      saveinone(os.path.relpath(os.path.join(filepath,fi)),fi)
gci('lfw_funneled')