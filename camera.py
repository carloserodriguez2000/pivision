import picamera
import io
import time

import argparse
import pprint
import analysis


def load_config():
    """:returns a json object read from config.json file in the same location as this script"""
    import os
    import json
    script_folder = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_folder, 'config.json')
    with open(config_path) as config_file:
        return json.load(config_file)


def load_image_file(path):
    with open(path, 'rb') as f:
        return f.read()


def take_picture():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, 'jpeg')
    return stream.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Takes a picture, uploads it to MS Computer Vision API and prints categories')
    parser.add_argument('--apikey', help='Key for accessing MS Computer Vision API')
    args = parser.parse_args()
    config = load_config()
    api_key = args.apikey or config[u'ms_vision_api_key']

    print "Reading image from %s" % args.path
    img = take_picture()
    result = analysis.process_image(img, api_key)
    pprint.pprint(result)
    print result[u'categories']
