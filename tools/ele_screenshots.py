from PIL import Image
'''appium区域截图'''


def ele_screenshots(ele, pic_name):
    left = ele.location['x']
    top = ele.location['y']
    right = ele.location['x'] + ele.size['width']
    bottom = ele.location['y'] + ele.size['height']
    im = Image.open(pic_name)
    im = im.crop((left, top, right, bottom))
    im.save(pic_name)
