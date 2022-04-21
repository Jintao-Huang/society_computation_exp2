# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def make_dataset(G, M, E, Dataset, E_features, M_features):
    X_train, y_train, X_test, y_test = Dataset
    X_train_ans, X_test_ans = [], []
    y_train_ans, y_test_ans = [], []

    for X, y, X_ans, y_ans in zip([X_train, X_test], [y_train, y_test],
                                  [X_train_ans, X_test_ans], [y_train_ans, y_test_ans]):
        for i, (e_id, m_id) in enumerate(X):
            data = []
            e = E[e_id]
            if m_id not in M:
                continue
            m = M[m_id]
            g_id = e["group"]
            if g_id not in G:
                continue
            g = G[g_id]
            for f in E_features:
                data.append(e[f])
            for f in M_features:
                data.append(m[f])
            #
            X_ans.append(data)
            y_ans.append(y[i])

    return X_train_ans, y_train_ans, X_test_ans, y_test_ans


from utils import read_PKL
import numpy as np
from sklearn.preprocessing import StandardScaler

G, M, E, Dataset = read_PKL(G=True, M=True, E=True, Dataset=True)
# *_rsvp_count, group, rating. 不能违背因果关系: e.g: rsvp_count; rating(评分要后面才会出现)
E_features = ["description", "updated", "created", "utc_offset", "time", "photo_url",
              "why", "has_why", "has_description", "how_to_find_us", "has_how_to_find_us", "duration",
              "rsvp_limit", "fee_amount", "fee_accepts", "fee_currency", "fee_required"]
#
M_features = ["photo",
              "state", "joined", "lat", "lang", "country", "other_services",
              "visited", "lon", "bio", "has_bio", "has_other_services"]


ALL = E_features
X_train, y_train, X_test, y_test = make_dataset(G, M, E, Dataset, E_features, M_features)
X_train = np.array(X_train, dtype=np.float64)
y_train = np.array(y_train, dtype=np.float64)
X_test = np.array(X_test, dtype=np.float64)
y_test = np.array(y_test, dtype=np.float64)
#
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#

print(len(X_train), len(X_test))  # 693270 169126
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, precision_recall_fscore_support

class_weight = {0: 1, 1: 1}  # 1的准确率还好, 召回率很低
clf = RandomForestClassifier(20, max_depth=30, random_state=42, n_jobs=-1, verbose=1,
                             class_weight=class_weight)
clf.fit(X_train, y_train)
# train dataset
y_pred_train = clf.predict(X_train)
print(roc_auc_score(y_train, y_pred_train))
print(precision_recall_fscore_support(y_train, y_pred_train))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_train, y_pred_train, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_train, y_pred_train))

# test dataset
y_pred = clf.predict(X_test)
print(roc_auc_score(y_test, y_pred))
print(precision_recall_fscore_support(y_test, y_pred))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_test, y_pred, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_test, y_pred))
# [0] baseline
# (array([0.96059497, 0.5815739 ]), array([0.99730678, 0.08382902]), array([0.97860669, 0.14653609]), array([161888,   7229], dtype=int64))
# (0.7710844344178449, 0.540567900995395, 0.5625713911091719, None)
# 0.9582596663848105
# [0.08888584 0.09585143 0.09528936 0.01231575 0.09813565 0.00937589
#  0.00779279 0.00290008 0.00198898 0.03972715 0.00788892 0.00208347
#  0.02945377 0.01322366 0.00344538 0.00111985 0.00203183 0.00988266
#  0.01532697 0.13510434 0.07725512 0.00139875 0.00068401 0.01182234
#  0.11270702 0.07869042 0.03358068 0.00488548 0.00715242]
