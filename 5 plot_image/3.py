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
M = read_PKL(M=True)
ans = defaultdict(int)
for m in M.values():
    ans[len(m['event_list']) // 10] += 1
ks = sorted(ans.keys())
vs = [ans[k] for k in ks]


#
plt.figure(figsize=(8, 4))
plt.xlabel("Number of Events (Per Year)", labelpad=8, fontsize=14)
plt.ylabel("Number of Members", labelpad=8, fontsize=14)
#
plt.xlim([0, 50])
# plt.xticks(list(range(2004, 2015, 1)))
plt.ylim([0, 70000])
# p1, = plt.plot(ks, vs)
plt.bar(ks, vs)
plt.savefig("out6.png", dpi=200, bbox_inches='tight')

plt.show()
print()
# 最多的Member, 平均每年参加106个Event.

G = read_PKL(G=True)
ans = defaultdict(int)
for g in G.values():
    ans[len(g['event_list']) // 10] += 1
ks = sorted(ans.keys())
vs = [ans[k] for k in ks]


#
plt.figure(figsize=(8, 4))
plt.xlabel("Number of Events (Per Year)", labelpad=8, fontsize=14)
plt.ylabel("Number of Groups", labelpad=8, fontsize=14)
#
plt.xlim([0, 82])
plt.ylim([0, 100])
plt.bar(ks, vs)
plt.savefig("out7.png", dpi=200, bbox_inches='tight')

plt.show()
print()
# 最多的Member, 平均每年参加106个Event.
# 最多的Group, 平均每年组织80个活动

# Event参加的Member人数
E = read_PKL(E=True)
ans = defaultdict(int)
for e in E.values():
    if len(e['member_list']) == 0:
        print()
    ans[len(e['member_list'])] += 1
ks = sorted(ans.keys())
vs = [ans[k] for k in ks]
#
plt.figure(figsize=(8, 4))
plt.xlabel("Number of Members", labelpad=8, fontsize=14)
plt.ylabel("Number of Events", labelpad=8, fontsize=14)
#
plt.xlim([-0.5, 100])
plt.ylim([0, 30000])
plt.bar(ks, vs)
plt.savefig("out8.png", dpi=200, bbox_inches='tight')

plt.show()
print()
# 最多一个Events, 有421个Member参加. 大多数Events都没人参加.
