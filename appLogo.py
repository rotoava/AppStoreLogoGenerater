#__author__ = 'dingfeng'
# -*- coding: utf-8 -*-
from __future__ import print_function
import os,shutil
from PIL import  Image
import json


originImagePath = "logo1024.png"
imageOrigin = Image.open(originImagePath)
print(imageOrigin.format, imageOrigin.size, imageOrigin.mode)


#创建生成LOGO的目录
path="logos"

#如果已经存在先清空删除
isExists=os.path.exists(path)
if isExists:
    shutil.rmtree(path)

#创建目录
os.mkdir(path)

#读取配置json文件   ---直接从Xcode 类似 <AppIcon-1.appiconset> 的文件夹中复制过来
contentsJsonFile = file("Contents.json")
jsonObject = json.load(contentsJsonFile)
print (jsonObject.keys())
logoForm_list = jsonObject["images"]

i = 0;
for element in logoForm_list:
    i= i+1
    print(element,i)

    logoFilePath = "%s/%d_%s_%s_%s.png" %(path,i,element["idiom"],element["size"],element["scale"])
    widthAndHeightString = "%s" % (element["size"])
    widthAndHeight=widthAndHeightString.split("x")
    scaleString = "%s" % (element["scale"])
    scale=scaleString.split("x")
    print(scale[0])


    width = int(widthAndHeight[0])*int(scale[0])
    Height = int(widthAndHeight[1])*int(scale[0])

    logoFile  =imageOrigin.resize((width,Height),Image.ANTIALIAS)
    logoFile.save(logoFilePath)
    print("logFilePath suceess! :",imageOrigin.format, imageOrigin.size, imageOrigin.mode)












