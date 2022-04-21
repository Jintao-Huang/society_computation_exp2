# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def make_dataset(G, M, E, Dataset, E_features, M_features, EG_features):
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
# venue
E_features += ["venue_state", "venue_country", "venue_lon", "venue_lat", "venue_repinned", "has_venue", "event_hosts"]
#
M_features = ["photo",
              "state", "joined", "lat", "lang", "country", "other_services",
              "visited", "lon", "bio", "has_bio", "has_other_services",
              "group_list", "event_list"]  # topics
# organizer. *.list
EG_features = ["state",
               "category", "description", "rating", "join_mode", "created", "lat",
               "members", "group_photo", "lon", "has_description", "timezone",
               "rsvp_id_list", "member_list", "event_list",
               "headcount", "rating_average", "rating_count", "tallies_maybe",
               "tallies_waitlist", "tallies_no", "tallies_yes", "organizer"
               ]
# Topics = [gt, mt, &, |]
ALL = E_features
X_train, y_train, X_test, y_test = make_dataset(G, M, E, Dataset, E_features, M_features, EG_features)
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

class_weight = {0: 1, 1: 1}  # 1的准确率还好, 召回率很低
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
#