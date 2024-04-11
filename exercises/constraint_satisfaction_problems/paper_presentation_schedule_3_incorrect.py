from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    # title = ID, topic = oblast
    # keys = paper titles
    variables = list(papers.keys())

    # domain = [f'T{i + 1}' for i in range(num)]
    domain = {}
    for topic in set(papers.values()):
        papers_topic = [paper for paper in papers.keys() if papers[paper] == topic]
        domain[topic] = [f"T{i + 1}" for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    # problem.addVariables(variables, domain)
    for var in variables:
        problem.addVariable(var, domain[papers[var]])

    # Tuka dodadete gi ogranichuvanjata
    # values = paper topic->trudovi
    for topic in set(papers.values()):
        papers_topic = [paper for paper in papers.keys() if papers[paper] == topic]
        if len(papers_topic) <= num:
            problem.addConstraint(AllEqualConstraint(), papers_topic)
        else:
            problem.addConstraint(SomeInSetConstraint(domain[topic]), papers_topic)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    ...
    for paper, topic in papers.items():
        print(f"{paper} ({topic}): {result[paper]}")
