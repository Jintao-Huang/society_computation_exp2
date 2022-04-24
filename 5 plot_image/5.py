# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 最重要的8个特性

from utils import read_PKL
from collections import defaultdict
import matplotlib.pyplot as plt

# Event参加的Member人数
x = ["M_joined", "M_lat", "M_lon", "M_visited", "E_description", "E_time", "M_is_event_hosts", "MG_topics_sim"]
y = [0.068166026437135084, 0.04303265829562348, 0.04267157564101918, 0.040820004110159477, 0.032008909943889264,
     0.030616624489678332, 0.029664258270002432, 0.028043610516526216]



#
plt.figure(figsize=(8, 6))
plt.xlabel("Features (Top 8)", labelpad=8, fontsize=14)
plt.ylabel("Importance of Features", labelpad=8, fontsize=14)
plt.xticks(range(0, 8), x, rotation=90, fontsize=11)
#
plt.ylim([0, 0.1])
plt.bar(x, y, width=0.6)
plt.savefig("out9.png", dpi=200, bbox_inches='tight')
plt.show()