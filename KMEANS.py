
import cv2
import random
import math
import sys
import os



imgpath = sys.argv[1]
img = cv2.imread(imgpath)
k=int(sys.argv[2])
km = []
updater = []
new = []

x=len(img[0])
y=len(img)

for i in range(k):
    t = [random.randint(0,255) for x in range(3)]
    km.append(t)
    t1= [0 for itr in range(3)] 
    updater.append(t1)

for i in range(y):
    t = [0 for j in range(x)]
    new.append(t)
  
count = [0 for i in range(k)]        

dist = 0    
min_pos = 0

#------------Compression-----------------
for i in range(y):
    for j in range(x):
        min_dist = -1
        for k_ptr in range(k):
            r = km[k_ptr][0] - img[i][j][0]
            g = km[k_ptr][1] - img[i][j][1]
            b = km[k_ptr][2] - img[i][j][2]
            dist = math.sqrt(math.pow(r,2)+math.pow(g,2)+math.pow(b,2))
            if (min_dist == -1 or dist < min_dist): 
                min_dist = dist
                min_pos = k_ptr

        new[i][j] = min_pos
        updater[min_pos][0] += img[i][j][0] 
        updater[min_pos][1] += img[i][j][1] 
        updater[min_pos][2] += img[i][j][2]
        count[min_pos] = count[min_pos] + 1

#-------Updating means--------------
for i in range(k):
        for col in range(3):
            if count[i] != 0:
                km[i][col] = updater[i][col]/count[i]
        
#-------Creating new image---------
for i in range(y):
    for j in range(x):
        for c in range(3):
            img[i][j][c] = km[new[i][j]][c]
                            
            

cv2.imwrite("k="+str(k)+".jpg", img)
    
print("Completed")


    


