import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--epoch', dest='nb_epoch', type=int, default=5000, help='# of epochs')
parser.add_argument('--learning_rate', dest='lr', type=float, default=0.0001, help='# learning rate')
parser.add_argument('--sample_size', dest='sample_size', type=int, default=60, help='# sample size')
parser.add_argument('--gen_hidden', dest='gen_hidden', type=int, default=80, help='# hidden nodes in generator')
parser.add_argument('--disc_hidden', dest='disc_hidden', type=int, default=80, help='# hidden nodes in discriminator')
parser.add_argument('--your_login', dest='your_login', type=str, default='rubens', help='# your login name')

args = vars(parser.parse_args())
