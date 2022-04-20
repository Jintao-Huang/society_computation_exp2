# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import pickle
from typing import Any, List, Union


def read_from_pickle(fpath: str) -> Any:
    with open(fpath, "rb") as f:
        return pickle.load(f)


def save_to_pickle(obj, fpath: str) -> None:
    with open(fpath, "wb") as f:
        pickle.dump(obj, f)


from config import G_PKL_PATH, M_PKL_PATH, E_PKL_PATH, R_PKL_PATH, T_PKL_PATH, V_PKL_PATH, C_PKL_PATH


def read_PKL(G=False, M=False, E=False, R=False, T=False, V=False, C=False) -> Union[List, Any]:
    ans = []
    for D, pkl_path in zip([G, M, E, R, T, V, C],
                           [G_PKL_PATH, M_PKL_PATH, E_PKL_PATH, R_PKL_PATH, T_PKL_PATH, V_PKL_PATH, C_PKL_PATH]):
        if D is True:
            ans.append(read_from_pickle(pkl_path))
    if len(ans) == 1:
        return ans[0]
    return ans


import os
import logging


def save_PKL(G=None, M=None, E=None, R=None, T=None, V=None, C=None, exist_ok=False) -> None:
    if not exist_ok:
        exist_ok = input("exist_ok? y/n")
        if exist_ok.lower() in {"y", "yes"}:
            exist_ok = True
        else:
            exist_ok = False
    #
    for D, pkl_path in zip([G, M, E, R, T, V, C],
                           [G_PKL_PATH, M_PKL_PATH, E_PKL_PATH, R_PKL_PATH, T_PKL_PATH, V_PKL_PATH, C_PKL_PATH]):
        if D is not None:
            if not exist_ok:
                logging.warning(f"File exist, not covered")
            else:
                save_to_pickle(D, pkl_path)
                print(f"File exist, covered")
    print()
