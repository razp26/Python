import numpy as np
import cv2
import sys


def start(classifier):
    try:
        face_classifier = cv2.CascadeClassifier(classifier)

        # Detecting camera
        i = 0
        found = False
        for i in range(4):
                capture = cv2.VideoCapture(i)
                if not capture:
                    print ("Unable to capture camera " + i + ".")
                else:
                    found = True
                    break

        if found == False:
            print ("No camera was found.")
            sys.exit()

        # Setting video properties
        #v_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        #v_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while True:
            # Capturing frame by frame
            res, video = capture.read(0)

            # Check if there is a face in current frame
            video = face_detector(video, face_classifier)
            cv2.imshow('Detecting face in video', video)
            
            # Exit condition
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        capture.release()
        cv2.destroyAllWindwos()

    except:
        raise Exception('There was an error whie running the face detector.')


def face_detector(image, classifier):
    bck_image = image.copy()
    rectangles = classifier.detectMultiScale(bck_image)
    for (x,y,w,h) in rectangles:
        cv2.rectangle(bck_image, (x,y), (x+w, y+y), (0,255,0), 10)
    return bck_image