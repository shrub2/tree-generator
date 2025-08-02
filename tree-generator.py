from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.timer import Timer
import random
import math

#Globals
DISP_WIDTH = 84
DISP_HEIGHT = 32

class Branch():
    def __init__(self, x_pos=0.0, y_pos=0.0, angle=90.0, age=1):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.initial_age = age
        self.age = age

        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def grow(self) -> bool:
        if self.age <= 0:
            return False

        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))

        self.x_pos += dx
        self.y_pos += dy

        if self.x_pos > DISP_WIDTH-1 or self.x_pos < 0:
            self.age = 0
            return False
        elif self.y_pos > DISP_HEIGHT-1 or self.y_pos < 0:
            self.age = 0
            return False

        if dy < 0:
            self.age -= 2
        else:
            self.age -= 1
        
        return True

class TreeGenerator(App):
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
        self.timer: Timer | None = None
        self.tree_display: Static | None = None
        self.init_state()

    def init_state(self):
        self.grid = [[' ' for _ in range(DISP_WIDTH)] for _ in range(DISP_HEIGHT)]
        self.branches = [Branch(42, -1, age=25)]

    def start_animation(self):
        if self.timer:
            self.timer.stop()
        self.timer = self.set_interval(0.075, self.animate_step)

    def animate_step(self):
        #for index in range(10):
        #    self.grid[index][42] = 'T'

        self.branches = [b for b in self.branches if b.grow()]
        new_branches = []
        for branch in self.branches:
            grid_y = int(round(branch.y_pos))
            grid_x = int(round(branch.x_pos))

            if not branch.age:
                self.grid[grid_y][grid_x] = "[green]@[/green]"
            else:
                self.grid[grid_y][grid_x] = "[brown]t[/brown]"

            split_chance = max(0.05, 0.3 * (branch.age / branch.initial_age))
            if branch.age and random.random() < split_chance:
                new_x = branch.x_pos
                new_y = branch.y_pos
                new_angle = branch.angle + random.uniform(-25, 25)
                new_age = random.randint(5, 10)
                new_branches.append(Branch(new_x, new_y, new_angle, new_age))

        if new_branches:
            self.branches.extend(new_branches)

        display_string = "\n".join("".join(row) for row in reversed(self.grid))
        self.tree_display.update(display_string)

        if not self.branches and self.timer:
            self.timer.stop()

    def reset_tree(self):
        self.init_state()
        self.tree_display.update("")
        self.start_animation()
        
    def on_mount(self):
        self.start_animation()

    def compose(self) -> ComposeResult:
        self.tree_display = Static("", id="tree_box")
        yield self.tree_display

    def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            self.reset_tree()


if __name__ == "__main__":
    TreeGenerator().run()
