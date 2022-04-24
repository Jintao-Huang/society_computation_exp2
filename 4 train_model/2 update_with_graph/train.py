# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def make_dataset(G, M, E, Dataset, E_features, M_features, G_features):
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
            for f in G_features:
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
from utils import attr_to_bool, attr_to_float, attr_to_len, \
    read_PKL, attr_to_int, default_using_median, remove_attr, save_PKL, unzip_venue, move_E_to_G, \
    handle_organizer_event_hosts

G, M, E, Dataset = read_PKL(G=True, M=True, E=True, Dataset=True)

# add organizer. event_hosts
handle_organizer_event_hosts(M, G, E)
attr_to_bool(G, ["organizer"])
attr_to_len(E, ["event_hosts"])
# G
attr_to_len(G, ["rsvp_id_list", "member_list", "event_list"])
# E
attr_names = ["headcount", "rating_average", "rating_count", "tallies_maybe",
              "tallies_waitlist", "tallies_no", "tallies_yes"]
move_E_to_G(E, G, attr_names)  # mean E to G. 有些特征E用不了
# M
attr_to_len(M, ["group_list", "event_list"])

# *_rsvp_count, rating, tallies. 不能违背因果关系: rsvp_count; rating(评分要后面才会出现)
t = ["_y", "_m", "_d", "_yd", "_wd"]
E_features = [
    "description", "why", "has_why", "has_description", "how_to_find_us", "has_how_to_find_us",
    *["updated" + s for s in t],
    *["created" + s for s in t],
    *["time" + s for s in t],
    "duration", "utc_offset",
    "photo_url",
    "rsvp_limit",
    "fee_amount", "fee_accepts", "fee_currency", "fee_required",
    "has_venue", "venue_state", "venue_lat", "venue_repinned", "venue_country", "venue_lon",
    #
    "event_hosts"
]
#
M_features = [
    "photo", "bio", "has_bio", "has_other_services", "other_services",
    "state", "lat", "country", "lon", "lang",
    *["joined" + s for s in t],
    *["visited" + s for s in t],
    #
    "is_organizer", "is_event_hosts"
]
#
G_features = [
    "state", "lat", "lon",
    *["created" + s for s in t], "timezone",
    "category", "description", "rating", "join_mode",
    "members", "group_photo", "has_description",
    #
    "organizer",
    #
    "rsvp_id_list", "member_list", "event_list",
    #
    "headcount", "rating_average", "rating_count", "tallies_maybe",
    "tallies_waitlist", "tallies_no", "tallies_yes"
]
X_train, y_train, X_test, y_test = make_dataset(G, M, E, Dataset, E_features, M_features, G_features)
class_name = E_features + M_features + G_features + ["topics_%d" % i for i in range(4)]

X_train = np.array(X_train, dtype=np.float64)
y_train = np.array(y_train, dtype=np.float64)
X_test = np.array(X_test, dtype=np.float64)
y_test = np.array(y_test, dtype=np.float64)
#
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
#

print(len(X_train), len(X_test))  # 693270 169126
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, precision_recall_fscore_support

class_weight = {0: 1, 1: 1}
clf = RandomForestClassifier(20, random_state=42, n_jobs=-1, verbose=1,
                             class_weight=class_weight)
clf.fit(X_train, y_train)
#
y_pred = clf.predict(X_train)
print(roc_auc_score(y_train, y_pred))
print(precision_recall_fscore_support(y_train, y_pred))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_train, y_pred, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_train, y_pred))
# test dataset
y_pred = clf.predict(X_test)
print(roc_auc_score(y_test, y_pred))
print(precision_recall_fscore_support(y_test, y_pred))  # precision, recall, fbeta_score, _
print(precision_recall_fscore_support(y_test, y_pred, average="macro"))  # precision, recall, fbeta_score, _
print(accuracy_score(y_test, y_pred))
#
imp = clf.feature_importances_
print(len(class_name), len(imp))

idxs = sorted(range(len(imp)), key=lambda i: imp[i])
class_name = [class_name[i] for i in idxs]
imp = [imp[i] for i in idxs]
for cn, x in zip(class_name, imp):
    print(cn, x)
"""
M, E -> 0,1
1. M的特征
2. E的特征
3. E对应G的特征. [topics的交并信息]
4. Graph
    G: "rsvp_id_list", "member_list", "event_list"
    from E: "headcount", "rating_average", "rating_count", "tallies_maybe",
              "tallies_waitlist", "tallies_no", "tallies_yes". 
    M: "group_list", "event_list"; organizer. event_hosts
"""
