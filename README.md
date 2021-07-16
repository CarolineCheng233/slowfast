# 计算机视觉理论与应用作业

## 环境
 + python 3.6
 + torch 1.7.1
 + torchvision 0.8.2
 + opencv

注：低于1.7.1的torch和低于0.8.2的torchvision可能也可，最好是torch版本1.4+，torchvision版本与torch对应，需要与CUDA版本对应，同时CUDA应该能支持对应GPU。

CUDA的安装见 https://github.com/CarolineCheng233/foolish_daily/blob/main/cuda.md

torch和torchvision的安装见 https://pytorch.org/get-started/previous-versions/


## 训练模型

### 准备数据集
##### 支持的数据集

目前仅支持ucf101数据集

##### 下载数据

进入到download文件夹下

运行ucf101_annotations.sh下载ucf101数据集注释文件

运行ucf101_videos.sh下载ucf101数据集视频文件

运行genlist.py文件生成相应数据集的训练文件train.txt和测试文件test.txt

文件格式如下：（分别是视频路径，帧数，标签）

```
related_path_of_video1  frames  label
related_path_of_video2  frames  label
related_path_of_video3  frames  label
...
```


### 运行

训练模型

e.g.

```bash
CUDA_VISIBLE_DEVICES=0 python main.py /train_list_of_your_data /test_list_of_your_data /data_path --gd 20 --lr 0.01 --epoch 60 -b12 -j4
```
仅支持DataParallel运行方式，更多参数见config.py文件，有注释说明


测试模型

e.g.

```bash
CUDA_VISIBLE_DEVICES=0 python main.py /train_list_of_your_data /test_list_of_your_data /data_path --evaluate --resume your_pretrained_mode_path -b12 -j4
```

加上--evaluate参数运行在测试模式，更多参数见config.py文件
