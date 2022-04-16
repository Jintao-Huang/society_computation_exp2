# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from config import PKL_PATH
import pickle

if __name__ == '__main__':
    with open(PKL_PATH, "rb") as f:
        obj = pickle.load(f)
        for k in obj.keys():
            print(k, len(obj[k]))
