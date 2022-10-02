import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)  # uses default webcam

while True:
    successful_frame_read, frame = webcam.read()

    greyscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(greyscaled_image)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

    cv2.imshow('Jetson Cyrus', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

print("code completed")

