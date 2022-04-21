# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


# 将E按created时间进行排序, 取最后的20%做测试集.


# 制作数据集:
import random
from typing import List, Tuple


def split_dataset(E, k: float) -> Tuple[List, List]:
    n_test = int(len(E) * k)
    keys = list(E.keys())
    keys = sorted(keys, key=lambda key: (E[key]["created_year"], E[key]["created_month"], E[key]["created_day"]))
    train_keys, test_keys = keys[:-n_test], keys[-n_test:]
    return train_keys, test_keys  # E


from utils import read_PKL


def sample_dataset(train_e: List, test_e: List, E, R):
    # return X_train, y_train, X_test, y_test
    random.seed(42)
    cnt = 0
    X_train, y_train, X_test, y_test = [], [], [], []
    for X, y, e_list in zip([X_train, X_test], [y_train, y_test], [train_e, test_e]):
        for k in e_list:
            e = E[k]
            m_list = []
            for r_id in e["rsvp_id_list"]:
                r = R[r_id]
                response = r["response"]  # 0: no, 1: yes
                if response > 1:
                    cnt += 1
                    continue
                m_list.append(r["member"])
                y.append(response)
            X += [[k, m] for m in m_list]  # [E, M] pair
    print(cnt)
    return X_train, y_train, X_test, y_test


import numpy as np

if __name__ == '__main__':
    from utils import save_PKL

    G, M, E, R = read_PKL(G=True, M=True, E=True, R=True)
    train_e, test_e = split_dataset(E, 0.2)
    X_train, y_train, X_test, y_test = sample_dataset(train_e, test_e, E,R)
    print(len(X_train), len(X_test))
    print(np.mean(y_train))
    print(np.mean(y_test))
    save_PKL(Dataset=(X_train, y_train, X_test, y_test))
"""
6668
567468 191181
0.5656371813036154
0.6059074908071409
exist_ok? y/ny
File exist, covered

"""