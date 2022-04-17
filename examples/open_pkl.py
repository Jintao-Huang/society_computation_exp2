# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from config import PKL_PATH
from utils import read_from_pickle

if __name__ == '__main__':
    obj = read_from_pickle(PKL_PATH)
    for k in obj.keys():
        print(k, len(obj[k]))
    # Group 783
    # Memeber 82770
    # PastEvent 93512
    # RSVPs 65128
