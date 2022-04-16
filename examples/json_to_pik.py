# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from config import JSON_PATH, PKL_PATH
import json
from typing import Dict
import os
import pickle

TO_PKL = False
#
if __name__ == '__main__':
    with open(JSON_PATH, "r") as f:
        obj = json.load(f)  # type: Dict
    for k in obj.keys():
        print(k, len(obj[k]))

    #
    if TO_PKL:
        with open(PKL_PATH, "wb") as f:
            pickle.dump(obj, f)
