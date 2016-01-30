import pandas
import matplotlib.pyplot as plt
import matplotlib as mplt


def get_skills(users):
    skills = {}
    for user_skill in users.skills:
        if not pandas.isnull(user_skill):
            for skill in user_skill.split('|'):
                skills.setdefault(skill, 0)
                skills[skill] += 1
    return skills


def get_solved_count(users):
    solved = {}
    for solved_count in users.solved_count:
        solved.setdefault(solved_count, 0)
        solved[solved_count] += 1
    return solved


def draw_hist_solved_count(solved_count):
    solved_count = list(solved_count.items())
    data = []
    for t in solved_count:
        if t[0] >= 0:
            data.extend([t[0] // 50] * t[1])
    plt.hist(x=data, bins=30)
    plt.show()


def get_user_type(users):
    user_types = {}
    for user_type in users.user_type:
        user_types.setdefault(user_type, 0)
        user_types[user_type] += 1
    return user_types


def get_user_attempts(users):
    users.attempts.hist()
    result = []
    for attempts in users.attempts:
        result.append(attempts)
    return result


def draw_hist_attempts(attempts):
    attempts = list(filter(lambda attempt: attempt < 50, attempts))
    print(len(attempts))
    plt.hist(x=attempts, bins=30)
    plt.show()


def get_all_ids(users):
    return set(users.user_id.tolist())


def explore_data(users):
    skills = get_skills(users)
    skills = sorted(skills.items(), key=lambda skill: skill[1], reverse=True)
    print("\n".join(str(skill) for skill in skills))

    # solved_count = get_solved_count(users)
    # print("\n".join(str(cnt) for cnt in solved_count))
    # draw_hist_solved_count(solved_count)

    # print(get_user_type(users))

    attempts = get_user_attempts(users)
    attempts = sorted(attempts)
    draw_hist_attempts(attempts)


def check_that_users_coincide_in_both_df(users_id, test_users, train_users):
    for user_id in users_id:
        expr = 'user_id == {}'.format(user_id)
        test_record = test_users.query(expr)
        train_record = train_users.query(expr)
        if not test_record.iloc[0].equals(train_record.iloc[0]):
            return False
    return True


def check_that_users_with_equal_ids_coincide_in_both_df(train_users,
                                                        test_users):
    train_ids = get_all_ids(train_users)
    test_ids = get_all_ids(test_users)
    assert check_that_users_coincide_in_both_df(
        list(train_ids.intersection(test_ids)),
        test_users,
        train_users)


def print_info_about_train_and_test_users(train_users, test_users):
    train_ids = get_all_ids(train_users)
    test_ids = get_all_ids(test_users)
    print('L_train_users =', len(train_users))
    print('L_test_users =', len(test_ids))
    print('L_intersection =', len(train_ids.intersection(test_ids)))


if __name__ == '__main__':
    train_users = pandas.read_csv('../train/users.csv')
    test_users = pandas.read_csv('../test/users.csv')

    all_users = pandas.concat((train_users, test_users), ignore_index=True,
                              verify_integrity=True)
    all_users.drop_duplicates()
    # print_info_about_train_and_test_users(train_users, test_users)
    # print(all_users.user_type.value_counts())
    print(all_users)

