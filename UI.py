from tkinter import *

from State import State
from functools import partial


class UI:
    def __init__(self):
        self.MAX_FLR = 14
        self.MAX_ELV = 5
        self.WIDTH = 75
        self.HEIGHT = 50
        self.WIDTH_FLR = 10
        self.CST_R = 5
        self.WIDTH_E = 4
        self.HEIGHT_E = 3

        self.pre_root = Tk()
        self.pre_root.title("شبیه‌ساز آسانسور")

        self.root = Frame(self.pre_root)
        self.root.pack()

        self.configs()

        self.pre_root.mainloop()

    def draw(self, canvas: Canvas):
        def return_butt():
            canvas.destroy()
            self.configs()

        def next_step():
            self.state.decision()
            canvas.destroy()
            self.main()

        def add_cst(floor):
            self.state.add_floor(floor)
            canvas.destroy()
            self.main()

        for i in range(1, self.flr + 1):
            Button(
                canvas,
                text=self.flr - i,
                command=partial(add_cst, self.flr - i),
                bg="light green",
            ).place(x=self.WIDTH * (self.elv + 1), y=i * self.HEIGHT - self.HEIGHT // 5)
        for i in range(1, self.elv + 1):
            canvas.create_line(
                i * self.WIDTH, self.HEIGHT, i * self.WIDTH, self.HEIGHT * self.flr
            )
            for j in range(1, self.flr + 1):
                canvas.create_line(
                    i * self.WIDTH - self.WIDTH // self.WIDTH_FLR,
                    j * self.HEIGHT,
                    i * self.WIDTH + self.WIDTH // self.WIDTH_FLR,
                    j * self.HEIGHT,
                )
        for i_, i in enumerate(self.state.elv_locs):
            canvas.create_rectangle(
                self.WIDTH * (i_ + 1) - self.WIDTH // self.WIDTH_E,
                self.HEIGHT * (self.flr - i) - self.HEIGHT // self.HEIGHT_E,
                self.WIDTH * (i_ + 1) + self.WIDTH // self.WIDTH_E,
                self.HEIGHT * (self.flr - i) + self.HEIGHT // self.HEIGHT_E,
            )
        for i in self.state.main_state:
            canvas.create_oval(
                self.WIDTH * (self.elv + 0.5) - self.CST_R,
                (self.flr - i) * self.HEIGHT - self.CST_R,
                self.WIDTH * (self.elv + 0.5) + self.CST_R,
                (self.flr - i) * self.HEIGHT + self.CST_R,
                fill="red",
            )
        Button(canvas, text="Next Step", command=next_step, bg="light blue").place(
            x=self.WIDTH // 2, y=0
        )
        Button(canvas, text="Return", command=return_butt, bg="light blue").place(
            x=(self.elv + 1) * self.WIDTH - self.WIDTH // 2, y=0
        )

    def main(self):
        c = Canvas(
            self.root,
            width=self.WIDTH * (self.elv + 2),
            height=self.HEIGHT * (self.flr + 1),
        )
        c.grid(row=0, column=0)

        self.draw(c)

    def configs(self):
        def submit():
            self.flr = int(flr.get())
            self.elv = int(elv.get())
            main_frame.destroy()

            self.flr += 1
            self.state = State(self.flr, self.elv)
            self.main()

        main_frame = Frame(self.root)
        main_frame.grid(row=0, column=0)
        flr = IntVar(main_frame)
        elv = IntVar(main_frame)
        self.flr: int
        self.elv: int
        self.state: State
        font = {"font": ("Arial", 15)}

        flr_o = OptionMenu(main_frame, flr, *range(self.MAX_FLR + 1))
        elv_o = OptionMenu(main_frame, elv, *range(self.MAX_ELV + 1))
        flr_o.config(**font)
        elv_o.config(**font)
        flr_o.grid(row=0, column=1)
        elv_o.grid(row=1, column=1)

        Label(main_frame, text="تعداد طبقات", **font).grid(row=0, column=0)
        Label(main_frame, text="تعداد آسانسورها", **font).grid(
            row=1, column=0, padx=20, pady=20
        )

        Button(main_frame, text="ثبت", **font, command=submit).grid(
            row=2, column=0, columnspan=2
        )


def draw_lines(w, elv, flr, cst, elv_locs):
    flr += 1
    width = 75  #
    height = 50  #
    width_flr = 10  #
    cst_r = 5  #
    width_e = 4
    height_e = 3
    # w = Canvas(master, width=width * (elv + 2), height=height * (flr + 1))

    for i in range(1, flr + 1):
        w.create_text(width * (elv + 1), i * height, text=flr - i)
    for i in range(1, elv + 1):
        w.create_line(i * width, height, i * width, height * flr)
        for j in range(1, flr + 1):
            w.create_line(
                i * width - width // width_flr,
                j * height,
                i * width + width // width_flr,
                j * height,
            )
    for i_, i in enumerate(elv_locs):
        w.create_rectangle(
            width * (i_ + 1) - width // width_e,
            height * (flr - i) - height // height_e,
            width * (i_ + 1) + width // width_e,
            height * (flr - i) + height // height_e,
        )
    for i in cst:
        w.create_oval(
            width * (elv + 0.5) - cst_r,
            (flr - i) * height - cst_r,
            width * (elv + 0.5) + cst_r,
            (flr - i) * height + cst_r,
            fill="red",
        )
    return w


# root = Tk()
# c = draw_lines(root, 4, 8, [1, 3, 5, 8, 0], [3, 5, 8, 0])
# c.pack()
# root.mainloop()
UI()
