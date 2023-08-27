import cv2

VIDEO_PATH = ""
vid = cv2.VideoCapture(VIDEO_PATH)

while True:
    status, img = vid.read()
    if not status:
        print('Video is not available')
        break
    # vision operations
    img = cv2.resize(img, None, fx=.5, fy=0.5)
    cv2.imshow('Video', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
vid.release()
