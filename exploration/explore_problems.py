import numpy
import pandas

map_tags = {'Algorithms': None,
            'Math': 'Math',
            'Ad-Hoc': 'Implementation',
            'Basic Programming': 'Implementation',
            'Dynamic Programming': 'Dynamic Programming',
            'Data Structures': 'Data Structures',
            'Implementation': 'Implementation',
            'Sorting': None,
            'Greedy': 'Implementation',
            'Graph Theory': 'Simple Graph Theory',
            'Number Theory': 'Math',
            'Combinatorics': 'Math',
            'Binary Search': None,
            'DFS': 'Simple Graph Theory',
            'Hashing': 'Data Structures',
            'Brute Force': 'Implementation',
            'String Algorithms': 'Simple String Algorithms',
            'Recursion': 'Implementation',
            'Geometry': 'Geometry',
            'BIT': 'Data Structures',
            'Bit manipulation': None,
            'Probability': 'Math',
            'Bitmask': None,
            'BFS': 'Simple Graph Theory',
            'Segment Trees': 'Data Structures',
            'Trees': 'Simple Graph Theory',
            'Matrix Exponentiation': 'Math',
            'Game Theory': 'Game Theory',
            'Disjoint Set': 'Data Structures',
            'Sieve': 'Math',
            'Simple-math': 'Math',
            'HashMap': 'Data Structures',
            'Prime Factorization': 'Math',
            'Priority Queue': 'Data Structures',
            'Modular arithmetic': 'Math',
            'Minimum Spanning Tree': 'Medium Graph Theory',
            'Stack': 'Data Structures',
            'Modular exponentiation': 'Math',
            'Heap': 'Data Structures',
            'Fenwick Tree': 'Data Structures',
            'Sqrt-Decomposition': 'Data Structures',
            'Binary Search Tree': 'Data Structures',
            'Trie': 'Hard String Algorithms',
            'Dijkstra': 'Medium Graph Theory',
            'Simulation': 'Implementation',
            'Divide And Conquer': None,
            'Shortest-path': 'Medium Graph Theory',
            'Two-pointer': 'Geometry',
            'adhoc': 'Implementation',
            'Sailesh Arya': None,
            'Floyd Warshall': 'Medium Graph Theory',
            'Binary Tree': 'Data Structures',
            'Suffix Arrays': 'Hard String Algorithms',
            'Expectation': 'Math',
            'Heavy light decomposition': 'Data Structures',
            'KMP': 'Simple String Algorithms',
            'Matching': 'Hard Graph Theory',
            'Memoization': 'Implementation',
            'Ad-hoc': 'Implementation',
            'Queue': 'Data Structures',
            'cake-walk': 'Implementation',
            'Completed': None,
            'Line-sweep': 'Geometry',
            'Priority-Queue': 'Data Structures',
            'Flow': 'Hard Graph Theory',
            'GCD': 'Math',
            'Data-Structures': 'Data Structures',
            'Kruskal': 'Medium Graph Theory',
            'String-Manipulation': 'Simple String Algorithms',
            'Very Easy': None,
            'Bipartite Graph': 'Hard Graph Theory',
            'Basic-Programming': 'Implementation',
            'Maps': 'Data Structures',
            'Bellman Ford': 'Medium Graph Theory',
            'Set': 'Data Structures',
            'Extended Euclid': 'Math',
            'FFT': 'Math',
            'Easy-medium': None,
            }

REAL_TAGS = [e for e in set(list(map_tags.values())) if e is not None]


def get_all_problem_ids(problems):
    return problems.problem_id.tolist()


def get_levels(problems):
    problem_levels = {}
    for level in problems.level:
        problem_levels.setdefault(level, 0)
        problem_levels[level] += 1
    return problem_levels


def information_about_problem_ids(train_problems, test_problems, all_problems):
    ids = get_all_problem_ids(all_problems)
    print('Number of elements in train_problems =', len(train_problems))
    print('Number of elements in test_problems =', len(test_problems))
    print('Number of elements in both train and test =', len(all_problems))
    print('Number of unique elements in both train and test =', len(set(ids)))
    train_ids = set(get_all_problem_ids(train_problems))
    test_ids = set(get_all_problem_ids(test_problems))
    print('Number of unique elements in test =',
          len(train_ids.difference(test_ids)))
    print('Number of unique elements in train =',
          len(test_ids.difference(train_ids)))
    print('Number of common elements in train and test =',
          len(test_ids.intersection(train_ids)))


def explore_levels(problems):
    real_levels = ('E', 'E-M', 'M', 'M-H', 'H')
    print(problems[problems])
    # for problem in problems[problems['level'] not in real_levels].iterrows():
    #     problems.ix[problem[0], 'level'] = 'E'
    # for level in real_levels:
    #     print('{} ='.format(level),
    #           problems[problems['level'] == level]['solved_count'].mean())


def get_rating(problems):
    return problems.rating.value_counts()


def explore_tags(problems):
    tags = problems.tag1
    tags = tags.append(problems.tag2)
    tags = tags.append(problems.tag3)
    tags = tags.append(problems.tag4)
    tags = tags.append(problems.tag5)
    tags = tags.dropna()
    print(tags.drop_duplicates().tolist())

    # count_tags = {}
    # for value in tags:
    #     count_tags.setdefault(value, 0)
    #     count_tags[value] += 1
    # tags = sorted(count_tags.items(), key=lambda x: x[1], reverse=True)
    # print('{ ', end='')
    # for tag in tags:
    #     print('\'{}\': \'\','.format(tag[0]))
    # print('}')


def show_problems_with_certain_tag(problems, tag):
    expr = 'tag1 == \'{0}\' | tag2 == \'{0}\' | tag3 == \'{0}\' | ' \
           'tag4 == \'{0}\' | tag5 == \'{0}\''.format(tag)
    for index, problem in problems.query(expr).iterrows():
        print(problem.get('tag1'))


if __name__ == '__main__':
    train_problems = pandas.read_csv("../train/problems.csv")
    test_problems = pandas.read_csv("../test/problems.csv")
    all_problems = train_problems.append(test_problems,
                                         ignore_index=True,
                                         verify_integrity=True)
    all_problems = all_problems.drop_duplicates()
    # explore_tags(all_problems)
    # show_problems_with_certain_tag(all_problems, 'Algorithms')
    print(all_problems.solved_count.describe())