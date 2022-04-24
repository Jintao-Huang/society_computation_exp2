# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 数据分析

# 1. 每一年, 活动数量; 活动参与人数数量; 拒绝人数数量
# 2. 每一年, 链接数的变化.
# 3. 随机森林的树个数, auc, f1的变化
# 4.

import matplotlib.pyplot as plt
from utils import read_PKL
from collections import defaultdict
# 1 Number of Member
E = read_PKL(E=True)
ans = defaultdict(int)
for e in E.values():
    ans[(e['time_y'], e["time_m"])] += 1
ks = sorted(ans.keys())
ks_int = [y + m / 12 for y, m in ks]
vs = [ans[k] for k in ks]

#
ks_int = ks_int[:-1]
vs = vs[:-1]
print(ks_int, vs)


#
plt.figure(figsize=(8, 4))
plt.xlabel("Year", labelpad=8, fontsize=14)
plt.ylabel("Number of Events (Per Month)", labelpad=8, fontsize=14)
#
plt.xlim([2004, 2014])
plt.xticks(list(range(2004, 2015, 1)))
plt.ylim([0, 2500])
p1, = plt.plot(ks_int, vs)
plt.savefig("out.png", dpi=200, bbox_inches='tight')
plt.show()
print()


# 2 Number of RSVPs
E, R = read_PKL(E=True, R=True)
ans_yes = defaultdict(int)
ans_no = defaultdict(int)
for e in E.values():
    rsvp_ids = e["rsvp_id_list"]
    t = (e['time_y'], e["time_m"])
    for id_ in rsvp_ids:
        r = R[id_]
        if r["response"] == 1:
            ans_yes[t] += 1
        else:
            ans_no[t] += 1
ks_y = sorted(ans_yes.keys())
ks_int_y = [y + m / 12 for y, m in ks_y]
vs_y = [ans_yes[k] for k in ks_y]
#
ks_n = sorted(ans_no.keys())
ks_int_n = [y + m / 12 for y, m in ks_n]
vs_n = [ans_no[k] for k in ks_n]

#
ks_int_y = ks_int_y[:-1]
vs_y = vs_y[:-1]
print(ks_int_y, vs_y)
#
ks_int_n = ks_int_n[:-1]
vs_n = vs_n[:-1]
print(ks_int_n, vs_n)
#
plt.figure(figsize=(8, 4))
plt.xlabel("Year", labelpad=8, fontsize=14)
plt.ylabel("Number of RSVPs (Per Month)", labelpad=8, fontsize=14)
#
plt.xlim([2004, 2014])
plt.xticks(list(range(2004, 2015, 1)))
plt.ylim([0, 18000])
p1, = plt.plot(ks_int_y, vs_y)
p2, = plt.plot(ks_int_n, vs_n)
plt.legend([p1, p2], ["yes", "no"])

plt.savefig("out2.png", dpi=200, bbox_inches='tight')

plt.show()
print()

# 平均每个Event参加的Member数.

# 2 Number of RSVPs
E, R = read_PKL(E=True, R=True)
ans_yes = defaultdict(int)
ans_no = defaultdict(int)
for e in E.values():
    rsvp_ids = e["rsvp_id_list"]
    t = (e['time_y'], e["time_m"])
    for id_ in rsvp_ids:
        r = R[id_]
        if r["response"] == 1:
            ans_yes[t] += 1
        else:
            ans_no[t] += 1

# 1 Number of Member
E = read_PKL(E=True)
ans = defaultdict(int)
for e in E.values():
    ans[(e['time_y'], e["time_m"])] += 1


for k, y in ans_yes.items():
    ans_yes[k] /= ans[k]
for k, y in ans_no.items():
    ans_no[k] /= ans[k]

ks_y = sorted(ans_yes.keys())
ks_int_y = [y + m / 12 for y, m in ks_y]
vs_y = [ans_yes[k] for k in ks_y]
#
ks_n = sorted(ans_no.keys())
ks_int_n = [y + m / 12 for y, m in ks_n]
vs_n = [ans_no[k] for k in ks_n]

#
ks_int_y = ks_int_y[:-1]
vs_y = vs_y[:-1]
print(ks_int_y, vs_y)
#
ks_int_n = ks_int_n[:-1]
vs_n = vs_n[:-1]
print(ks_int_n, vs_n)
#
plt.figure(figsize=(8, 4))
plt.xlabel("Year", labelpad=8, fontsize=14)
plt.ylabel("Number of RSVPs (Per Events)", labelpad=8, fontsize=14)
#
plt.xlim([2004, 2014])
plt.xticks(list(range(2004, 2015, 1)))
plt.ylim([0, 10])
p1, = plt.plot(ks_int_y, vs_y)
p2, = plt.plot(ks_int_n, vs_n)
plt.legend([p1, p2], ["yes", "no"])
plt.savefig("out3.png", dpi=200, bbox_inches='tight')

plt.show()