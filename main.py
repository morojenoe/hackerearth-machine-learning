import pandas

import data_files
import purifying
import u0p0
import u0p1
import u1p0
import u1p1
import utils

ANSWER_FILE = 'answers/answer7'


def update_answers(user_label, problem_label):
    train_problems = data_files.get_train_problems()
    train_users = data_files.get_train_users()
    submissions = data_files.get_submissions()
    test_problems = data_files.get_test_problems()
    test_users = data_files.get_test_users()

    tests_df = pandas.read_csv('test/test.csv')

    known_problems = set(train_problems.keys())
    known_users = set(train_users.keys())

    queries = []
    for test in tests_df.values:
        user_id = test[1]
        problem_id = test[2]
        u = 1 if user_id in known_users else 0
        p = 1 if problem_id in known_problems else 0
        if u == user_label and p == problem_label:
            queries.append({'index': test[0], 'user_id': user_id,
                            'problem_id': problem_id})
    solutions = [[u0p0.solution, u0p0.solution],
                 [u0p0.solution, u1p1.solution]]
    answers = solutions[user_label][problem_label](queries, train_problems,
                                                   train_users, test_problems,
                                                   test_users, submissions)
    result = pandas.read_csv(ANSWER_FILE)
    result = result.solved_status.tolist()
    for index, answer in enumerate(answers):
        query_id = queries[index]['index']
        result[query_id] = answer
    utils.save_answer(result, ANSWER_FILE)


def main():
    for u in range(2):
        for p in range(2):
            update_answers(u, p)


if __name__ == '__main__':
    main()
