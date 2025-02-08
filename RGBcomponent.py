import numpy as np
import matplotlib.pyplot as plt
img1=input("Enter your RGB Image File Name=")
img2=input("Enter your Output Image File Name=")
data1=plt.imread(img1) 
shape1=data1.shape
r,c,d=shape1[0],shape1[1],shape1[2]
print('r=',r,' c=',c,' d=',d)
R,G,B=data1[:,:,0],data1[:,:,1],data1[:,:,2]
rows=1
columns=4
fig=plt.figure(figsize=(20,20))
fig.add_subplot(rows,columns,1)
plt.title('RGB Image')
plt.imshow(data1)
fig.add_subplot(rows,columns,2)
plt.title('Red Component of image')
plt.imshow(R, cmap='Reds') 
fig.add_subplot(rows,columns,3)
plt.title('Green Component of image')
plt.imshow(G, cmap='Greens') 
fig.add_subplot(rows,columns,4)
plt.title('Blue Component of image')
plt.imshow(B, cmap='Blues') 
plt.savefig(img2) 
plt.show() 
