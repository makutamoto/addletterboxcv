#!/usr/bin/env python3
import sys
import argparse
import cv2
import numpy as np
from tqdm import tqdm


def add_letterbox(video, width, height, codec, interpolation, outpath):
    original_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    original_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    original_aspect = original_width / original_height
    fps = int(video.get(cv2.CAP_PROP_FPS))
    if codec is None:
        fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
        if fourcc == cv2.VideoWriter_fourcc(*'avc1'):
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    else:
        fourcc = cv2.VideoWriter_fourcc(*codec)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    output = cv2.VideoWriter(outpath, fourcc, fps, (width, height))
    video_width = width
    video_height = width / original_aspect
    if video_height > height:
        video_width = height * original_aspect
        video_height = height
    video_width = round(video_width)
    video_height = round(video_height)
    video_size = (video_width, video_height)
    x = round((width - video_width) / 2)
    y = round((height - video_height) / 2)
    with tqdm(total=frame_count) as pbar:
        while True:
            status, frame = video.read()
            if not status:
                break
            background = np.zeros((height, width, 3), np.uint8)
            frame = cv2.resize(frame, video_size, interpolation=interpolation)
            background[y:y + video_height, x:x + video_width] = frame
            output.write(background)
            pbar.update(1)
        output.release()


def check_fourcc(string):
    if len(string) != 4:
        msg = "TypeError: codec must conform to the fourcc syntax"
        raise argparse.ArgumentTypeError(msg)
    return string.lower()


def main():
    INTERPOLATIONS = {
        'NEAREST': cv2.INTER_NEAREST,
        'LINEAR': cv2.INTER_LINEAR,
        'AREA': cv2.INTER_AREA,
        'CUBIC': cv2.INTER_CUBIC,
        'LANCZOS4': cv2.INTER_LANCZOS4
    }
    parser = argparse.ArgumentParser(description="Add a letterbox to the video and scale it to the specified size. Note: this program does not support audio.")
    parser.add_argument('video', help="video file", nargs=1)
    parser.add_argument('output', help="output file", nargs=1)
    parser.add_argument('--dimension', '-d', help="video dimension", type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), required=True)
    parser.add_argument('--interpolation', '-i', help="interpolation type", default='LINEAR', choices=['NEAREST', 'LINEAR', 'AREA', 'CUBIC', 'LANCZOS4'])
    parser.add_argument('--codec', '-c', help="video codec", nargs=1, type=check_fourcc)
    args = parser.parse_args(sys.argv[1:])
    file = cv2.VideoCapture(args.video[0])
    if file.isOpened():
        add_letterbox(file, args.dimension[0], args.dimension[1], None if args.codec is None else args.codec[0], INTERPOLATIONS[args.interpolation], args.output[0])
        file.release()
        print("\u2713 Completed!")
    else:
        print("error: no such file or directory: '%s'" % args.video[0], file=sys.stderr)


if __name__ == '__main__':
    main()
