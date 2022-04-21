# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from utils import convert_datetime, read_PKL, attr_to_int, default_using_median, remove_attr, save_PKL, unzip_venue

if __name__ == '__main__':
    E, V = read_PKL(E=True, V=True)

    # add venue in E
    unzip_venue(E, V)
    attr_names = ["state", "lon", "lat", "repinned", "country"]
    attr_names = ["venue_" + attr_name for attr_name in attr_names]
    default_using_median(E, attr_names)
    save_PKL(E=E)

    # 考虑到使用的是最后20%的信息, 时间信息可能产生干扰. 打算转成月份信息.
    # G: created
    # E: updated, created, time
    # M: joined, visited
    G, M, E = read_PKL(G=True, M=True, E=True)

    convert_datetime(E, ["updated", "created", "time"])
    convert_datetime(G, ["created"])
    convert_datetime(M, ["joined", "visited"])
    save_PKL(G=G, E=E, M=M)
