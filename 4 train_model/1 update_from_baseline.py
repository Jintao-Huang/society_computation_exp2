# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from utils import attr_to_bool, attr_to_float, attr_to_len, \
    read_PKL, attr_to_int, default_using_median, remove_attr, save_PKL, unzip_venue, move_E_to_G, \
    handle_organizer_event_hosts

# 一些杂工作
if __name__ == '__main__':
    G, M, E, V = read_PKL(G=True, M=True, E=True, V=True)
    # organizer_event_hosts
    handle_organizer_event_hosts(M, G, E)
    attr_to_bool(G, ["organizer"])
    attr_to_len(E, ["event_hosts"])
    # venue in E
    unzip_venue(E, V)
    attr_names = ["state", "lon", "lat", "repinned", "country"]
    attr_names = ["venue_" + attr_name for attr_name in attr_names]
    default_using_median(E, attr_names)
    # G
    attr_to_len(G, ["rsvp_id_list", "member_list", "event_list"])
    # E
    attr_names = ["headcount", "rating_average", "rating_count", "tallies_maybe",
                  "tallies_waitlist", "tallies_no", "tallies_yes"]
    move_E_to_G(E, G, attr_names)  # mean E to G. 有些特征E用不了
    # M
    attr_to_len(M, ["group_list", "event_list"])
    save_PKL(G=G, M=M, E=E)
