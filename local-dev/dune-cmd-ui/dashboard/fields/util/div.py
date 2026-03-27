from dashboard.fields.field_base import HtmlElement
class Div(HtmlElement):
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"<div>{self.content}</div>"
