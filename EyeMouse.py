from PIL.Image import CUBIC
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import math
import pyautogui

def eye_aspect_ratio(eye):
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    kk1 = eye[1]
    kk2 = eye[5]
    x1 = kk1[1]
    yl = kk2[0]
    hl = kk1[1] - kk2[1]
    wl = kk2[0] - kk1[0]
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])
    ## print eye[0],eye[3]
    vert1 = eye[0]
    vert2 = eye[3]
    x = vert1[1]
    y = vert1[0]
    h = vert1[1] - vert2[1]
    w = vert2[0] - vert1[0]
    if w == 0:
        w = -1
    if h == 0:
        h = 1
    ## print w
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])
    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    # return the eye aspect ratio
    cnter = (eye[0] + eye[3]) / 2
    return ear, h, w, x, y, cnter

ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
#                 help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
args = vars(ap.parse_args())

# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold for to set off the
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 1
# initialize the frame counter as well as a boolean used to
COUNTER = 0

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(args["shape_predictor"])
predictor = dlib.shape_predictor("Model/shape_predictor_68_face_landmarks.dat")

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
# start the video stream thread
print("[INFO] starting video stream thread...")
##vs = cv2. VideoCapture(‘http://192.168.43.1:8080/video')
vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

time.sleep(1.0)
# data = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
# loop over frames from the video stream
cursdata = [[1, 192], [193, 384], [385, 576]]
muldiffcentX = 0
muldiffcentY = 0
CentInitX = 1920 / 2
CentInitY = 1080 / 2
FrameCentX = 960 / 2
FrameCentY = 540 / 2
Ip = 0
cursorfactor = 8
pyautogui.FAILSAFE = False
pyautogui.moveTo(CentInitX, CentInitY)
while True:
    # grab the frame from the threaded video file stream, resize
    # it, and convert it to grayscale
    # channels)
    ret, frame = vs.read()
    frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    rects = detector(gray, 0)
    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # extract the left and right eye coordinates, then use the
        # coordinates to compute the eye aspect ratio for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        ear, h, w, x, y, cnter = eye_aspect_ratio(leftEye)
        if Ip > 0:
            c11 = x
            c22 = y
            x = int(math.ceil(cnter[0]))
            y = int(math.ceil(cnter[1]))
            cv2.circle(frame, (x, y), 5, 255, -1)
        if Ip > 0:
            diffcentX = FrameCentX - x
            diffcentY = FrameCentY - y
            print(diffcentX, diffcentY)
            print('###########')
            print('###########')
            muldiffcentX = diffcentX * cursorfactor
            muldiffcentY = diffcentY * cursorfactor
            pyautogui.moveTo(CentInitX + muldiffcentX, CentInitY - muldiffcentY)
            print(CentInitX + muldiffcentX, CentInitY - muldiffcentY)

        Ip = 1
        print("\nRight Eye\n")
        rightEAR, hrr, wr, xr, yr, cnterr = eye_aspect_ratio(rightEye)
        print("\nLeft Eye\n")
        leftEAR, hrl, wl, xl, yl, cnterl = eye_aspect_ratio(leftEye)
        # average the eye aspect ratio together for both eyes
        # compute the convex hull for the left and right eye, then
        # visualize each of the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        if ear < EYE_AR_THRESH:
            pyautogui.doubleClick(button='left')
            COUNTER += 1
        # if the eyes were closed for a sufficient number of time
        if COUNTER >= EYE_AR_CONSEC_FRAMES:
            cv2.putText(frame, "BUTTON PRESSED!", (10, 30),
                        cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 2)
        # otherwise, the eye aspect ratio is not below the blink
        # threshold, so reset the counter
        else:
            COUNTER = 0
        if rightEAR < EYE_AR_THRESH:
            COUNTER += 1
            pyautogui.doubleClick(button='right')
        # if the eyes were closed for a sufficient number of time
        if COUNTER >= EYE_AR_CONSEC_FRAMES:
            cv2.putText(frame, "RIGHT CLICK PRESSED!", (10, 30),
                        cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 2)
        # otherwise, the eye aspect ratio is not below the blink
        # threshold, so reset the counter
        else:
            COUNTER = 0
        if leftEAR < EYE_AR_THRESH:
            COUNTER += 1
            pyautogui.click(button='left')

        # if the eyes were closed for a sufficient number of

        if COUNTER >= EYE_AR_CONSEC_FRAMES:
            cv2.putText(frame, "left CLICK PRESSED!", (10, 30),
                        cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 2)

        # otherwise, the eye aspect ratio is not below the blink
        # threshold, so reset the counter
        else:
            COUNTER = 0
            # draw the computed eye aspect ratio on the frame to help
            # with debugging and setting the correct eye aspect ratio# thresholds and frame counters
            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 2)

        # show the frame
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # if the “q® key was pressed, break from the loop
    if key == ord("q"):
        break

# do abit of cleanup
cv2.destroyAllWindows()
vs.stop()
