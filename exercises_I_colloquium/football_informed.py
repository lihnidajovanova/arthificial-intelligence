import math
import bisect

"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Врати ја цената на решавачкиот пат кој пристигнува во состојбата
        state2 од состојбата state1 преку акцијата action, претпоставувајќи
        дека цената на патот до состојбата state1 е c. Ако проблемот е таков
        што патот не е важен, оваа функција ќе ја разгледува само состојбата
        state2. Ако патот е важен, ќе ја разгледува цената c и можеби и
        state1 и action. Даденава имплементација му доделува цена 1 на секој
        чекор од патот.
        :param c: цена на патот до состојбата state1
        :param state1: дадена моментална состојба
        :param action: акција која треба да се изврши
        :param state2: состојба во која треба да се стигне
        :return: цена на патот по извршување на акцијата
        :rtype: float
        """
        return c + 1

    def value(self):
        """За проблеми на оптимизација, секоја состојба си има вредност.
        Hill-climbing и сличните алгоритми се обидуваат да ја максимизираат
        оваа вредност.
        :return: вредност на состојба
        :rtype: float
        """
        raise NotImplementedError


"""
Дефинирање на класата за структурата на јазел од пребарување.
Класата Node не се наследува
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Креирај јазол од пребарувачкото дрво, добиен од parent со примена
        на акцијата action
        :param state: моментална состојба (current state)
        :param parent: родителска состојба (parent state)
        :param action: акција (action)
        :param path_cost: цена на патот (path cost)
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """Излистај ги јазлите достапни во еден чекор од овој јазол.
        :param problem: даден проблем
        :return: листа на достапни јазли во еден чекор
        :rtype: list(Node)
        """

        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Дете јазел
        :param problem: даден проблем
        :param action: дадена акција
        :return: достапен јазел според дадената акција
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Врати ја секвенцата од акции за да се стигне од коренот до овој јазол.
        :return: секвенцата од акции
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Врати ја секвенцата од состојби за да се стигне од коренот до овој јазол.
        :return: листа од состојби
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Врати ја листата од јазли што го формираат патот од коренот до овој јазол.
        :return: листа од јазли од патот
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """Сакаме редицата од јазли кај breadth_first_search или 
    astar_search да не содржи состојби - дупликати, па јазлите што
    содржат иста состојба ги третираме како исти. [Проблем: ова може
    да не биде пожелно во други ситуации.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Дефинирање на помошни структури за чување на листата на генерирани, но непроверени јазли
"""


class Queue:
    """Queue е апстрактна класа / интерфејс. Постојат 3 типа:
        Stack(): Last In First Out Queue (стек).
        FIFOQueue(): First In First Out Queue (редица).
        PriorityQueue(order, f): Queue во сортиран редослед (подразбирливо,од најмалиот кон
                                 најголемиот јазол).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Додади го елементот item во редицата
        :param item: даден елемент
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Додади ги елементите items во редицата
        :param items: дадени елементи
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Врати го првиот елемент од редицата
        :return: прв елемент
        """
        raise NotImplementedError

    def __len__(self):
        """Врати го бројот на елементи во редицата
        :return: број на елементи во редицата
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Проверка дали редицата го содржи елементот item
        :param item: даден елемент
        :return: дали queue го содржи item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """Редица во која прво се враќа минималниот (или максималниот) елемент
    (како што е определено со f и order). Оваа структура се користи кај
    информирано пребарување"""
    """"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: функција за подредување, ако order е min, се враќа елементот
                      со минимална f(x); ако order е max, тогаш се враќа елементот
                      со максимална f(x).
        :param f: функција f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


from sys import maxsize as infinity

"""
Информирано пребарување во рамки на граф
"""


def memoize(fn, slot=None):
    """ Запамети ја пресметаната вредност за која била листа од
    аргументи. Ако е специфициран slot, зачувај го резултатот во
    тој slot на првиот аргумент. Ако slot е None, зачувај ги
    резултатите во речник.
    :param fn: зададена функција
    :type fn: function
    :param slot: име на атрибут во кој се чуваат резултатите од функцијата
    :type slot: str
    :return: функција со модификација за зачувување на резултатите
    :rtype: function
    """
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memoized_fn(*args):
            if args not in memoized_fn.cache:
                memoized_fn.cache[args] = fn(*args)
            return memoized_fn.cache[args]

        memoized_fn.cache = {}
    return memoized_fn


def best_first_graph_search(problem, f):
    """Пребарувај низ следбениците на даден проблем за да најдеш цел. Користи
     функција за евалуација за да се одлучи кој е сосед најмногу ветува и
     потоа да се истражи. Ако до дадена состојба стигнат два пата, употреби
     го најдобриот пат.
    :param problem: даден проблем
    :type problem: Problem
    :param f: дадена функција за евалуација (проценка)
    :type f: function
    :return: Node or None
    :rtype: Node
    """
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return None


def greedy_best_first_graph_search(problem, h=None):
    """ Greedy best-first пребарување се остварува ако се специфицира дека f(n) = h(n).
    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)


def astar_search(problem, h=None):
    """ A* пребарување е best-first graph пребарување каде f(n) = g(n) + h(n).
    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


