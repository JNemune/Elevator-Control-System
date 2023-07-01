from typing import Literal


class Decision:
    def __init__(self) -> None:
        self.main_struct = {}
        self.current_floor = 0

    def next_move(self) -> Literal["UP", "DOWN", "STOP"] | None:
        if self.current_floor in self.main_struct:
            del self.main_struct[self.current_floor]
            return "STOP"
        for floor in self.main_struct:
            self.main_struct[floor] += 1
        if not self.main_struct:
            return

        cb_dict = {}
        for floor, time in self.main_struct.items():
            cb_dict[floor] = time - abs(floor - self.current_floor)
        dist_floor = max(list(cb_dict.items()), key=lambda x: x[1])[0]

        if dist_floor > self.current_floor:
            self.current_floor += 1
            return "UP"
        if dist_floor < self.current_floor:
            self.current_floor -= 1
            return "DOWN"

    def add_customer(self, floor) -> None:
        self.main_struct.setdefault(floor, 0)


if __name__ == "__main__":
    decision = Decision()
    decision.add_customer(4)
    decision.add_customer(5)
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    decision.add_customer(6)
    print(decision.next_move())
    decision.add_customer(4)
    print(decision.next_move())
    decision.add_customer(8)
    decision.add_customer(3)
    decision.add_customer(2)
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
    print(decision.next_move())
