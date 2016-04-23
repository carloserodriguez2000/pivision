import requests

_url = 'https://api.projectoxford.ai/vision/v1/analyses'


def process_image(image_bin, api_key):
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/octet-stream'
    }

    response = requests.request('post', _url, data=image_bin, headers=headers)
    if response.status_code != 200 and response.status_code != 201:
        raise Exception('Message: %s' % (response.json()['message']), response.status_code)

    return response.json() if response.content else None
