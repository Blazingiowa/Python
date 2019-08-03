import matplotlib.pyplot as plt
import cv2

cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

img = cv2.imread("waithi.jpg")
img_gray = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))
if len(face_list)==0:
    print("失敗")
    quit()

for (x,y,w,h) in face_list:
    print("顔の座標=",x,y,w,h)
    red=(0,0,255)
    cv2.rectangle(img,(x,y),(x+w,y+h),red,thickness=20)

cv2.imwrite("face-detect.png",img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
