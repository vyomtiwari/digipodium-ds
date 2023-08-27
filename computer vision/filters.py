import cv2

CAM_IDX = 0
cam = cv2.VideoCapture(CAM_IDX)

while cam.isOpened():
    state , img = cam.read()
    if not state:
        print('Camera is not available')
        break
    #filter
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # adv filter
    im_canny = cv2.Canny(img, 0, 1)
    im_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize = 3)
    cv2.imshow('original', img )
    cv2.imshow('gray', im_gray)
    cv2.imshow('rgb', im_rgb)
    cv2.imshow('canny', im_canny)
    cv2.imshow('sobel', im_sobel)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cam.release()