def recursive_best_first_search(problem, h=None):
    """Recursive best first search - ја ограничува рекурзијата
    преку следење на f-вредноста на најдобриот алтернативен пат
    од било кој јазел предок (еден чекор гледање нанапред).
    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0  # (втората вредност е неважна)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, infinity
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            # Подреди ги според најниската f вредност
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = infinity
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, infinity)
    return result


class Goal(Problem):
    def __init__(self, opponents, goal_cor, initial, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents
        self.goal_cor = goal_cor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):

        return self.successor(state)[action]

    def goal_test(self, state):

        return state[1] in self.goal_cor

    def successor(self, state):
        successors = dict()
        man = state[0]
        ball = state[1]

        # Up man
        new_man_x, new_man_y = man_up(man, ball, self.opponents)
        if new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche gore'] = (new_man, ball)

        # Down man
        new_man_x, new_man_y = man_down(man, ball, self.opponents)
        if new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche dolu'] = (new_man, ball)

        # Right man
        new_man_x, new_man_y = man_right(man, ball, self.opponents)
        if new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche desno'] = (new_man, ball)

        # Up-right man
        new_man_x, new_man_y = man_up_right(man, ball, self.opponents)
        if new_man_x != man[0] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche gore-desno'] = (new_man, ball)

        # Down-right man
        new_man_x, new_man_y = man_down_right(man, ball, self.opponents)
        if new_man_x != man[0] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche dolu-desno'] = (new_man, ball)

        # Up ball
        new_man_x, new_man_y, new_ball_x, new_ball_y = ball_up(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore'] = (new_man, new_ball)

        # Down ball
        new_man_x, new_man_y, new_ball_x, new_ball_y = ball_down(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu'] = (new_man, new_ball)

        # Right ball
        new_man_x, new_man_y, new_ball_x, new_ball_y = ball_right(man, ball, self.opponents)
        if new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka desno'] = (new_man, new_ball)

        # Up-right ball
        new_man_x, new_man_y, new_ball_x, new_ball_y = ball_up_right(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1] and new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore-desno'] = (new_man, new_ball)

        # Down-right ball
        new_man_x, new_man_y, new_ball_x, new_ball_y = ball_down_right(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1] and new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu-desno'] = (new_man, new_ball)

        return successors

    def h(self, node):

        return min(
            max(abs(goal_place[1][0] - node.state[1][0]),
                abs(goal_place[1][1] - node.state[1][1])),
            max(abs(goal_place[0][0] - node.state[1][0]),
                abs(goal_place[0][1] - node.state[1][1]))) + (1 if node.state[0][1] == 0 else 0)

        """return min(
            abs(goal_place[0][0] - node.state[1][0]) + abs(
                goal_place[0][1] - node.state[1][1]),
            abs(goal_place[1][0] - node.state[1][0]) + abs(
                goal_place[1][1] - node.state[1][1]))"""

        """return min(max(abs(node.state[1][0] - 7), abs(node.state[1][1] - 2)),
                   max(abs(node.state[1][0] - 7), abs(node.state[1][1] - 3))) + (1 if node.state[0][1] == 0 else 0)"""

        """return min(max(abs(node.state[1][0] - 7), abs(node.state[1][1] - 2)),
                   max(abs(node.state[1][0] - 7), abs(node.state[1][1] - 3)))"""


def man_up(man, ball, opponents):
    new_man = (man[0], man[1] + 1)

    if check_valid(new_man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def ball_up(man, ball, opponents):
    new_man = (man[0], man[1] + 1)
    new_ball = (ball[0], ball[1] + 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def man_down(man, ball, opponents):
    new_man = (man[0], man[1] - 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def ball_down(man, ball, opponents):
    new_man = (man[0], man[1] - 1)
    new_ball = (ball[0], ball[1] - 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def man_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1])

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def ball_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1])
    new_ball = (ball[0] + 1, ball[1])

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def man_up_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1] + 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def ball_up_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1] + 1)
    new_ball = (ball[0] + 1, ball[1] + 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def man_down_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1] - 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def ball_down_right(man, ball, opponents):
    new_man = (man[0] + 1, man[1] - 1)
    new_ball = (ball[0] + 1, ball[1] - 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def check_valid(man, ball, opponents):
    man_pos = man
    ball_pos = ball

    # opponents opp[4] and opp[11]
    return 0 <= man_pos[0] < 8 and \
        0 <= man_pos[1] < 6 and \
        0 <= ball_pos[0] < 8 and \
        0 <= ball_pos[1] < 6 and \
        man_pos != opponents[4] and man_pos != opponents[11] and \
        ball_pos not in opponents and \
        man_pos != ball_pos


"""
def check_validTopka(man, ball, opponents):
    man_pos = man
    ball_pos = (ball[0] - 1, ball[1] - 1)
    return 0 <= man_pos[0] < 8 and \
        0 <= man_pos[1] < 6 and \
        0 <= ball_pos[0] < 8 and \
        0 <= ball_pos[1] < 6 and \
        man_pos not in opponents and \
        ball_pos not in opponents and \
        man_pos == ball_pos
"""

if __name__ == '__main__':
    tmp = input().split(",")
    player = (int(tmp[0]), int(tmp[1]))

    tmp = input().split(",")
    ball_input = (int(tmp[0]), int(tmp[1]))

    opponents_radius = ((2, 2), (3, 2), (4, 2),
                        (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                        (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
                        (4, 5), (5, 5), (6, 5))

    goal_place = ((7, 2), (7, 3))

    g = Goal(opponents_radius, goal_place, (player, ball_input))
    print(astar_search(g).solution())
