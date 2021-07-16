import os
import os.path as osp
import random


dire = "../data/ucf101/annotations"
files = [osp.join(dire, f) for f in os.listdir(dire)]
test = [f for f in files if 'testlist' in f]
train = [f for f in files if 'trainlist' in f]
test_list = []
train_list = []

# 生成合并的注释文件
for f in test:
    test_list += open(f, 'r', encoding='utf-8').readlines()
for f in train:
    train_list += open(f, 'r', encoding='utf-8').readlines()
with open(osp.join(dire, "test.txt"), 'w', encoding='utf-8') as f:
    f.write(''.join(test_list))
with open(osp.join(dire, "train.txt"), 'w', encoding='utf-8') as f:
    f.write(''.join(train_list))

# 删除原来的单个文件
for f in test:
    os.remove(f)
for f in train:
    os.remove(f)

# 从训练集里sample 10%作为验证集
