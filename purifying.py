def _purify_submissions_solved_status(submissions):
    for submission in submissions:
        if submission['solved_status'] == 'UK' or submission['result'] == 'AC':
            submission['solved_status'] = 'SO'


def _purify_submissions_unique_rows(submissions):
    users_solved_problems = {}
    for submission in submissions:
        user_id = submission['user_id']
        problem_id = submission['problem_id']
        users_solved_problems.setdefault(user_id, set())
        if submission['solved_status'] == 'SO':
            users_solved_problems[user_id].add(problem_id)

    final_submissions = []
    added_user_problems = set()
    for submission in submissions:
        user_id = submission['user_id']
        problem_id = submission['problem_id']
        if (user_id, problem_id) in added_user_problems:
            continue
        if submission['solved_status'] == 'SO':
            final_submissions.append(submission)
            added_user_problems.add((user_id, problem_id))
        else:
            if problem_id not in users_solved_problems[user_id]:
                final_submissions.append(submission)
                added_user_problems.add((user_id, problem_id))
    submissions.clear()
    submissions.extend(final_submissions)


def _purify_submissions_users_with_many_solved_problems(submissions, users):
    final_submissions = []
    for submission in submissions:
        user_id = submission['user_id']
        if users[user_id]['solved_count'] >= 3:
            final_submissions.append(submission)
    submissions.clear()
    submissions.extend(final_submissions)


def purify_submissions(submissions):
    _purify_submissions_solved_status(submissions)
    # _purify_submissions_unique_rows(submissions)
    # _purify_submissions_users_with_many_solved_problems(submissions, users)


def _purify_problems_levels(problems):
    real_levels = ('E', 'E-M', 'M', 'M-H', 'H')
    for problem_id in problems.keys():
        if problems[problem_id]['level'] not in real_levels:
            problems[problem_id]['level'] = 'E'


def purify_problems(problems):
    _purify_problems_levels(problems)


def _purify_users_user_type(users):
    allowed_user_types = ('S', 'W')
    for user_id in users.keys():
        if users[user_id]['user_type'] not in allowed_user_types:
            users[user_id]['user_type'] = 'NA'


def purify_users(users):
    _purify_users_user_type(users)
