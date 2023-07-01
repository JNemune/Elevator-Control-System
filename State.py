from __future__ import annotations

from itertools import product
from typing import Literal


class State:
    def __init__(
        self, main_state: dict[int, int], elv_locs: list[int], floors: int
    ) -> None:
        self.main_state = main_state
        self.elv_locs = elv_locs
        self.floors = floors

    def doit(self, actions: list[Literal["UP", "DOWN", "STOP"]]) -> None:
        for elv_num, action in enumerate(actions):
            if action == "UP":
                self.elv_locs[elv_num] += 1
            elif action == "DOWN":
                self.elv_locs[elv_num] -= 1
            elif action == "STOP":
                if self.elv_locs[elv_num] in self.main_state:
                    del self.main_state[self.elv_locs[elv_num]]

    def transition(self, actions: list[Literal["UP", "DOWN", "STOP"]]) -> State:
        new = State(self.main_state, self.elv_locs)
        new.doit(actions)
        return new

    def cost(self) -> int:
        cost = sum(self.main_state.values())
        for floor in self.main_state.keys():
            cost += min([abs(floor - elv) for elv in self.elv_locs])
        return cost

    def actions(self) -> list[list[Literal["UP", "DOWN", "STOP"]]]:
        possible_actions = []
        for elv_loc in self.elv_locs:
            if elv_loc == 0:
                possible_actions.append(["UP", "STOP"])
            elif elv_loc == self.floors:
                possible_actions.append(["DOWN", "STOP"])
            else:
                possible_actions.append(["UP", "DOWN", "STOP"])
        return list(product(*possible_actions))
