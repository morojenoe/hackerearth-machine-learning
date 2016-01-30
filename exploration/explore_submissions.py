import pandas


def get_solved_status(submissions):
    return submissions.solved_status.value_counts()


if __name__ == '__main__':
    submissions = pandas.read_csv('../train/submissions.csv')
    a = {}
    for submit in submissions.values:
        a.setdefault((submit[0], submit[1]), [])
        result = 1 if submit[2] == 'SO' else 0
        a[(submit[0], submit[1])].append(result)
    cnt = 0
    for key in a.keys():
        flag = True
        one = False
        for e in a[key]:
            if e == 1:
                if one == 1:
                    flag = False
                one = True
            else:
                if one == 1:
                    flag = False
        if not flag:
            print(a[key])
            cnt += 1
    print(cnt)
    print(len(a))
