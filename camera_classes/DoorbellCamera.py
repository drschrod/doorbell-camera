import numpy as np
import cv2
import time

class DoorbellCamera(object):
    '''
    Only purpose is to fetch frames consecutively.
    '''
    def __init__(self, cameraName, cameraNumber=0):
        self.cameraNumber = cameraNumber
        self.cameraName = cameraName
        self.cameraFeed = cv2.VideoCapture(cameraNumber)
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
        cv2.imshow(self.cameraName, self.currentFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.endCameraFeed()

    def endCameraFeed(self):
        self.debugLogger('Feed ending', 'endCameraFeed()')
        self.cameraFeed.release()
        cv2.destroyAllWindows()
        exit()