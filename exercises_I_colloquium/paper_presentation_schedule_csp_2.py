from constraint import *


# var    #domain     #dic
def max_4_constraint(*paper_domains):
    check_my_dic = {}
    # print(paper_domains)

    # only 4 in one time_slot
    for time_slot in paper_domains:
        if time_slot not in check_my_dic.keys():
            check_my_dic[time_slot] = 1
        else:
            check_my_dic[time_slot] = check_my_dic.get(time_slot) + 1
    for value in check_my_dic.values():
        if value > 4:
            return False

    return True


def same_time_slot(*paper_domains):
    return len(set(paper_domains)) == 1


if __name__ == "__main__":
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != "end":
        title, topic = paper_info.split(" ")
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [var + f" ({papers[var]})" for var in papers.keys()]
    # print(variables)

    domain = [f"T{i + 1}" for i in range(num)]
    # print(domain)

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max_4_constraint, tuple(variables))
    areas = tuple(set(papers.values()))
    # print(areas)
    for area in areas:
        l1 = []
        for var in variables:
            if area in var:
                l1.append(var)
        # print(l1)
        if len(l1) <= 4:
            problem.addConstraint(same_time_slot, l1)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for v in variables:
        print(v + ": " + result[v])
