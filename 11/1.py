import copy
from collections import deque
from sortedcontainers import SortedSet


class State:
    def __init__(self, state, position):
        self.state = state
        self.position = position
        self.distance_from_root = int(1e10)
        self.distance_through_state = int(1e10)

        if not self.is_valid():
            raise Exception

    def __eq__(self, other):
        if other is None:
            return False

        return (self.state == other.state and self.position == other.position) or self.equivalent(other)

    def __hash__(self):
        return hash(self.__repr__())

    def __str__(self):
        return "Position: {0}, state: {1}".format(self.position, " ".join("{0} : {1}".format(x, str(sorted(self.state[x]))) for x in self.state))

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def from_state(cls, state):
        return cls(copy.deepcopy(state.state), state.position)

    def generate_possible_states(self):
        result = set([])

        for v1 in self.state[self.position]:
            for v2 in self.state[self.position]:
                result.add(self.move_values(max(1, self.position - 1), set([v1, v2])))
                result.add(self.move_values(min(4, self.position + 1), set([v1, v2])))

        return [r for r in result if State.validate_state(r) if r != self]

    def move_values(self, to_index, values):
        result = State.from_state(self)

        for v in values:
            result.state[result.position].remove(v)
            result.state[to_index].add(v)

        result.position = to_index

        return result

    def is_valid(self):
        return State.validate_state(self)

    def validate_state(state):
        values = state.state[state.position]
        generators = [x for x in values if x[1] == 0]

        for g in generators:
            for m in [x for x in values if x[0] != g[0] and x[1] == 1]:
                if not [x for x in generators if x[0] == m[0]]:
                    return False

        return True

    def is_final_state(self):
        return (not self.state[1]) and (not self.state[2]) and (not self.state[3])

    def find_value(self, value):
        for i in range(1, 5):
            if value in self.state[i]:
                return i

    def distance(self, state):
        distance = 0

        for i in range(1, 5):
            for v in self.state[i]:
                distance += abs(i - state.find_value(v))

        return distance

    def equivalent(self, state):
        if self.position != state.position:
            return False

        position_dict1 = {}
        position_dict2 = {}

        for i in range(1, 5):
            for v in self.state[i]:
                position_dict1[v] = i

        for i in range(1, 5):
            for v in state.state[i]:
                position_dict2[v] = i

        for k in list(position_dict1.keys()):
            if position_dict1[k] == position_dict2[k]:
                position_dict1.pop(k)
                position_dict2.pop(k)

        keys = list(position_dict1.keys())

        for k1 in keys:
            for k2 in [k for k in keys if k > k1]:
                if position_dict1[k1] == position_dict2[k2] and position_dict1[k2] == position_dict2[k1]:
                    position_dict1.pop(k1)
                    position_dict2.pop(k1)
                    position_dict1.pop(k2)
                    position_dict2.pop(k2)

        if position_dict1:
            return False
        else:
            return True


def walk_state_tree_dfs(inital_state):
    visited = set([])
    stack = []
    stack.append(inital_state)

    while stack:
        state = stack.pop()
        if state not in visited:
            visited.add(state)
            for s in state.generate_possible_states():
                print(s)

                if s.is_final_state():
                    return

                stack.append(s)
    return visited


def walk_state_tree_bfs(inital_state):
    queue = deque([])
    inital_state.distance_from_root = 0
    queue.append(inital_state)
    came_from = {}

    while queue:
        state = queue.popleft()

        for s in state.generate_possible_states():
            if s.distance_from_root == int(1e10):
                print(s)
                s.distance_from_root = state.distance_from_root + 1
                queue.append(s)
                came_from[s] = state
                if s.is_final_state():
                    #print(s)
                    return get_path_length(came_from, s)


def walk_state_tree_a_star(state, end):
    visited = set([])
    unvistied = set([state])
    came_from = {}

    g_score = SortedSet([], key=lambda x: -x.distance_from_root)
    state.distance_from_root = 0
    g_score.add(state)
    f_score = SortedSet([], key=lambda x: -x.distance_through_state)
    state.distance_through_state = state.distance(end)
    f_score.add(state)

    while unvistied:
        current = f_score.pop()

        if current == end:
            return get_path_length(came_from, current)

        unvistied.remove(current)
        visited.add(current)

        for s in current.generate_possible_states():
            if s in visited:
                continue

            temp_score = current.distance_from_root + current.distance(s)

            if s not in unvistied:
                unvistied.add(s)
            elif temp_score > s.distance_from_root:
                continue

            came_from[s] = current
            s.distance_from_root = temp_score
            s.distance_through_state = s.distance_from_root + s.distance(end)
            f_score.add(s)
            g_score.add(s)


def get_path_length(came_from, state):
    path = [state]

    while state in came_from:
        state = came_from[state]
        path.append(state)

    return path


state = {
    1: set([(0, 0), (1, 0), (1, 1), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1)]),
    2: set([(0, 1), (2, 1)]),
    3: set([]),
    4: set([])
}

equiv_state = {
    1: set([(3, 0), (1, 0), (1, 1), (2, 0), (0, 0), (0, 1), (4, 0), (4, 1)]),
    2: set([(3, 1), (2, 1)]),
    3: set([]),
    4: set([])
}

#state = {
    #1: set([(3, 1)]),
    #2: set([(0, 1)]),
    #3: set([]),
    #4: set([])
#}

#state = {
    #1: set([(0, 1)]),
    #2: set([(3, 1)]),
    #3: set([]),
    #4: set([])
#}

end_state = {
    1: set([]),
    2: set([]),
    3: set([]),
    4: set([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)])
}

test_state = {
    1: set([(0, 1), (1, 1)]),
    2: set([(0, 0)]),
    3: set([(1, 0)]),
    4: set([])
}

test_end_state = {
    1: set([]),
    2: set([]),
    3: set([]),
    4: set([(0, 0), (0, 1), (1, 0), (1, 1)])
}

#s = State(state, 1)
#e = State(end_state, 4)
#eq = State(equiv_state, 1)
#print(s.equivalent(eq))

s = State(test_state, 1)
e = State(test_end_state, 4)
#print(s.generate_possible_states())
#print(e)
#path = walk_state_tree_a_star(s, e)
path = walk_state_tree_bfs(s)

#for state in reversed(path):
    #print(state)

#print(len(path) - 1)
