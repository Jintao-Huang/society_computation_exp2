# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


# random+yes+p
# random+yes+r
# random+no+p
# random+no+r


# last+yes+p
# last+yes+r
# last+no+p
# last+no+r
# Backbone, Number of Trees, AUE; F1
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.xlabel("Settings (with Graph Info)", labelpad=8, fontsize=14)
plt.ylabel("Metrics", labelpad=8, fontsize=14)
#
plt.xlim([0.7, 2.3])
plt.xticks([1, 2], ["Random", "Last"])
plt.ylim([0.4, 0.9])

x = [1, 2]
# array([0.71046438, 0.75973601]), array([0.65022876, 0.80623694])  # random
# array([0.63737941, 0.70069048]), array([0.43433171, 0.84608142])  # Last


yp = [0.75973601, 0.70069048]
yr = [0.80623694, 0.84608142]
np = [0.71046438, 0.63737941]
nr = [0.65022876, 0.43433171]
p1, = plt.plot(x, yp)
p2, = plt.plot(x, yr)
p3, = plt.plot(x, np)
p4, = plt.plot(x, nr)
plt.legend([p1, p2, p3, p4], ["Yes+Precision", "Yes+Recall", "No+Precision", "No+Recall"])
plt.savefig("out10.png", dpi=200, bbox_inches='tight')
plt.show()
print()

