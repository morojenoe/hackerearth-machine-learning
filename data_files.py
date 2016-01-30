import numpy
import pandas
import pickle

import time

import purifying

_PATH_TO_TRAIN_PROBLEMS = 'pickle_dumps/train_problems'
_PATH_TO_TEST_PROBLEMS = 'pickle_dumps/test_problems'
_PATH_TO_TRAIN_USERS = 'pickle_dumps/train_users'
_PATH_TO_TEST_USERS = 'pickle_dumps/test_users'
_PATH_TO_SUBMISSIONS = 'pickle_dumps/submissions'


def _get_problem_tags(problem):
    tags_name = ('tag1', 'tag2', 'tag3', 'tag4', 'tag5')
    result = set()
    for tag in tags_name:
        result.add(problem.get(tag))
    return result


def _get_dict_from_problems(problems):
    result = {}
    for index, problem in problems.iterrows():
        tags = _get_problem_tags(problem)
        result[problem.problem_id] = {'solved_count': problem.solved_count,
                                      'error_count': problem.error_count,
                                      'accuracy': problem.accuracy,
                                      'level': problem.level,
                                      'rating': problem.rating,
                                      'tags': tags}
    return result


def _get_dict_from_users(users):
    result = {}
    for user in numpy.array(users):
        skills = user[1].split('|') if not pandas.isnull(user[1]) else []
        result[user[0]] = {'skills': skills,
                           'solved_count': user[2],
                           'attempts': user[3],
                           'user_type': user[4]}
    return result


def _get_dict_from_submissions(submissions):
    result = []
    for index, submission in enumerate(numpy.array(submissions)):
        item = {'user_id': submission[0],
                'problem_id': submission[1],
                'solved_status': submission[2],
                'result': submission[3],
                'language_used': submission[4],
                'execution_time': submission[5]}
        result.append(item)
    return result


def _load(path_to_obj):
    with open(path_to_obj, 'rb') as file:
        return pickle.load(file)


def _get_problems(path_to_problems):
    problems = pandas.read_csv(path_to_problems)
    return _get_dict_from_problems(problems)


def get_train_problems():
    return _load(_PATH_TO_TRAIN_PROBLEMS)


def get_test_problems():
    return _load(_PATH_TO_TEST_PROBLEMS)


def get_submissions():
    return _load(_PATH_TO_SUBMISSIONS)


def _get_users(path_to_users):
    users = pandas.read_csv(path_to_users)
    return _get_dict_from_users(users)


def get_train_users():
    return _load(_PATH_TO_TRAIN_USERS)


def get_test_users():
    return _load(_PATH_TO_TEST_USERS)


def _dump(obj, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file)


def build_dump():
    train_problems = _get_problems('train/problems.csv')
    test_problems = _get_problems('test/problems.csv')
    train_users = _get_users('train/users.csv')
    test_users = _get_users('test/users.csv')
    submissions = _get_dict_from_submissions(pandas.read_csv('train/submissions.csv'))

    purifying.purify_problems(train_problems)
    purifying.purify_problems(test_problems)
    purifying.purify_users(train_users)
    purifying.purify_users(test_users)
    purifying.purify_submissions(submissions)

    _dump(train_problems, _PATH_TO_TRAIN_PROBLEMS)
    _dump(test_problems, _PATH_TO_TEST_PROBLEMS)
    _dump(train_users, _PATH_TO_TRAIN_USERS)
    _dump(test_users, _PATH_TO_TEST_USERS)
    _dump(submissions, _PATH_TO_SUBMISSIONS)


def measure_load_time():
    cur = time.clock()
    get_submissions()
    print('Submissions =', cur - time.clock())


if __name__ == '__main__':
    measure_load_time()
