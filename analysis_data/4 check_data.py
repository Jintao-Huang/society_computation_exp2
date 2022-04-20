# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from utils import read_PKL, save_PKL, check_data, attr_to_float

if __name__ == '__main__':
    G, M, E, R, V = read_PKL(G=True, M=True, E=True, R=True, V=True)
    for D in [G, M, E, R, V]:
        check_data(D)

"""Out[0]
set()
set()
{'venue', 'event_hosts'}
{'venue'}
set()
"""
