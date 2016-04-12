import os
import cv2


class Camera:
    def __init__(self):
        self.vc = cv2.VideoCapture(0)
        self.frame = None
        self.status = None

    def grab_frame(self):
        "Grab a frame from the webcam and store it"
        self.status, self.frame = self.vc.read()
        return self.frame

    def save_frame(self, filename="static/img/default.jpg"):
        "Save the most recently grabbed frame in the static folder"
        fullpath = os.path.join("static", "img", filename)
        if self.frame is not None:
            cv2.imwrite(fullpath, self.frame)

    def refresh_capture(self):
        "Reset the webcam in case the device is no longer working"
        self.vc.release()
        self.vc = cv2.VideoCapture(0)

    def __del__(self):
        "Release the capture device once we're done with it"
        self.vc.release()
