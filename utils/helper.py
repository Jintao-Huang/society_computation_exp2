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


from config import G_PKL_PATH, M_PKL_PATH, E_PKL_PATH, R_PKL_PATH


def read_GMER(G=False, M=False, E=False, R=False) -> Union[List, Any]:
    ans = []
    if G is True:
        ans.append(read_from_pickle(G_PKL_PATH))
    if M is True:
        ans.append(read_from_pickle(M_PKL_PATH))
    if E is True:
        ans.append(read_from_pickle(E_PKL_PATH))
    if R is True:
        ans.append(read_from_pickle(R_PKL_PATH))
    if len(ans) == 1:
        return ans[0]
    return ans


def save_GMER(G=None, M=None, E=None, R=None) -> None:
    if G is not None:
        save_to_pickle(G, G_PKL_PATH)
    if M is not None:
        save_to_pickle(M, M_PKL_PATH)
    if E is not None:
        save_to_pickle(E, E_PKL_PATH)
    if R is not None:
        save_to_pickle(R, R_PKL_PATH)
