import pandas


if __name__ == '__main__':
    tests = pandas.read_csv('test/test.csv')
    train_users = pandas.read_csv('train/users.csv')
    train_problems = pandas.read_csv('train/problems.csv')

    known_problems = set(train_problems.problem_id.tolist())
    known_users = set(train_users.user_id.tolist())

    res = [[0, 0], [0, 0]]
    for index, test in tests.iterrows():
        u = 1 if test.user_id in known_users else 0
        p = 1 if test.problem_id in known_problems else 0
        res[u][p] += 1
    print(*res, sep='\n')
