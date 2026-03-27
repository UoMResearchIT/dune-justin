from .field_base import FieldBase
from .util.label import Label


class Checkbox(FieldBase):
    def __init__(
        self,
        name: str,
        label_name: str,
        value = str,
        id: str | None = None,
        validators: list[str] | None = None,
        is_checked: bool = False,
    ):
        super().__init__(name=name, val=value, id=id, validators=validators)
        self.label_name = label_name
        self.is_checked = is_checked

    @property
    def value(self) -> bool:
        return self._value
    
    @value.setter
    def value(self, val: str | None):
        self._value = val
    
    def reset(self):
        self.is_checked = False

    def _render(self):
        validator_attr = f"onchange='{self.validator_js}'" if self.validators else ""
        checked_attr = "checked" if self.is_checked else ""
        checkbox_html = (
            f"<input type='checkbox' id='{self.id}' name='{self.name}' value='{self.value}' "
            f"{checked_attr} "
            f"{validator_attr} "
            f">"
            )
        return checkbox_html

    def render(self):
        return Label(target=self, is_target_after_label=True).render()