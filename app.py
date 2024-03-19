import os
import picture_converter as pc
import video_converter as vc

IMAGE_PATH = 'data/image'
VIDEO_PATH = 'data/video'

image_li = [f for f in os.listdir(IMAGE_PATH) if os.path.isfile(os.path.join(IMAGE_PATH, f))]
video_li = [f for f in os.listdir(VIDEO_PATH) if os.path.isfile(os.path.join(VIDEO_PATH, f))]

print('============   CARTOON COVERTER   ============')
print('=  Put your images in the data/image folder  =')
print('=  Put your videos in the data/video folder  =')
print('==============================================')

order = 1
print('>-- DETECTED IMAGES --<')
for image in image_li:
    print(f'{order}. {image}')
    order += 1
print('>-- DETECTED VIDEOS --<')
for video in video_li:
    print(f'{order}. {video}')
    order += 1
print('WHAT FILE DO YOU WANT TO CONVERT? : ', end='')

fileNum = int(input())
if fileNum <= len(image_li):
    pc.convert(f'{IMAGE_PATH}/{image_li[fileNum-1]}', f'{IMAGE_PATH}/converted_{image_li[fileNum-1]}')
else:
    vc.convert(f'{VIDEO_PATH}/{video_li[fileNum-len(image_li)-1]}', f'{VIDEO_PATH}/converted_{video_li[fileNum-len(image_li)-1]}')