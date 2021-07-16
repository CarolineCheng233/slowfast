import argparse
parser = argparse.ArgumentParser(description="slowfast pytorch")
parser.add_argument('dataset', type=str, choices=['ucf101'])  # 选择一个数据集，目前仅支持ucf101数据集
parser.add_argument('train_list', type=str)  # 训练数据文件名
parser.add_argument('val_list', type=str)    # 测试数据文件名
parser.add_argument('root_path', type=str)
parser.add_argument('--record_path', type=str, default='record/')

# ========================= Learning Configs ==========================
parser.add_argument('--T', default=4, type=int, metavar='N',
                    help='frames the slow way to take')
parser.add_argument('--tau', default=16, type=int, metavar='N',
                    help='stride of the slow way')
parser.add_argument('--epochs', default=50, type=int, metavar='N',  # 训练的总轮数
                    help='number of total epochs to run')
parser.add_argument('-b', '--batch-size', default=256, type=int,  # 训练时一批的数据大小
                    metavar='N', help='mini-batch size (default: 256)')
parser.add_argument('--lr', '--learning-rate', default=0.001, type=float,  # 学习率
                    metavar='LR', help='initial learning rate')
parser.add_argument('--lr_steps', default=[20,40,60], type=float, nargs="+",
                    metavar='LRSteps', help='epochs to decay learning rate by 10')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument('--clip-gradient', '--gd', default=None, type=float,
                    metavar='W', help='gradient norm clipping (default: disabled)')
parser.add_argument('--no_partialbn', '--npb', default=False, action="store_true")

parser.add_argument('--no_dense_sample', '--nds', default=False, action="store_true")
# ========================= Runtime Configs ==========================
parser.add_argument('-j', '--workers', default=4, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',  # 是否从checkpoint中恢复
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',  # 是否是测试
                    help='evaluate model on validation set')









