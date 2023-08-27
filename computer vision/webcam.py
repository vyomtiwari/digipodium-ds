import cv2  # library version is 4

# create a VideoCapture object
# the cam index show the total number of camera and their indexes we have one camera in out system so idx 0 means sc
CAM_IDX = 0
cam = cv2.VideoCapture(CAM_IDX)

while cam.isOpened():
    status, img = cam.read()  # read the frame/image
    if status:
        cv2.imshow(f'Webcam {CAM_IDX}', img)  # display the frame/ image
        key = cv2.waitKey(
            10)  # wait for a key press it means we will wait for 0ms after the person clicks a button from keyboard
        if key == 27:  # this means if the key pressed is esc key which has value of 27 then break the loop
            break
    else:
        print('Webcam is not available')
        break
# free up resources
cv2.destroyAllWindows()  # closes all windows
cam.release()  # Releases the camera
