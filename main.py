from camera_classes.DoorbellCamera import DoorbellCamera
from camera_classes.FrameAnalyzer import FrameAnalyzer
from camera_classes.CameraSentry import CameraSentry
# TODO: Implement:
# - Class for image processing and motion detection
# - Class to handle internet comms and data transfer
# - Facial Recogition to capture faces
# - Class that handles logging messages for debugging purposes
# - 

doorBellCamera = DoorbellCamera('Feed1')
frameAnalyzer = FrameAnalyzer(sensitivity=200)

while(True):
    frame = doorBellCamera.getNextFrame()
    frameAnalyzer.generateMog2Frame(frame)

    frameAnalyzer.showCurrentMogFrame()
    doorBellCamera.showCurrentFrame()
