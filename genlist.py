import json
import os
import cv2

'''
def count_frames(path):
    frame_count=len(os.listdir(path))
    assert frame_count > 0, \
        "VideoIter:: Video: `{}' has no frames".format(path)
    return frame_count

def get_file_list(video_prefix,txt_list,cached_info_path):

    assert os.path.exists(video_prefix), "VideoIter:: failed to locate: `{}'".format(video_prefix)
    assert os.path.exists(txt_list), "VideoIter:: failed to locate: `{}'".format(txt_list)

    video_list=[]
    # building dataset
    with open(txt_list) as f:
        lines = f.read().splitlines()
        print("VideoIter:: found {} videos in `{}'".format(len(lines), txt_list))
        for i, line in enumerate(lines):
            v_id, label, video_subpath = line.split()
            video_subpath=video_subpath[:-4]
            video_path = os.path.join(video_prefix, video_subpath)
            if not os.path.exists(video_path):
                print("VideoIter:: >> cannot locate `{}'".format(video_path))
                continue

            frame_count = count_frames(video_path)
            info = [video_subpath, frame_count,int(label)]
            video_list.append(info)

        with open(cached_info_path, 'w') as f:
            for i, video in enumerate(video_list):
                if i > 0:
                    f.write("\n")
                f.write("{:s}\t\t{:d}\t{:d}".format(video[0], video[1],video[2]))
'''
# root_path = './data/ucf101'


def read_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        list = f.readlines()
    return list


def count_frames(path):
    cap = cv2.VideoCapture(path)
    frame_counts = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    num = 0
    for i in range(frame_counts):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        res, frame = cap.read()
        if res:
            num += 1
        else:
            break
    cap.release()
    return num


def gen_list(trainlist, cached_info_path):
    video_list = []

    for line in trainlist:
        id, label = line.strip().split(" ")
        frame_counts = int(count_frames(id))
        frame_counts = frame_counts - 1
        video_list.append([id, frame_counts, int(label)])

    with open(cached_info_path, 'w') as f:
        for i, video in enumerate(video_list):
            if i > 0:
                f.write("\n")
            f.write("{:s}\t{:d}\t{:d}".format(video[0], video[1], video[2]))


if __name__ == '__main__':  # ??????????????????????????????????????????
    train_list = read_list("data/ucf101/annotations/train.txt")
    test_list = read_list("data/ucf101/annotations/val.txt")
    gen_list(trainlist, "data/ucf101/annotations/train_list.txt")
    gen_list(testlist, "data/ucf101/annotations/val_list.txt")
