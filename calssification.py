import sklearn.ensemble
import xgboost


def classify_xgb(train_data, train_labels, test_data):
    dtrain = xgboost.DMatrix(data=train_data, label=train_labels)
    params = {'booster': 'gbtree',
              'eta': 0.3,
              'gamma': 0,
              'max_depth': 6,
              'min_child_weight': 1,
              'max_delta_step': 0,
              'subsample': 1,
              'colsample_bytree': 1,

              'objective': 'binary:logistic',
              'base_score': 0.5,
              'eval_metric': 'error',
              }
    classifier = xgboost.train(params=params, dtrain=dtrain)
    test_data = xgboost.DMatrix(test_data)
    return classifier.predict(test_data)


def classify_sklearn(train_data, train_labels, test_data):
    classifier = sklearn.ensemble.GradientBoostingClassifier(loss='deviance',
                                                             learning_rate=0.1,
                                                             n_estimators=50,
                                                             subsample=1.0,
                                                             min_samples_split=4,
                                                             min_samples_leaf=5,
                                                             max_depth=10)
    classifier.fit(train_data, train_labels)
    return classifier.predict(test_data)
