import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score, ShuffleSplit

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel
from sklearn.utils import safe_mask
from configs.path_config import DATA_PATH_HOME



plt.style.use('ggplot')
df = pd.read_csv(DATA_PATH_HOME + "feature/train.csv", low_memory=False, index_col='EID')
df_test = pd.read_csv(DATA_PATH_HOME + "feature/test.csv", low_memory=False, index_col='EID')
X_train = df.drop(['TARGET'],axis=1)
y_train = df['TARGET']
X_test = df_test
#X_selection = SelectFromModel(RandomForestClassifier()).fit(X_train,y_train)
#X_mask = X_selection.get_support()
#X_mask = safe_mask(X_train,X_mask)
#print(X_mask)

ans_matrix = []
for i in range(0,10):
    number_default_1 = len(df[df.TARGET == 1])
    default_1 = np.array(df[df.TARGET == 1].index)
    default_0 = df[df.TARGET == 0].index
    random_default_0 = np.random.choice(default_0, int(number_default_1), replace = False)
    under_sample_default_0 = np.array(random_default_0)
    under_sample_indices = np.concatenate([default_1,under_sample_default_0])
    #print(len(under_sample_indices))
    df_undersample = df.loc[under_sample_indices]
    class_counts = df_undersample.groupby('TARGET')['TARGET'].agg({
            'count': len,
            'ratio': lambda x: float(len(x)) / len(df_undersample)


        })
    print(class_counts)
    X_train = df_undersample.drop(['TARGET'],axis=1)
    y_train = df_undersample['TARGET']
    X_train_s = np.array(X_train)
    X_test_s = np.array(X_test)
    #X_train_s = np.array(X_train)
    #X_test_s = np.array(X_test)
    clf = RandomForestClassifier(n_estimators=60, random_state=0)
    clf.fit(X_train_s, y_train)
    y_pred = clf.predict_proba(X_test_s)[:,1]
    ans_matrix.append(y_pred)

    clf = GradientBoostingClassifier(n_estimators=60, learning_rate=0.15, random_state=42);
    clf.fit(X_train_s, y_train)
    y_pred = clf.predict_proba(X_test_s)[:,1]
    ans_matrix.append(y_pred)
    '''
    clf = LogisticRegression(C=1, penalty='l2')
    clf.fit(X_train_s, y_train)
    y_pred = clf.predict_proba(X_test_s)[:,1]
    ans_matrix.append(y_pred)
    '''
'''
X_selection = SelectFromModel(GradientBoostingClassifier()).fit(X_train,y_train)
X_mask = X_selection.get_support()
X_mask = safe_mask(X_train,X_mask)
print(X_mask)
X_train_selected = np.array(X_train)[:,X_mask]
X_test_selected = np.array(X_test)[:,X_mask]
#SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(np.array(X_train), np.array(y_train))
print(np.array(X_train).shape)
print(X_train_selected.shape)
'''
#y_result = []
#print(ans_matrix)
ans_array = np.array(ans_matrix)
'''
for i in range(0,len(X_test)):
    t = 0
    for j in range(0,len(ans_matrix)):
        if ans_matrix[j][i] == 0:
            t -= 1
        else:
            t += 1
    #print(t)
    if t>0 :
        y_result.append(1)
    else:
        y_result.append(0)

y_result = np.array(y_result)
'''
y_result = np.mean(ans_array,axis=0)
print(y_result)
df_test['TARGET'] = pd.Series(y_result, index=df_test.index)
result = df_test[['TARGET']]
result.to_csv("result.csv",encoding='utf-8')