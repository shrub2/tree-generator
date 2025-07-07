from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.timer import Timer
import random

class Branch():
    def __init__(self, x_pos=0, y_pos=0, angle=90, age=1):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.age = age

    def grow(self) -> bool:
        if self.age == 0:
            return False

        self.x_pos += random.randint(-1, 1)
        self.y_pos += 1

        if self.x_pos > 63 or self.x_pos < 0:
            self.age = 0
            return False

        elif self.y_pos > 31 or self.y_pos < 0:
            self.age = 0
            return False
        
        return True

class TreeGenerator(App):
    DISP_WIDTH = 64
    DISP_HEIGHT = 32

    CSS = f"""
    #tree_box {{
        width: {DISP_WIDTH};
        height: {DISP_HEIGHT};
        background: black;
        color: lightgreen;
        content-align: center middle;
    }}
    """

    def __init__(self):
        super().__init__()
        self.grid = [[' ' for _ in range(self.DISP_WIDTH)] for _ in range(self.DISP_HEIGHT)]
        self.branches = [Branch(20, -1), Branch(40, -1)]
        self.timer: Timer | None = None
        self.tree_display: Static | None = None

    def animate_step(self):
        self.branches = [b for b in self.branches if b.grow()]
        for branch in self.branches:
            self.grid[branch.y_pos][branch.x_pos] = 'T'

        display_string = "\n".join("".join(row) for row in reversed(self.grid))
        self.tree_display.update(display_string)

        if not self.branches:
            self.timer.stop()

    def on_mount(self):
        self.timer = self.set_interval(0.1, self.animate_step)

    def compose(self) -> ComposeResult:
        self.tree_display = Static("", id="tree_box")
        yield self.tree_display


if __name__ == "__main__":
    TreeGenerator().run()
