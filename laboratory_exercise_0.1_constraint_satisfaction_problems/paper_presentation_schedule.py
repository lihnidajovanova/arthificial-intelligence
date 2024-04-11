from constraint import *


def fourPerTerm(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    firstTerm = 0
    secondTerm = 0
    thirdTerm = 0
    fourthTerm = 0

    temp = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

    for x in temp:
        if x == "T1":
            firstTerm += 1
        if x == "T2":
            secondTerm += 1
        if x == "T3":
            thirdTerm += 1
        if x == "T4":
            fourthTerm += 1

    return firstTerm <= 4 and secondTerm <= 4 and thirdTerm <= 4 and fourthTerm <= 4


if __name__ == '__main__':
    num = int(input())

    # papers = dict()
    ai = []
    ml = []
    nlp = []

    paper_info = input()
    variables = []

    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        # papers[title] = topic
        variables.append(title + ' (' + topic + ')')

        if topic == "AI":
            ai.append(title + ' (' + topic + ')')
        if topic == "ML":
            ml.append(title + ' (' + topic + ')')
        if topic == "NLP":
            nlp.append(title + ' (' + topic + ')')

        paper_info = input()

    # Tuka definirajte gi promenlivite
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    if len(ai) <= 4 and len(ai) != 0:
        problem.addConstraint(AllEqualConstraint(), ai)
    if len(ml) <= 4 and len(ml) != 0:
        problem.addConstraint(AllEqualConstraint(), ml)
    if len(nlp) <= 4 and len(nlp) != 0:
        problem.addConstraint(AllEqualConstraint(), nlp)

    problem.addConstraint(fourPerTerm, variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    names = sorted(result)
    values = []
    for x in names:
        values.append(result[x])

    print(f"{names[0]}: {values[0]}")
    for i in range(2, len(names)):
        print(f"{names[i]}: {values[i]}")
    print(f"{names[1]}: {values[1]}")
