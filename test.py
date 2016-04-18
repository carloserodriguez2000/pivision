import requests
import argparse

_url = 'https://api.projectoxford.ai/vision/v1/analyses'


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


def process_image(image_bin, api_key):
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/octet-stream'
    }

    response = requests.request('post', _url, data=image_bin, headers=headers)
    if response.status_code != 200 and response.status_code != 201:
        raise Exception('Message: %s' % (response.json()['message']), response.status_code)

    return response.json() if response.content else None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uploads given file to MS Computer Vision API and prints categories')
    parser.add_argument('path', help='Path to the image file')
    parser.add_argument('--apikey', help='Key for accessing MS Computer Vision API')
    args = parser.parse_args()

    config = load_config()
    api_key = args.apikey or config[u'ms_vision_api_key']

    print "Reading image from %s" % args.path
    img = load_image_file(args.path)
    process_image(img, api_key)
