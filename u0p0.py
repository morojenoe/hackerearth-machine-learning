import numpy
import time

import calssification
import data2feature_vector
import main
import purifying
import utils
import u1p1

PROBLEM_FEATURES = 2
USER_FEATURES = 2
NUMBER_OF_FEATURES = PROBLEM_FEATURES + USER_FEATURES  # + len(explore_problems.REAL_TAGS)


def _get_problem_features(problem_id, problems):
    # levels = {'E': 0, 'E-M': 1, 'M': 2, 'M-H': 3, 'H': 4}
    result = numpy.zeros(shape=(PROBLEM_FEATURES,))
    solved_count = problems[problem_id]['solved_count']
    error_count = problems[problem_id]['error_count']
    # rating = problems[problem_id]['rating']
    accuracy = problems[problem_id]['accuracy']
    # problem_tags = problems[problem_id]['tags']
    # level = problems[problem_id]['level']
    result[0] = solved_count / (solved_count + error_count)
    result[1] = accuracy
    # for index, tag in enumerate(explore_problems.REAL_TAGS, start=2):
    #     result[index] = 1 if tag in problem_tags else 0
    # result[2] = rating
    # result[2] = levels[level]
    return result


def _get_users_features(user_id, users):
    # users_types = {'S': 0, 'W': 1, 'NA': 2}
    result = numpy.zeros(shape=(USER_FEATURES,))
    result[0] = users[user_id]['solved_count']
    result[1] = users[user_id]['attempts']
    # result[2] = users_types[users[user_id]['user_type']]
    return result


def get_feature_vector(problem_id, problems, user_id, users):
    result = _get_problem_features(problem_id, problems)
    result = numpy.concatenate((result, _get_users_features(user_id, users)))
    assert len(result) == NUMBER_OF_FEATURES
    return result


def solution(tests, train_problems, train_users, test_problems, test_users,
             submissions):
    purifying._purify_submissions_unique_rows(submissions)
    return utils.solve(train_problems, train_users, submissions, tests,
                       test_problems, test_users, NUMBER_OF_FEATURES,
                       get_feature_vector)


if __name__ == '__main__':
    main.update_answers(0, 0)
