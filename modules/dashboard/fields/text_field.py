from .field_base import FieldBase
from .util.label import Label


class TextField(FieldBase):
    def __init__(
        self,
        name: str,
        label_name: str,
        value: str = None,
        placeholder: str = "",
        id: str = None,
        validators: list[str] = None,
        conditional_display: list[str] = None,
    ):
        super().__init__(name=name, val=value if value is not None else "", id=id, validators=validators, conditional_display=conditional_display)
        self.label_name = label_name
        self.placeholder = placeholder
        

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, val: str = None):
        self._value = "" if val is None else str(val)

    def _render(self):

        tag_attrs = {
            "type": "text",
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "placeholder": self.placeholder
        }

        if self.validators:
            tag_attrs["data-validate"] = self.validator_js
        
        if self.conditional_display:
            tag_attrs["data-display"] = self.conditional_display_js

        tag_attrs_str = " ".join(f"{key}='{value}'" for key, value in tag_attrs.items())  
        textfield_html = f"<input {tag_attrs_str}>"  
        
        return textfield_html

    def render(self):
        return Label(target=self).render()
