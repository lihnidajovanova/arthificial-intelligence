from constraint import *

if __name__ == "__main__":
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # Simona has to participate
    problem.addConstraint(InSetConstraint({1}), ["Simona_prisustvo"])

    # constraint for Simona's free terms
    simona_terms = list(range(13, 15)) + list(range(16, 17)) + list(range(19, 20))
    problem.addConstraint(lambda participant, time: participant == 1 and time in simona_terms,
                          ["Simona_prisustvo", "vreme_sostanok"])

    # constraint for participating either Marija or Petar
    problem.addConstraint(MaxSumConstraint(1), ["Marija_prisustvo", "Petar_prisustvo"])
    problem.addConstraint(lambda marija, petar: marija == 1 or petar == 1,
                          ["Marija_prisustvo", "Petar_prisustvo"])

    # constraint for Marija's free terms
    marija_terms = list(range(14, 16)) + list(range(18, 19))
    problem.addConstraint(lambda participant,
                                 time: participant == 1 if time in marija_terms and time in simona_terms else participant == 0,
                          ["Marija_prisustvo", "vreme_sostanok"])

    # constraint for Petar's free terms
    petar_terms = list(range(12, 14)) + list(range(16, 20))
    problem.addConstraint(lambda participant,
                                 time: participant == 1 if time in petar_terms and time in simona_terms else participant == 0,
                          ["Petar_prisustvo", "vreme_sostanok"])

    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]

    solutions = problem.getSolutions()

    for solution in solutions:
        print({'Simona_prisustvo': solution['Simona_prisustvo'],
               'Marija_prisustvo': solution['Marija_prisustvo'],
               'Petar_prisustvo': solution['Petar_prisustvo'],
               'vreme_sostanok': solution['vreme_sostanok']})
