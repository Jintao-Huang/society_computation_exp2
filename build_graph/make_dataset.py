# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def make_dataset(G, M, E, R, V, Dataset, E_features, M_features, EG_features):
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
            # g
            for f in EG_features:
                data.append(g[f])
            # topics
            g_t = set(g["topics"])
            m_t = set(m["topics"])
            data += [len(g_t), len(m_t), len(g_t & m_t), len(g_t | m_t)]
            # venue
            #
            #
            X_ans.append(data)
            y_ans.append(y[i])

    return X_train_ans, y_train_ans, X_test_ans, y_test_ans


from utils import read_PKL
import numpy as np
from sklearn.preprocessing import StandardScaler

G, M, E, R, V, Dataset = read_PKL(G=True, M=True, E=True, R=True, V=True, Dataset=True)
# *_rsvp_count, group, rating. 不能违背因果关系: e.g: rsvp_count; rating(评分要后面才会出现)
E_features = ["description", "updated", "created", "utc_offset", "time", "photo_url",
              "why", "has_why", "has_description", "how_to_find_us", "has_how_to_find_us", "duration",
              "rsvp_limit", "fee_amount", "fee_accepts", "fee_currency", "fee_required"]
M_features = ["photo",
              "state", "joined", "lat", "lang", "country", "other_services",
              "visited", "lon", "bio", "has_bio", "has_other_services"]  # topics
# Topics = [gt, mt, &, |]
# organizer. *.list
EG_features = ["state",
               "category", "description", "rating", "join_mode", "created", "lat",
               "members", "group_photo", "lon", "has_description", "timezone"]

X_train, y_train, X_test, y_test = make_dataset(G, M, E, R, V, Dataset, E_features, M_features, EG_features)
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)
#
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#

print(len(X_train), len(X_test))  # 349763 85444
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, GridSearchCV
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score, precision_recall_fscore_support

class_weight = {0: 1, 1: 5}  # 1的准确率还好, 召回率很低
clf = RandomForestClassifier(20, max_depth=30, random_state=42, n_jobs=-1, verbose=1,
                             class_weight=class_weight)
clf.fit(X_train, y_train)
#
y_pred_train = clf.predict(X_train)
print(roc_auc_score(y_train, y_pred_train))
print(precision_recall_fscore_support(y_train, y_pred_train))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_train, y_pred_train, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_train, y_pred_train))

#
y_pred = clf.predict(X_test)
print(roc_auc_score(y_test, y_pred))
print(precision_recall_fscore_support(y_test, y_pred))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_test, y_pred, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_test, y_pred))
# [0]
# 0.6545896781609606
# (array([0.87490936, 0.86248625]), array([0.9893969 , 0.31978246]), array([0.92863778, 0.46657409]), array([70734, 14710], dtype=int64))
# (0.8686978061476607, 0.6545896781609606, 0.6976059337239735, None)
# 0.8741163803192734
# [0.07656352 0.07730543 0.0816024  0.00850657 0.08077359 0.00864168
#  0.00645051 0.00284031 0.00165949 0.03498487 0.00696852 0.00112604
#  0.0264197  0.01413719 0.00313926 0.00342474 0.00325356 0.00673757
#  0.01384834 0.22971376 0.06590174 0.00035043 0.0003311  0.0104494
#  0.11400794 0.06945074 0.03499141 0.00968588 0.0067343 ]

# [1]
# 0.7133854514967721
# (array([0.8950062 , 0.81631135]), array([0.97904827, 0.44772264]), array([0.9351428 , 0.57827729]), array([70734, 14710], dtype=int64))
# (0.8556587784846177, 0.713385451496772, 0.756710042185235, None)
# 0.8875754880389495
# [0.04807213 0.06447713 0.06586124 0.00791707 0.0701944  0.00664423
#  0.0042181  0.00203035 0.00154151 0.0213902  0.0058613  0.00081457
#  0.01542651 0.01131351 0.0055713  0.00534447 0.00632755 0.00551269
#  0.00677791 0.16598847 0.04014386 0.00023373 0.00024028 0.00801784
#  0.07671    0.04127448 0.02325299 0.00738738 0.0056954  0.00453822
#  0.02317589 0.03209952 0.02859929 0.00386092 0.05316354 0.0224544
#  0.08311705 0.00093622 0.0229453  0.00049468 0.00037439]

# [2]
# 0.7185893072228915
# (array([0.89682159, 0.81613645]), array([0.97851104, 0.45866757]), array([0.93588712, 0.58728294]), array([70734, 14710], dtype=int64))
# (0.8564790190180496, 0.7185893072228915, 0.761585028209229, None)
# 0.8890150273863583
# [0.04548452 0.06619134 0.06517897 0.00788318 0.06717386 0.0070418
#  0.00398391 0.00204667 0.00141202 0.02110833 0.00584148 0.0007004
#  0.01460192 0.01107145 0.00523724 0.00401007 0.00554104 0.00471398
#  0.0054373  0.14673003 0.03359998 0.00018388 0.00018699 0.00768297
#  0.06336484 0.03640259 0.02096193 0.00769385 0.00506194 0.00390693
#  0.01959368 0.02955253 0.02545513 0.00328601 0.04987998 0.02125965
#  0.07264088 0.00093231 0.01932407 0.00048706 0.0005811  0.01838462
#  0.02417601 0.01382297 0.0301886 ]
print(clf.feature_importances_)
exit(0)
#
# y_pred = cross_val_predict(clf, X_train, y_train, cv=3, method="predict_proba")
# if y_pred.ndim == 2 and y_pred.shape[1] == 2:
#     y_pred = y_pred[:, 1]
# print(roc_auc_score(y_test, y_pred))
# 0.7041257132924746 {'max_depth': 30, 'min_samples_leaf': 1, 'n_estimators': 1000}
# 0.6820650472907595
