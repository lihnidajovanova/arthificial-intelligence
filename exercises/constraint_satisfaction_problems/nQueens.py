from constraint import *


def queens_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or \
            abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False
    return True


if __name__ == '__main__':
    number = int(input())

    if number <= 6:
        problem = Problem(BacktrackingSolver())
    else:
        problem = Problem()

    variables = range(1, number + 1)

    domain = [(i, j) for i in range(number) for j in range(number)]

    problem.addVariables(variables, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for queen1 in variables:
        for queen2 in variables:
            if queen1 < queen2:
                problem.addConstraint(queens_attacking, (queen1, queen2))

    # ----------------------------------------------------

    if number <= 6:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        solution = problem.getSolution()
        print(solution)
