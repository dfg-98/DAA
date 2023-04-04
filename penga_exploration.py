from math import ceil, floor


class State:
    def __init__(self, columns, cost, action=None, parent=None) -> None:
        self.columns = columns
        self.action = action
        self.cost = cost
        self.h_max = self.columns[0]
        self.h_min = self.columns[0]
        self.h_max_index = 0
        self.h_min_index = 0

        self.parent = parent
        for i, h in enumerate(self.columns):
            if h > self.h_max:
                self.h_max = h
                self.h_max_index = i
            if h < self.h_min:
                self.h_min = h
                self.h_min_index = i

    def new_state(self, action, C, E, M):
        new_state = list(self.columns)
        assert action is not None

        if action[0] == "C":
            new_state[action[1]] += 1
            cost = self.cost + C

        elif action[0] == "E":
            new_state[action[1]] -= 1
            cost = self.cost + E

        else:  # M
            s = action[1]
            d = action[2]
            new_state[s] -= 1
            new_state[d] += 1
            cost = self.cost + M
        return self.__class__(tuple(new_state), cost, action, parent=self)

    def valid(self):
        return self.h_max == self.h_min

    def get_actions(self):
        raise NotImplemented

    def __str__(self) -> str:
        prefix = ""
        if self.action:
            prefix = self.action[0]
        return prefix + f"{self.columns} | {self.cost}"

    def __repr__(self) -> str:
        return str(self)

    def traverse(self):
        current = self
        while current:
            yield current
            current = current.parent


class BruteForceState(State):
    def get_actions(self):
        actions = []

        for i in range(len(self.columns)):
            if self.columns[i] < self.h_max:
                action = ("C", i)
                new_state = self.new_state(action, 0, 0, 0)
                for state in self.traverse():
                    if state.columns == new_state.columns:
                        break
                else:
                    actions.append(action)
            if self.columns[i] > self.h_min:
                action = ("E", i)
                new_state = self.new_state(action, 0, 0, 0)
                for state in self.traverse():
                    if state.columns == new_state.columns:
                        break
                else:
                    actions.append(action)
            for j in range(len(self.columns)):
                if i != j and self.columns[i] > self.columns[j]:
                    action = ("M", i, j)
                    new_state = self.new_state(action, 0, 0, 0)
                    for state in self.traverse():
                        if state.columns == new_state.columns:
                            break
                    else:
                        actions.append(action)

        return actions


class SmarterState(State):
    def get_actions(self):
        actions = []
        # C Aumentar el mínimo
        c_i = self.h_min_index
        actions.append(("C", c_i))

        # E eliminar del máximo
        e_i = self.h_max_index
        actions.append(("E", e_i))

        # M mover maximo a minimo
        if self.columns[e_i] > (self.columns[c_i] + 1):
            actions.append(("M", e_i, c_i))

        return actions


def penga(n, C, E, M, state_class=BruteForceState):
    assert isinstance(n, tuple)

    state_class
    n = sorted(n)
    root = state_class(n, 0)
    current_states = [root]
    h_max = max(n)
    h_min = min(n)
    total_initial = sum(n)
    l_n = len(n)
    mean_h_f = floor(total_initial / l_n)
    mean_h_c = ceil(total_initial / l_n)
    e_mean = total_initial - mean_h_f * l_n
    c_mean = mean_h_c * l_n - total_initial

    if e_mean * E < c_mean * C:
        m = sum(i - mean_h_f for i in n if i > mean_h_f)
    else:
        m = sum(i - mean_h_c for i in n if i > mean_h_c)

    E_cost = E * (total_initial - l_n * h_min)
    C_cost = C * (h_max * l_n - total_initial)
    M_cost = m * M + min(e_mean * E, c_mean * C)
    min_cost = min(E_cost, C_cost, M_cost)
    final_states = []

    states = {tuple(root.columns): root.cost}

    while len(current_states):
        state = current_states.pop()

        if state.cost > min_cost:
            continue

        if state.valid():
            if state.cost <= min_cost:
                min_cost = state.cost
            final_states.append(state)

        else:
            actions = state.get_actions()
            for action in actions:
                new_state = state.new_state(action, C, E, M)

                saved_state_cost = states.get(new_state.columns, None)
                if saved_state_cost is None:
                    states[new_state.columns] = new_state.cost
                else:
                    if new_state.cost < saved_state_cost:
                        states[new_state.columns] = new_state.cost
                    else:
                        continue

                if new_state.cost > min_cost:
                    continue
                current_states.append(new_state)

    return min_cost, final_states


def get_path(state):
    current = state
    states = []
    while current.parent != None:
        states.append(current)
        current = current.parent
    states.append(current)
    return reversed(states)


def penga_brute_force(n, C, E, M):
    return penga(n, C, E, M, BruteForceState)


def jenga_smarter(n, C, E, M):
    return penga(n, C, E, M, SmarterState)
