# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import pickle
from typing import Any, Tuple


def read_from_pickle(fpath: str) -> Any:
    with open(fpath, "rb") as f:
        return pickle.load(f)


def save_to_pickle(obj, fpath: str) -> None:
    with open(fpath, "wb") as f:
        pickle.dump(obj, f)


from config import G_PKL_PATH, M_PKL_PATH, E_PKL_PATH, R_PKL_PATH


def read_GMER(G=False, M=False, E=False, R=False) -> Tuple[Any, Any, Any, Any]:
    G = read_from_pickle(G_PKL_PATH) if G else None
    M = read_from_pickle(M_PKL_PATH) if M else None
    E = read_from_pickle(E_PKL_PATH) if E else None
    R = read_from_pickle(R_PKL_PATH) if R else None
    return G, M, E, R
