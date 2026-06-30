from .div import Div
from ..field_base import FieldBase, HtmlElement


class Label(HtmlElement):
    def __init__(self, target: FieldBase = None, is_target_after_label: bool = False):
        self.target_id = target.id if target else None
        self.target_label_name = (
            target.label_name if hasattr(target, "label_name") else target.name
        )
        self.content = target._render()
        self.is_target_after_label = is_target_after_label

    def render(self) -> str:
        label_html = f"<label for='{self.target_id}'>{self.target_label_name}</label>"
        if self.is_target_after_label:
            label_html = self.content + '<span> </span>' + label_html
        else:
            label_html += '<span>: </span>' + self.content
        return Div(content=label_html).render()
