# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from preprocessing import xml_to_dict
import os
from collections import defaultdict
import json
from config import DATASET_DIR, JSON_PATH

if __name__ == '__main__':
    files = os.listdir(DATASET_DIR)
    ans = defaultdict(list)
    for i, fname in enumerate(files):
        ftype = fname.split(" ")[0]
        path = os.path.join(DATASET_DIR, fname)
        ans[ftype].append(xml_to_dict(path))
        if i % 1000 == 0:
            print("\r>> %d/%d" % (i + 1, len(files)), end="")
    print("\r>> %d/%d" % (len(files), len(files)))
    with open(JSON_PATH, "w") as f:
        json.dump(ans, f)
    print()
