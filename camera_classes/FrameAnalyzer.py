import numpy as np
import cv2
import time

class FrameAnalyzer(object):
    def __init__(self, sensitivity=500):
        self.currentMogFrame = None
        self.sensitivity = sensitivity
        self.mog2 = cv2.createBackgroundSubtractorMOG2(history=self.sensitivity)
    
    def generateMog2Frame(self, frame):
        self.currentMogFrame = self.mog2.apply(frame)
        return self.currentMogFrame
    
    def showCurrentMogFrame(self):
        cv2.imshow('MOG2 Frame', self.currentMogFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.endCameraFeed()