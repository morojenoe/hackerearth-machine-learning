import pandas
import random

# test = pandas.read_csv('test/test.csv')
problems = pandas.read_csv('test/problems.csv')
m = {}
for i in range(len(problems)):
    m[problems.loc[i, 'problem_id']] = problems.loc[i, 'level']
tests = pandas.read_csv('test/test.csv')
result = pandas.DataFrame(index=range(0, len(tests)),
                          columns=['solved_status'])
m2 = {'E': 1, 'E-M': 1, 'M': 0, 'M-H': 0, 'H': 0}
for i in range(len(tests)):
    pid = tests.ix[i, 2]
    lvl = m[pid]
    r = m2.get(lvl, 0)
    result.ix[i] = r

for i in range(len(tests)):
    if result.solved_status[i] == 0:
        if random.randint(0, 99) < 70:
            result.solved_status[i] = random.randint(0, 1)
    else:
        if random.randint(0, 99) < 10:
            result.solved_status[i] = random.randint(0, 1)

result.to_csv('answers/answer1', index_label='Id')
