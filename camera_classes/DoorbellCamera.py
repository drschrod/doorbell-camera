import numpy as np

from cv2 import VideoCapture, destroyAllWindows, imshow
import time

class DoorbellCamera(object):
    '''
    Purpose: Connects to camera hardware and begins fetching frames from the camera
    TODOs:
    - Add a connection retry function
    '''
    def __init__(self, cameraName, cameraNumber=0):
        self.cameraNumber = cameraNumber
        self.cameraName = cameraName
        self.cameraFeed = VideoCapture(cameraNumber)
        self.previousFrame = None
        self.currentFrame = None

    def debugLogger(self, message, source='', timestamp = time.time()):
        logMessage = {
            'camera_info': {
                'camera_number': self.cameraNumber,
                'camera_name': self.cameraName,
                'camera_model': None
            },
            'message': message,
            'source': source,
            'timestamp': timestamp
        }
        print(logMessage)

    def getNextFrame(self):
        ret, nextFrame = self.cameraFeed.read()
        if ret:
            self.previousFrame = self.currentFrame
            self.currentFrame = nextFrame
            return self.currentFrame
        else:
            self.debugLogger('Error Reading Next Frame', 'getNextFrame()')
    
    def showCurrentFrame(self):
        imshow(self.cameraName, self.currentFrame)

    def endCameraFeed(self):
        self.debugLogger('Feed ending', 'endCameraFeed()')
        self.cameraFeed.release()
        destroyAllWindows()
        exit()