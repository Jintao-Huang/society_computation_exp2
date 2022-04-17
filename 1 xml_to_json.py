# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from utils import xml_to_dict
import os
from collections import defaultdict
import json
from config import DATASET_DIR, JSON_PATH
from typing import Dict

if __name__ == '__main__':
    files = os.listdir(DATASET_DIR)
    ans = defaultdict(list)
    for i, fname in enumerate(files):
        ftype = fname.split(" ")[0]
        fpath = os.path.join(DATASET_DIR, fname)
        d = xml_to_dict(fpath)  # type: Dict
        ans[ftype].append(d)
        if i % 1000 == 0:
            print("\r>> %d/%d" % (i + 1, len(files)), end="")
    print("\r>> %d/%d" % (len(files), len(files)))
    #
    with open(JSON_PATH, "w") as f:
        json.dump(ans, f)
