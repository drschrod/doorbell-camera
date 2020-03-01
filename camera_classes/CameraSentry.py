import queue
from cv2 import VideoWriter_fourcc, VideoWriter

class CameraSentry(object):
    '''
    Used for
    - Maintaining a temp write buffer to append to the recording so we capture moments before an event
    - Saving video files
    '''
    def __init__(self, maxBufferSize=300, frameRate=30, height=480, width=640):
        self.buffer = queue.Queue(maxsize=maxBufferSize)
        self.frameRate = frameRate
        self.videoDimensions = (width, height)
        self.fourcc = VideoWriter_fourcc(*'MJPG')
        self.recorder = None
        self.isRecording = False

    def updateBuffer(self, frame):
        if self.buffer.full() and self.isRecording:
            self.writeFrame(self.buffer.get(), self.recorder)
        elif self.buffer.full() and not self.isRecording:
            self.buffer.get()
        self.buffer.put(frame)
    
    def startRecording(self):
        self.recorder = VideoWriter('output.avi', self.fourcc, self.frameRate, self.videoDimensions)
        self.writeFrame(self.buffer.get(), self.recorder)

    @staticmethod
    def writeFrame(frame, recorder):
        recorder.write(frame)

    def endRecording(self):
        self.recorder.release()
        self.recorder = None
