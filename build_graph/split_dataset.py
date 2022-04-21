# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


# 将E按created时间进行排序, 取最后的20%做测试集.


# 制作数据集:

# E, M. 50%正样本
import random
from typing import List, Tuple


def split_dataset(E, k: float) -> Tuple[List, List]:
    n_test = int(len(E) * k)
    keys = list(E.keys())
    keys = sorted(keys, key=lambda k: E[k]["created"])
    train_keys, test_keys = keys[:-n_test], keys[-n_test:]
    return train_keys, test_keys  # E


from utils import read_PKL


def sample_dataset(train_e: List, test_e: List, E):
    # return X_train, y_train, X_test, y_test
    X_train, y_train, X_test, y_test = [], [], [], []
    for X, y, e_list in zip([X_train, X_test], [y_train, y_test], [train_e, test_e]):
        for k in e_list:
            e = E[k]
            g_id = e["group"]
            m_list = G[g_id]["member_list"]
            m_list_in_e = set(e["member_list"])
            choices = random.sample(m_list, min(5, len(m_list)))
            for c in choices:
                if c in m_list_in_e:
                    y.append(1)
                else:
                    y.append(0)
            X += [[k, c] for c in choices]  # [E, M] pair
    return X_train, y_train, X_test, y_test

import numpy as np
if __name__ == '__main__':
    from utils import save_PKL

    random.seed(42)
    G, M, E = read_PKL(G=True, M=True, E=True)
    train_e, test_e = split_dataset(E, 0.2)
    X_train, y_train, X_test, y_test = sample_dataset(train_e, test_e, E)
    print(np.mean(y_train))
    print(np.mean(y_test))
    # 0.1761532413694518
    # 0.1721494692740699
    save_PKL(Dataset=(X_train, y_train, X_test, y_test))

# itt: test G, E中member的比例
# if __name__ == '__main__':
#     G, E = read_PKL(G=True, E=True)
#     mean_G = []
#     mean_E = []
#     for k, g in G.items():
#         mean_G.append(len(g['member_list']))
#
#     for k, e in E.items():
#         mean_E.append(len(e['member_list']))
#
#
#     print(np.mean(mean_G))
#     print(np.mean(mean_E))
#     # 977.4163473818646
#     # 8.184158182907007
