import cv2

file_name = u"kanashiy.mp4"
video = cv2.VideoCapture(file_name)
frame_count = int(video.get(7))
frame_rate = int(video.get(5))
cv2.namedWindow('player',  cv2.WINDOW_AUTOSIZE)
for i in range(frame_count):
    is_read, frame = video.read()
    k = cv2.waitKey(frame_rate)
    if k == 27 or not is_read:
        break
    cv2.imshow("player", frame)
