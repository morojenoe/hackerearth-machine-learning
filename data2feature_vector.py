import numpy


def get_train_data(problems, users, submissions, number_of_features,
                   get_feature_vector):
    data = numpy.zeros(shape=(len(submissions), number_of_features))
    labels = numpy.zeros(shape=(len(submissions),), dtype=numpy.int8)
    for index, submission in enumerate(submissions):
        user_id = submission['user_id']
        problem_id = submission['problem_id']
        data[index] = get_feature_vector(problem_id, problems, user_id, users)
        solved_status = submission['solved_status']
        result = submission['result']
        labels[index] = 1 if solved_status == 'SO' and result == 'AC' else 0
    return data, labels


def get_test_data(tests, problems, users, number_of_features,
                  get_feature_vector):
    data = numpy.zeros(shape=(len(tests), number_of_features))
    for index, test in enumerate(tests):
        user_id = test['user_id']
        problem_id = test['problem_id']
        data[index] = get_feature_vector(problem_id, problems, user_id, users)
    return data
