from constraint import *


def constraint(s, e, n, d, m, o, r, y):
    send = (((s * 10 + e) * 10 + n) * 10 + d)
    more = (((m * 10 + o) * 10 + r) * 10 + e)
    money = ((((m * 10 + o) * 10 + n) * 10 + e) * 10 + y)
    return send + more == money


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]

    problem.addVariables(tuple(variables), range(10))
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(constraint, variables)

    print(problem.getSolution())
