import cv2
import glob
ext=("*.jpg","*.jpeg","*.bmp","*.png")
files=[]
for i in ext:
    files.extend(glob.glob(i))
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for photo in files:
    img = cv2.imread(photo)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(87,230,111),3)
    print(img.shape[0],img.shape[1])
    resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow("Face Detection",resized_img)
    cv2.waitKey(50)
