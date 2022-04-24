# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from utils import read_PKL

from collections import defaultdict

G, M, E, R = read_PKL(G=True, M=True, E=True, R=True)

ans_yes = defaultdict(int)
ans_no = defaultdict(int)
from math import sqrt
import matplotlib.pyplot as plt

cnt_yes = 0
cnt_no = 0

for r in R.values():
    g_id, m_id = r["group"], r["member"]
    g = G[g_id]
    if m_id not in M:
        continue
    m = M[m_id]
    response = r["response"]
    t_g = set(g["topics"])
    t_m = set(m["topics"])
    if len(t_g) == 0 or len(t_m) == 0:
        sim = 0
    else:
        sim = len(t_g & t_m) / sqrt(len(t_g)) / sqrt(len(t_m))
    sim = int(sim * 10) / 10
    if response == 0:
        ans_no[sim] += 1
        cnt_no += 1
    else:
        cnt_yes += 1
        ans_yes[sim] += 1

# 1 Number of Member
ks_y = sorted(ans_yes.keys())
vs_y = [ans_yes[k] / cnt_yes for k in ks_y]
#
ks_n = sorted(ans_no.keys())
vs_n = [ans_no[k] / cnt_no for k in ks_n]
print(ks_y, vs_y)
print(ks_n, vs_n)
#
plt.figure(figsize=(7, 4))
plt.xlabel("Topics Cosine Similarity", labelpad=8, fontsize=14)
plt.ylabel("Proportion", labelpad=8, fontsize=14)
# #
# plt.xlim([2004, 2014])
# plt.xticks(list(range(2004, 2015, 1)))
# plt.ylim([0, 10])
p1, = plt.plot(ks_y, vs_y)
p2, = plt.plot(ks_n, vs_n)
plt.legend([p1, p2], ["yes", "no"])
plt.savefig("out11.png", dpi=200, bbox_inches='tight')
plt.show()
