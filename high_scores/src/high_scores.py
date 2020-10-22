def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores)[-1]


def personal_top_three(scores):
    return sorted(scores)[-3:]


def scores_highest_to_lowest(scores):
    return sorted(scores, reverse=True)
