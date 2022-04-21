# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


def make_dataset(G, M, E, Dataset, E_features, M_features):
    X_train, y_train, X_test, y_test = Dataset
    X_train_ans, X_test_ans = [], []
    y_train_ans, y_test_ans = [], []
    class_name = E_features + M_features

    for X, y, X_ans, y_ans in zip([X_train, X_test], [y_train, y_test],
                                  [X_train_ans, X_test_ans], [y_train_ans, y_test_ans]):
        for i, (e_id, m_id) in enumerate(X):
            data = []
            e = E[e_id]
            if m_id not in M:
                continue
            m = M[m_id]
            for f in E_features:
                data.append(e[f])
            for f in M_features:
                data.append(m[f])
            #
            X_ans.append(data)
            y_ans.append(y[i])

    return X_train_ans, y_train_ans, X_test_ans, y_test_ans, class_name


from utils import read_PKL
import numpy as np
from sklearn.preprocessing import StandardScaler

G, M, E, Dataset = read_PKL(G=True, M=True, E=True, Dataset=True)
# *_rsvp_count, rating, tallies. 不能违背因果关系: rsvp_count; rating(评分要后面才会出现)
E_features = [
    "description", "why", "has_why", "has_description", "how_to_find_us", "has_how_to_find_us",
    *["updated" + s for s in ["_y", "_m", "_d", "_yd", "_wd"]],
    *["created" + s for s in ["_y", "_m", "_d", "_yd", "_wd"]],
    *["time" + s for s in ["_y", "_m", "_d", "_yd", "_wd"]],
    "duration", "utc_offset",
    "photo_url",
    "rsvp_limit",
    "fee_amount", "fee_accepts", "fee_currency", "fee_required",
    "has_venue", "venue_state", "venue_lat", "venue_repinned", "venue_country", "venue_lon"]
#
M_features = [
    "photo", "bio", "has_bio", "has_other_services", "other_services",
    "state", "lat", "country", "lon", "lang",
    *["joined" + s for s in ["_y", "_m", "_d", "_yd", "_wd"]],
    *["visited" + s for s in ["_y", "_m", "_d", "_yd", "_wd"]],
]

X_train, y_train, X_test, y_test, class_name = make_dataset(G, M, E, Dataset, E_features, M_features)
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
0.5396629712872326
(array([0.95999833, 0.50540316]), array([0.99632253, 0.08300341]), array([0.9778232 , 0.14258912]), array([161796,   7325], dtype=int64))
(0.7327007456445931, 0.5396629712872326, 0.5602061612758689, None)
0.9567646832741056
29 29
country 0.0005917733880061721
fee_currency 0.0008774542742347044
lang 0.0008882120631961317
fee_required 0.001846185216982206
duration 0.0018481249321648276
has_description 0.0019314753369072592
has_why 0.0028286836431251398
fee_accepts 0.003463550454386383
has_bio 0.00440261462509534
has_other_services 0.006723542648211703
why 0.00742683340341969
has_how_to_find_us 0.008684062893890397
photo_url 0.009030855313167645
photo 0.009032590271213203
utc_offset 0.011852507388576556
other_services 0.012345678936938987
fee_amount 0.01235139012398252
state 0.014043797433401495
rsvp_limit 0.029216813169256124
bio 0.030344399401460005
how_to_find_us 0.040477456130170106
lat 0.07620078708997281
lon 0.07884460701653082
description 0.09060673175946057
created 0.09697440058167026
updated 0.09877102284585677
time 0.09986146784422566
visited 0.11504677389766271
joined 0.13348620791683374
"""
