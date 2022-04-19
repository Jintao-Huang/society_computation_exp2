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
    if G is True:
        ans.append(read_from_pickle(G_PKL_PATH))
    if M is True:
        ans.append(read_from_pickle(M_PKL_PATH))
    if E is True:
        ans.append(read_from_pickle(E_PKL_PATH))
    if R is True:
        ans.append(read_from_pickle(R_PKL_PATH))
    if T is True:
        ans.append(read_from_pickle(T_PKL_PATH))
    if V is True:
        ans.append(read_from_pickle(V_PKL_PATH))
    if C is True:
        ans.append(read_from_pickle(C_PKL_PATH))
    if len(ans) == 1:
        return ans[0]
    return ans


def save_PKL(G=None, M=None, E=None, R=None, T=None, V=None, C=None) -> None:
    if G is not None:
        save_to_pickle(G, G_PKL_PATH)
    if M is not None:
        save_to_pickle(M, M_PKL_PATH)
    if E is not None:
        save_to_pickle(E, E_PKL_PATH)
    if R is not None:
        save_to_pickle(R, R_PKL_PATH)
    if T is not None:
        save_to_pickle(T, T_PKL_PATH)
    if V is not None:
        save_to_pickle(V, V_PKL_PATH)
    if C is not None:
        save_to_pickle(C, C_PKL_PATH)