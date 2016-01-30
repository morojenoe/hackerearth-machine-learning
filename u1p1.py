import time

import numpy

import main
import utils
import exploration.explore_problems
import purifying

PROBLEM_FEATURES = 2
USER_FEATURES = 2
COMMON_FEATURES = len(exploration.explore_problems.REAL_TAGS)
NUMBER_OF_FEATURES = PROBLEM_FEATURES + USER_FEATURES + COMMON_FEATURES


def get_problem_features(problem_id, problems):
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


def get_users_features(user_id, users):
    # users_types = {'S': 0, 'W': 1, 'NA': 2}
    result = numpy.zeros(shape=(USER_FEATURES,))
    result[0] = users[user_id]['solved_count']
    result[1] = users[user_id]['attempts']
    # result[2] = users_types[users[user_id]['user_type']]
    return result


def get_common_features(problem, user):
    result = numpy.zeros(shape=(COMMON_FEATURES,))
    for index, tag in enumerate(exploration.explore_problems.REAL_TAGS):
        if tag in problem['tags']:
            result[index] = -1
        if tag in user['solved_tags']:
            result[index] = 1

    # result[0] = problem['solved_count'] - user['min_solved_count']
    return result


def get_feature_vector(problem_id, problems, user_id, users):
    result = numpy.concatenate((get_problem_features(problem_id, problems),
                                get_users_features(user_id, users),
                                get_common_features(problems[problem_id],
                                                    users[user_id])))
    assert len(result) == NUMBER_OF_FEATURES
    return result


def get_feature_vector_for_low(problem_id, problems, user_id, users):
    result = numpy.concatenate((get_problem_features(problem_id, problems),
                                get_users_features(user_id, users)))
    assert len(result) == NUMBER_OF_FEATURES
    return result


def _extend_users_min_solved_count(problems, users, submissions):
    for user_id in users.keys():
        users[user_id]['min_solved_count'] = 10 ** 4
    for submit in submissions:
        user_id = submit['user_id']
        problem_id = submit['problem_id']
        if submit['solved_status'] == 'SO':
            users[user_id]['min_solved_count'] = min(
                    users[user_id]['min_solved_count'],
                    problems[problem_id]['solved_count'])


def _extend_users_solved_tags(problems, users, submissions):
    for user_id in users.keys():
        users[user_id]['solved_tags'] = set()
    for submit in submissions:
        user_id = submit['user_id']
        problem_id = submit['problem_id']
        if submit['solved_status'] == 'SO':
            users[user_id]['solved_tags'] |= set(problems[problem_id]['tags'])


def extend_data(problems, users, submissions):
    _extend_users_min_solved_count(problems, users, submissions)
    _extend_users_solved_tags(problems, users, submissions)


def split_submissions(submissions, users):
    sbmt_low = []
    sbmt_high = []
    for submit in submissions:
        user_id = submit['user_id']
        if users[user_id]['solved_count'] <= 5:
            sbmt_low.append(submit)
        else:
            sbmt_high.append(submit)
    return sbmt_low, sbmt_high


def split_tests(tests, users):
    test_low = []
    test_high = []
    ids_low = []
    ids_high = []
    for index, test in enumerate(tests):
        user_id = test['user_id']
        if users[user_id]['solved_count'] <= 5:
            test_low.append(test)
            ids_low.append(index)
        else:
            test_high.append(test)
            ids_high.append(index)
    return test_low, test_high, ids_low, ids_high


def solution(tests, train_problems, train_users, test_problems, test_users,
             submissions):
    print('u1p1 has started, time =', time.clock())
    purifying._purify_submissions_unique_rows(submissions)
    extend_data(train_problems, train_users, submissions)
    return utils.solve(train_problems, train_users, submissions, tests,
                       train_problems, train_users, NUMBER_OF_FEATURES,
                       get_feature_vector)
    # sbmt_low, sbmt_high = split_submissions(submissions, train_users)
    # test_low, test_high, ids_low, ids_high = split_tests(tests, train_users)

    # purifying._purify_submissions_unique_rows(sbmt_high)

    # answer_labels = [0] * len(tests)
    # temp_labels = utils.solve(train_problems, train_users, sbmt_low, test_low,
    #                           train_problems, train_users,
    #                           NUMBER_OF_FEATURES,
    #                           get_feature_vector_for_low)
    # utils.apply_results(answer_labels, temp_labels, ids_low)
    # temp_labels = utils.solve(train_problems, train_users, sbmt_high,
    #                           test_high, train_problems, train_users,
    #                           NUMBER_OF_FEATURES,
    #                           get_feature_vector_for_low)
    # utils.apply_results(answer_labels, temp_labels, ids_high)
    #
    # print('u1p1 has ended, time =', time.clock())
    # return answer_labels


if __name__ == '__main__':
    main.update_answers(1, 1)
