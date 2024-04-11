from constraint import *


def read_solver():
    solver = input()
    if solver == "BacktrackingSolver":
        return Problem(BacktrackingSolver())
    elif solver == "RecursiveBacktrackingSolver":
        return Problem(RecursiveBacktrackingSolver())
    elif solver == "MinConflictsSolver":
        return Problem(MinConflictsSolver())


if __name__ == '__main__':
    # problem = Problem(BacktrackingSolver())
    # variables = []
    # for variable in variables:
    #   problem.addVariable(variable, Domain(set(range(100))))

    problem = read_solver()

    variables = range(0, 81)
    domain = range(1, 10)

    problem.addVariables(variables, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # all different in row
    for row in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), [(row * 9 + num) for num in range(0, 9)])

    # all different in column
    for col in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), [(num * 9 + col) for num in range(0, 9)])

    # all different in block
    for w in range(0, 9, 3):
        for h in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(),
                                  [((y * 9) + x) for x in range(h, h + 3) for y in range(w, w + 3)])
    # ----------------------------------------------------

    print(problem.getSolution())
