""" The aim of this module is to do face detection. This is required in order to

crop some of the input databases, because they are not centered"""

import cv2
import numpy as np

# Create window for image display
CASCADE_FN = "haarcascade_frontalface_default.xml"

# The scale used for face recognition.
# It is important as the face recognition algorithm works better on small images
# Also helps with removing faces that are too far away
RESIZE_SCALE = 3
RECTANGE_COLOUR = (255, 0, 0)
THICKNESS = 2


# TODO: add the rescaling
def cropFace(image):
  print "image.shape"
  print image.shape
  cascade = cv2.CascadeClassifier(CASCADE_FN)
  # img_copy = cv2.resize(image, (image.shape[1],
  #                               image.shape[0]))
  # gray = cv2.cvtColor(img_copy, cv2.cv.CV_GRAY2BGR)
  # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(image)
  rects = cascade.detectMultiScale(gray, 1.3, 5)
  print "rects"
  print rects
  # You need to find exactly one face in the picture
  assert len(rects) == 1

  x, w, y, h = rects[0]
  face = image[y:y + h, x:x + w]
  return face
