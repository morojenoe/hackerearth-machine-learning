import pandas

import calssification
import data2feature_vector


def save_answer(data, file_name):
    data = pandas.DataFrame(data=data, index=range(len(data)),
                            columns=['solved_status'])
    data.to_csv(file_name, index_label='Id')


def solve(train_problems, train_users, submissions,
          tests, test_problems, test_users,
          number_of_features, get_feature_vector):
    train_data, train_labels = data2feature_vector.get_train_data(
            train_problems,
            train_users,
            submissions,
            number_of_features,
            get_feature_vector)
    test_data = data2feature_vector.get_test_data(tests,
                                                  test_problems,
                                                  test_users,
                                                  number_of_features,
                                                  get_feature_vector)
    test_labels = calssification.classify_xgb(train_data, train_labels,
                                              test_data)
    test_labels = [0 if label < 0.5 else 1 for label in test_labels]
    return test_labels


def apply_results(answer_labels, temp_labels, indexes):
    assert len(temp_labels) == len(indexes)
    for index, label in enumerate(temp_labels):
        answer_labels[indexes[index]] = label
