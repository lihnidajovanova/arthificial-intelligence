# from searching_framework import # what do you need to solve this problem?
from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, initial, goal, red_apples):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def check_valid(self, snake_head, snake_body):
        # check if snake ate a red apple
        if snake_head in self.red_apples:
            return False
        # check collision with itself
        if snake_head in snake_body:
            return False
        # check if snake is outside the table
        if 0 > snake_head[0] or snake_head[0] > 9 or 0 > snake_head[1] or snake_head[1] > 9:
            return False
        return True

    def move(self, direction, snake, snake_head, green_apples):
        temp = snake[0]
        new_snake = [snake_head]
        for part in snake[1:]:
            new_snake.append(temp)
            temp = part
        if snake_head in green_apples:
            new_snake.append(temp)
            return (direction, tuple(new_snake)), tuple([apple for apple in green_apples if apple != snake_head])
        return (direction, tuple(new_snake)), green_apples

    def successor(self, state):
        direction, snake, green_apples = state[0][0], state[0][1], state[1]

        successors = dict()

        # 1 = facing north
        if direction == 1:
            # continue straight
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, green_apples)
                successors['ProdolzhiPravo'] = new_state
            # turn right
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(2, snake, snake_head, green_apples)
                successors['SvrtiDesno'] = new_state
            # turn left
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(4, snake, snake_head, green_apples)
                successors['SvrtiLevo'] = new_state

        # 2 = facing east
        elif direction == 2:
            # continue straight
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, green_apples)
                successors['ProdolzhiPravo'] = new_state
            # turn right
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(3, snake, snake_head, green_apples)
                successors['SvrtiDesno'] = new_state
            # turn left
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(1, snake, snake_head, green_apples)
                successors['SvrtiLevo'] = new_state

        # 3 = facing south
        elif direction == 3:
            # continue straight
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, green_apples)
                successors['ProdolzhiPravo'] = new_state
            # turn right
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(4, snake, snake_head, green_apples)
                successors['SvrtiDesno'] = new_state
            # turn left
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(2, snake, snake_head, green_apples)
                successors['SvrtiLevo'] = new_state

        # 4 = facing west
        else:
            # continue straight
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, green_apples)
                successors['ProdolzhiPravo'] = new_state
            # turn right
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(1, snake, snake_head, green_apples)
                successors['SvrtiDesno'] = new_state
            # turn left
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(3, snake, snake_head, green_apples)
                successors['SvrtiLevo'] = new_state

        return successors

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())  # number of green apples
    green_apples = [tuple(map(int, input().split(","))) for _ in range(n)]

    m = int(input())  # number of red apples
    red_apples = [tuple(map(int, input().split(","))) for _ in range(m)]

    direction = 3  # initial direction towards south
    snake = (0, 7), (0, 8), (0, 9)  # initial snake location

    condition = ((direction, snake), tuple(green_apples))  # initial state

    snake_problem = Snake(condition, None, red_apples)

    answer = breadth_first_graph_search(snake_problem)

    print(answer.solution())
