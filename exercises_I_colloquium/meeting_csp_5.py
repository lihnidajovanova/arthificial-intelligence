from constraint import *


def free_time(marija, simona, petar, time):
    simona_free = (13, 14, 16, 19)
    marija_free = (14, 15, 18)
    petar_free = (12, 13, 16, 17, 18, 19)

    if simona == 1 and time in simona_free:
        if marija == 1 and time in marija_free:
            if petar == 1 and time in petar_free:
                return True
            elif petar == 0:
                return True
        else:
            if petar == 1 and time in petar_free:
                if marija == 0:
                    return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = [i for i in range(12, 21)]

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1, ])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", domain)

    variables = ["Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"]
    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(free_time, variables)
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
