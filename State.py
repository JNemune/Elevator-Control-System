from __future__ import annotations

from itertools import product
from typing import Generator, Literal
from copy import deepcopy


class State:
    def __init__(
        self, floors: int, elv_num: int, main_state=None, elv_locs=None
    ) -> None:
        self.floors = floors
        self.elv_num = elv_num
        if main_state is None and elv_locs is None:
            self.main_state = {}
            self.elv_locs = [0 for _ in range(elv_num)]
        else:
            self.main_state = main_state
            self.elv_locs = elv_locs

    def add_floor(self, floor):
        self.main_state.setdefault(floor, 0)

    def doit(self, actions: list[Literal["UP", "DOWN", "STOP"]]) -> None:
        for floor in self.main_state:
            self.main_state[floor] += 1
        for elv_num, action in enumerate(actions):
            if action == "UP":
                self.elv_locs[elv_num] += 1
            elif action == "DOWN":
                self.elv_locs[elv_num] -= 1
            elif action == "STOP":
                if self.elv_locs[elv_num] in self.main_state:
                    del self.main_state[self.elv_locs[elv_num]]

    def transition(self, actions: list[Literal["UP", "DOWN", "STOP"]]) -> State:
        new = State(
            self.floors,
            self.elv_num,
            deepcopy(self.main_state),
            deepcopy(self.elv_locs),
        )
        new.doit(actions)
        return new

    def cost(self) -> int:
        cost = sum(self.main_state.values())
        for floor in self.main_state.keys():
            cost += min([abs(floor - elv) for elv in self.elv_locs])
        return cost

    def actions(self) -> Generator[list[Literal["UP", "DOWN", "STOP"]]]:
        possible_actions = []
        for elv_loc in self.elv_locs:
            if elv_loc == 0:
                possible_actions.append(["UP", "STOP"])
            elif elv_loc == self.floors:
                possible_actions.append(["DOWN", "STOP"])
            else:
                possible_actions.append(["UP", "DOWN", "STOP"])
        return product(*possible_actions)

    def decision(self) -> None:
        cost_dict = {}
        for action in self.actions():
            cost_dict[tuple(action)] = self.transition(action).cost()
        decision = list(cost_dict.items())
        decision.sort(key=lambda x: x[0].count("STOP"), reverse=True)
        decision.sort(key=lambda x: x[1])
        self.doit(decision[0][0])
