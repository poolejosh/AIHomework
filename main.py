from queue import PriorityQueue, SimpleQueue
import math


class State:
    def __init__(self, id, parent_id, board_vector, priority, gn=0, hn=0):
        self.id = id
        self.parent_id = parent_id
        self.board_vector = board_vector
        self.priority = priority
        self.gn = gn
        self.hn = hn
        self.fn = gn + hn

    def children(self):  # find child states
        children_boards = []

        zero_index = self.board_vector.index(0)
        if zero_index > 2:  # not top row so there must be a value above
            value_above = self.board_vector[zero_index - 3]
            child_board = self.board_vector[:]
            child_board[zero_index] = value_above
            child_board[zero_index - 3] = 0
            children_boards.append(child_board)

        if zero_index < 15:  # not bottom row so there must be a value below
            value_below = self.board_vector[zero_index + 3]
            child_board = self.board_vector[:]
            child_board[zero_index] = value_below
            child_board[zero_index + 3] = 0
            children_boards.append(child_board)

        if zero_index % 3 != 0:  # not left column so there must be a value to the left
            value_left = self.board_vector[zero_index - 1]
            child_board = self.board_vector[:]
            child_board[zero_index] = value_left
            child_board[zero_index - 1] = 0
            children_boards.append(child_board)

        if (zero_index - 2) % 3 != 0: # not right column so there must be a value to the right
            value_right = self.board_vector[zero_index + 1]
            child_board = self.board_vector[:]
            child_board[zero_index] = value_right
            child_board[zero_index + 1] = 0
            children_boards.append(child_board)

        return children_boards

    def print(self):  # Pretty print board
        count = 0
        for i in self.board_vector:
            print('\t' + str(i) + '\t', end='')
            count += 1
            if count == 3:
                print()
                count = 0

    def __eq__(self, other):  # for not allowing duplicate board states
        if isinstance(other, State):
            return self.board_vector == other.board_vector
        return False


def bfs(open_list, closed_list, goal_vector):
    open_list_count = 1
    id_counter = 0

    current_state = open_list.get()[1]  # grab first element from open list (start state)
    level_priority = 0
    old_level = level_priority

    while current_state.board_vector != goal_vector:  # end when state being evaluated is the goal state
        if len(closed_list) > 10000:
            print('Over 10,000 nodes evaluated without finding the solution')
            print('Process has been terminated')
            return

        children = current_state.children()

        # calculate priority value for new level, or continue with old
        new_level = (math.floor(current_state.priority / 1000) + 1) * 1000
        if old_level > new_level:
            level_priority = old_level
        else:
            level_priority = new_level

        for child in children:  # find children of current state and add to open list
            id_counter += 1
            child_state = State(id_counter, current_state.id, child, level_priority)
            if child_state in closed_list:
                id_counter -= 1  # if board vector already present in closed list, skip child
            else:
                open_list.put((level_priority, child_state))
                level_priority += 1
                old_level = level_priority
                open_list_count += 1

        closed_list.append(current_state)  # put current state in closed list when done evaluating
        current_state = open_list.get()[1]  # get new current state

    closed_list.append(current_state)  # put goal state in the closed list to complete

    print('Nodes added to the Open List: %d' % open_list_count)
    print('Nodes added to the Closed List: %d' % len(closed_list))

    bfs_print_path(closed_list, current_state.id)


def bfs_print_path(closed_list, parent_id):
    for state in closed_list:
        if state.id == parent_id:
            bfs_print_path(closed_list, state.parent_id)

            print('State ID: %d' % state.id)
            print('Level Num: %d' % math.floor(state.priority / 1000))
            state.print()
            print()


def find_solution(start_vector, goal_vector):
    # initialize data structures for holding lists
    open_list = PriorityQueue()
    closed_list = []

    # initialize start state and add to open list
    init_level = 0
    start_state = State(init_level, -1, start_vector, init_level)
    open_list.put((init_level, start_state))

    print('Start vector: %s' % start_vector)
    print('Goal vector: %s' % goal_vector)

    bfs(open_list, closed_list, goal_vector)


if __name__ == '__main__':
    find_solution([1, 13, 3, 5, 6, 9, 11, 0, 8, 12, 14, 10, 7, 16, 15, 4, 17, 2],  # i
                  [1, 13, 3, 5, 6, 9, 11, 14, 8, 12, 16, 10, 7, 17, 15, 0, 4, 2])

    find_solution([1, 13, 3, 5, 17, 9, 11, 0, 8, 12, 14, 10, 7, 16, 15, 4, 6, 2],  # ii
                  [5, 1, 3, 13, 17, 9, 11, 0, 8, 12, 14, 10, 7, 16, 15, 4, 6, 2])

    find_solution([5, 15, 7, 8, 9, 11, 10, 3, 12, 0, 2, 13, 4, 14, 1, 6, 16, 17],  # to test for process timeout
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 17, 16])
