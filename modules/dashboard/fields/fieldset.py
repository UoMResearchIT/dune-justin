from .field_base import FieldBase

class FieldSet(FieldBase):
    def __init__(self, name: str, fields: list[FieldBase]):
        super().__init__(name=name, val=fields)
    
    @property    
    def value(self) -> dict[str, str]:
        return {field.name: field.value for field in self._fields}
    
    @value.setter
    def value(self, new_value: list[FieldBase]):
        self._value = new_value
    
    @property
    def fields(self) -> list[FieldBase]:
        return {field.name: field for field in self._value}
    
    @fields.setter
    def fields(self, new_fields: list[FieldBase]):
        self.value = new_fields

    def render(self):
        fieldset_html =  f"<fieldset>"
        fieldset_html += f"<legend>{self.name}</legend>"
        for field in self.fields.values():
            fieldset_html += field.render()
        fieldset_html += "</fieldset>"
        return fieldset_html
