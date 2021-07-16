import os
import os.path as osp


dire = "../data/ucf101/annotations"
files = [osp.join(dire, f) for f in os.listdir(dire)]
test = [f for f in files if 'test' in f]
train = [f for f in files if 'train' in f]
test_list = []
train_list = []
for f in test:
    test_list += f.readlines()
for f in train:
    train_list += f.readlines()
with open(osp.join(dire, "test.txt"), 'w', encoding='utf-8') as f:
    f.write(''.join(test_list))
with open(osp.join(dire, "train.txt"), 'w', encoding='utf-8') as f:
    f.write(''.join(train_list))
