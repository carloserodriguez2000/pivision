import picamera
import io
import time


def take_picture():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, 'jpeg')
    return stream.read()

