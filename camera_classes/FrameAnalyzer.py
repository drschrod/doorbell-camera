import numpy as np
from cv2 import createBackgroundSubtractorMOG2, imshow
import time

class FrameAnalyzer(object):
    '''
    Purpose:
    - Processes frames as they're read for:
        - Motion
        - Unique Faces (TODO)
    '''
    def __init__(self, sensitivity=500):
        self.currentMogFrame = None
        self.sensitivity = sensitivity
        self.mog2 = createBackgroundSubtractorMOG2(history=self.sensitivity)
    
    def generateMog2Frame(self, frame):
        self.currentMogFrame = self.mog2.apply(frame)
        return self.currentMogFrame
    
    def showCurrentMogFrame(self):
        imshow('MOG2 Frame', self.currentMogFrame)
        