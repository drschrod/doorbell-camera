import queue

class CameraSentry(object):
    '''
    Used for
    - Maintaining a temp write buffer to append to the recording so we capturemoments before an event
    - Saving video files
    '''
    def __init__(self, maxBufferSize=300, frameRate=30):
        self.buffer = queue.Queue(maxsize=maxBufferSize)
        self.frameRate = frameRate

    def updateBuffer(self, frame):
        if self.buffer.full():
            self.buffer.get()
        self.buffer.put(frame)
    
    def startRecording(self):
        pass

    def endRecording(self):
        pass
