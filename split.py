#coding=utf-8
import cv2
import os
pages=0
for filename in os.listdir("./"):
    if filename.endswith(".xml")==True:
        pages=pages+1
        
if not os.path.exists("./out"):
    os.makedirs("./out")        
index=0
currentPage=-1
for filename in os.listdir("./"):
    if filename.endswith(".jpg")==True:
        #if currentPage>=pages-1:
        #    exit()
        if index>=0:
            img=cv2.imread(filename)
            height=img.shape[0]
            width=img.shape[1]
            mid=int(width/2)
            left = img[0:height,0:mid]
            right = img[0:height,mid:width]
            currentPage=currentPage+1
            cv2.imwrite("./out/"+str(currentPage)+".jpg",right) #1
            currentPage=currentPage+1
            cv2.imwrite("./out/"+str(currentPage)+".jpg",left) #2
        index=index+1