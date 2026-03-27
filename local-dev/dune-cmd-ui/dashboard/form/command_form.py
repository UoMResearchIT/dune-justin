from collections import OrderedDict

from ..fields.field_base import FieldBase
from ..fields.fieldset import FieldSet


class CommandForm:
    def __init__(
        self,
        fields: list[FieldBase],
        cgi_method: str,
        action: str = "/dashboard/",
        request_method: str = "GET",
    ):
        self._fields: list[FieldBase] = fields
        self.action: str = action
        self.cgi_method: str = cgi_method
        self.request_method: str = request_method
        self.css_style = (
            "display: flex; flex-direction: column; gap: 10px; align-items: flex-start;"
        )

    @property
    def fields(self) -> list[FieldBase]:
        fs = []
        for f in self._fields:
            if isinstance(f, FieldSet):
                fs.extend(f.fields.values())
            elif isinstance(f, FieldBase):
                fs.append(f)
            else:
                raise TypeError(f"CommandForm fields must be FieldBase or FieldSet instances. found type: {type(f)} with value: {f}")
        return fs
        

    @property
    def field_dict(self) -> dict[str, FieldBase]:
        return {field.name: field for field in self._fields}

    def update(
        self, field_values: dict[str, str], is_ignore_unknown_fields: bool = True
    ):
        """Bulk update field values from a dict, e.g. cgi value"""
        for field_name, field_value in field_values.items():
            try:
                self[field_name] = field_value
            except KeyError:
                if is_ignore_unknown_fields is False:
                    raise KeyError(
                        f"Field with name '{field_name}' not found in FilterForm."
                    )

    def __setitem__(self, field_name: str, field_value: str):
        for i, f in enumerate(self.fields):
            if f.name == field_name:
                f.value = field_value
                self._fields[i] = f
                return
        raise KeyError(f"Field with name '{field_name}' not found in FilterForm.")

    def __getitem__(self, field_name: str) -> str:
        return self.get_field(field_name).value

    def get_field(self, field_name: str) -> FieldBase:
        f = self.field_dict.get(field_name)
        if f is None:
            raise KeyError(f"Field with name '{field_name}' not found in FilterForm.")
        return f

    def set_field(self, field: FieldBase):
            if field.name is None:
                raise ValueError("Field must have a name to be set in FilterForm.")

            for i, f in enumerate(self._fields):
                if f is isinstance(f, FieldSet):
                    for j, sub_f in enumerate(f.fields):
                        if sub_f.name == field.name:
                            f.fields[j] = field
                            self._fields[i] = f
                            return
                elif not isinstance(f, FieldBase):
                    raise TypeError("FilterForm fields must be FieldBase or FieldSet instances.")
                elif f.name == field.name:
                    self._fields[i] = field
                    return
            raise KeyError(f"Field with name '{field.name}' not found in FilterForm.")
    
    def as_fieldset(self)  -> List[FieldSet]:
        pass
    

    def render_submit_button(self):
        return "<input type='submit' value='Filter' style='background: #E1703D; border-radius: 5px; padding: 5px; color: white; font-weight: bold; font-size: 1em; border: 0; cursor: pointer'>"

    def render(self) -> str:

        form_html = "<h1>Command Form</h1>"
        form_html += f"<form action='{self.action}' method='{self.request_method}', style='{self.css_style}'>"
        form_html += f"<input type='hidden' name='method' value='{self.cgi_method}'>"

        for field in self._fields:
            form_html += field.render()

        form_html += self.render_submit_button()
        form_html += "</form>"

        return form_html
