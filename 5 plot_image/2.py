# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

import matplotlib.pyplot as plt

# Backbone, Number of Trees, AUE; F1
plt.figure(figsize=(6, 4))
plt.xlabel("Settings (Random)", labelpad=8, fontsize=14)
plt.ylabel("Metrics", labelpad=8, fontsize=14)
#
plt.xlim([0.5, 3.5])
plt.xticks([1, 2, 3], ["Backbone", "with Group Info", "with Graph Info"])
plt.ylim([0.68, 0.75])

x = [1, 2, 3]

auc = [0.6968438992465513, 0.7227328450580986, 0.7282328457519213]
acc = [0.7171896753446236, 0.7369552855359396, 0.7407919708744844]
f1 = [0.700056935, 0.7255266300000001, 0.72927571]
p1, = plt.plot(x, auc)
p2, = plt.plot(x, acc)
p3, = plt.plot(x, f1)
plt.legend([p1, p2, p3], ["AUC", "ACC", "F1"])
plt.savefig("out4.png", dpi=200, bbox_inches='tight')
plt.show()
print()

# Backbone, Number of Trees, AUE; F1
plt.figure(figsize=(6, 4))
plt.xlabel("Settings (Last)", labelpad=8, fontsize=14)
plt.ylabel("Metrics", labelpad=8, fontsize=14)
#
plt.xlim([0.5, 3.5])
plt.xticks([1, 2, 3], ["Backbone", "with Group Info", "with Graph Info"])
plt.ylim([0.56, 0.72])

x = [1, 2, 3]

auc = [0.5932394647414587, 0.6249995890514206, 0.6402065690541658]
acc = [0.6589277121037765, 0.678553195940998, 0.6838152526414897]
f1 = [0.5776151885964096, 0.6215426653890038, 0.6413591387212605]
p1, = plt.plot(x, auc)
p2, = plt.plot(x, acc)
p3, = plt.plot(x, f1)
plt.legend([p1, p2, p3], ["AUC", "ACC", "F1"])
plt.savefig("out5.png", dpi=200, bbox_inches='tight')
plt.show()
print()
