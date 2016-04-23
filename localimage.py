import argparse
import pprint
import analysis





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uploads given file to MS Computer Vision API and prints categories')
    parser.add_argument('path', help='Path to the image file')
    parser.add_argument('--apikey', help='Key for accessing MS Computer Vision API')
    args = parser.parse_args()
    config = load_config()
    api_key = args.apikey or config[u'ms_vision_api_key']

    print "Reading image from %s" % args.path
    img = load_image_file(args.path)
    result = analysis.process_image(img, api_key)
    pprint.pprint(result)
    print result[u'categories']
