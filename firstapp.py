from textual.app import App, ComposeResult
from textual.events import Key
from textual.color import Color
from textual.widgets import Button, Label, Header, Footer, Static
from textual.containers import Container, Horizontal 

QUESTION = "Do you want to learn about Textual CSS?"

class FirstApp(App[str]):

    CSS_PATH = "firstapp.tcss"
    
    TITLE = "FirstApp"
    SUB_TITLE = "First Textual App to learn about the framework"
    
    def compose(self) -> ComposeResult:
        self.screen.styles.background = Color(30, 35, 55)

        self.header = Header(show_clock=True)
        yield self.header
        
        self.footer = Footer()
        yield self.footer
        
        yield Container(
            Static(QUESTION, classes="question"),
            Horizontal(
                Button("Yes", variant="success"),
                Button("No", variant="error"),
                classes="buttons",
            ),
            id="dialog",
        )
        
        # Static widget call without corresponding tcss snippet
        # self.widget = Static("Textual")
        # yield self.widget
        
        self.label = Label("Do you love Textual ?", id="question")
        yield self.label
        
        self.buttonyes = Button("Yes", id="yes", variant="primary")
        yield self.buttonyes
        
        self.buttonno  = Button("No", id="no", variant="error")
        yield self.buttonno
        
        
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)
        
    def on_key(self, event: Key):
        self.title = event.key
        self.sub_title = f"You just pressed {event.key}!"



if __name__ == "__main__":
    app = FirstApp()
    reply = app.run()
    print(reply)
    
    