from .field_base import FieldBase
from .util.label import Label


class TextField(FieldBase):
    def __init__(
        self,
        name: str,
        label_name: str,
        value: str | None = None,
        placeholder: str = "",
        id: str | None = None,
        validators: list[str] | None = None,
    ):
        super().__init__(name=name, val=value if value is not None else "", id=id, validators=validators)
        self.label_name = label_name
        self.placeholder = placeholder
        

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, val: str | None):
        self._value = "" if val is None else str(val)

    def _render(self):
        if self.validators:
            textfield_html = f"<input type='text' id='{self.id}' name='{self.name}' value='{self.value}' placeholder='{self.placeholder}' data-validate='{self.validator_js}'>"
        else:
            textfield_html = f"<input type='text' id='{self.id}' name='{self.name}' value='{self.value}' placeholder='{self.placeholder}'>"

            
        return textfield_html

    def render(self):
        return Label(target=self).render()
