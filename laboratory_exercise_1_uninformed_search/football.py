# from searching_framework import # what do you need to solve this problem?
from searching_framework import Problem, breadth_first_graph_search


class Football(Problem):
    def __init__(self, initial, opponents, goal=None):
        super().__init__(initial, goal)
        self.grid_size_x = 8
        self.grid_size_y = 6
        self.opponents = opponents

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ball_x = state[1][0]
        ball_y = state[1][1]
        return ball_x == 7 and ball_y in (2, 3)

    @staticmethod
    def check_valid(state, opponents):
        man_pos = state[0]
        ball_pos = state[1]

        check_opponents = True

        for opponent in opponents:
            if abs(opponent[0] - ball_pos[0]) <= 1 and abs(opponent[1] - ball_pos[1]) <= 1:
                check_opponents = False

        return man_pos[0] >= 0 and man_pos[0] < 8 and \
            man_pos[1] >= 0 and man_pos[1] < 6 and \
            ball_pos[0] >= 0 and ball_pos[0] < 8 and \
            ball_pos[1] >= 0 and ball_pos[1] < 6 and \
            ball_pos != man_pos and check_opponents and man_pos not in opponents

    def successor(self, state):
        successors = dict()

        man = state[0]
        ball = state[1]

        # Move Up
        man_new = (man[0], man[1] + 1)
        if man_new == ball:
            ball_new = (ball[0], ball[1] + 1)
        else:
            ball_new = ball
        new_state = (man_new, ball_new)
        if self.check_valid(new_state, self.opponents):
            if ball_new != ball:
                successors["Turni topka gore"] = new_state
            else:
                successors["Pomesti coveche gore"] = new_state

        # Move Down
        man_new = (man[0], man[1] - 1)
        if man_new == ball:
            ball_new = (ball[0], ball[1] - 1)
        else:
            ball_new = ball
        new_state = (man_new, ball_new)
        if self.check_valid(new_state, self.opponents):
            if ball_new != ball:
                successors["Turni topka dolu"] = new_state
            else:
                successors["Pomesti coveche dolu"] = new_state

        # Move Right
        man_new = (man[0] + 1, man[1])
        if man_new == ball:
            ball_new = (ball[0] + 1, ball[1])
        else:
            ball_new = ball
        new_state = (man_new, ball_new)
        if self.check_valid(new_state, self.opponents):
            if ball_new != ball:
                successors["Turni topka desno"] = new_state
            else:
                successors["Pomesti coveche desno"] = new_state

        # Move Up-Right
        man_new = (man[0] + 1, man[1] + 1)
        if man_new == ball:
            ball_new = (ball[0] + 1, ball[1] + 1)
        else:
            ball_new = ball
        new_state = (man_new, ball_new)
        if self.check_valid(new_state, self.opponents):
            if ball_new != ball:
                successors["Turni topka gore-desno"] = new_state
            else:
                successors["Pomesti coveche gore-desno"] = new_state

        # Move Down-Right
        man_new = (man[0] + 1, man[1] - 1)
        if man_new == ball:
            ball_new = (ball[0] + 1, ball[1] - 1)
        else:
            ball_new = ball
        new_state = (man_new, ball_new)
        if self.check_valid(new_state, self.opponents):
            if ball_new != ball:
                successors["Turni topka dolu-desno"] = new_state
            else:
                successors["Pomesti coveche dolu-desno"] = new_state

        return successors


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))

    opponents = [(3, 3), (5, 4)]

    football = Football((man_pos, ball_pos), opponents, ((7, 2), (7, 3)))

    result = breadth_first_graph_search(football)
    print(result.solution())
