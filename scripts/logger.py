from rich import print
from datetime import datetime


class Logger:
    def __init__(self, name: str):
        self.name = name

    def log(self, *objects):
        text = ""
        for object in objects:
            text += str(object) + " "
        text = text[:-1]

        print("[white](%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))

    def warning(self, *objects):
        text = ""
        for object in objects:
            text += str(object) + " "
        text = text[:-1]

        print("[yellow](%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))

    def error(self, *objects):
        text = ""
        for object in objects:
            text += str(object) + " "
        text = text[:-1]

        print(f"[red](%s)[%s]: %s"%(
            datetime.now().strftime("%H:%M:%S"),
            self.name,
            text
        ))


