from textual.app import App, ComposeResult
from textual.widgets import Static
import textwrap

class TreeGenerator(App):
    CSS = """
    #tree_box {
        width: 66;
        height: 34;
        border: solid green;
        background: black;
        color: lightgreen;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        tree = textwrap.dedent("""
            @@@@@@@@
          @@@@@@@@@@@@@
        @@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@
         @@@@@@@@@@@@@@@@
             @@@@@@@@@
         @@@   TTTTT
          @@TT TTTTT
             TTTTTTT
               TTTTT
               TTTTTT
              TTTTTTTT
            TTTTTTTTTTTT
        """)
        yield Static(tree, id="tree_box")

if __name__ == "__main__":
    TreeGenerator().run()
