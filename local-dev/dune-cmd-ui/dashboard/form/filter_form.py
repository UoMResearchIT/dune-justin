from dashboard.fields.field_base import FieldBase, HtmlElement

class FilterForm:
    def __init__(
        self,
        fields: list[HtmlElement],
        cgi_method: str,
        action: str = "/dashboard/",
        request_method: str = "GET",
    ):
        self._fields: list[HtmlElement] = fields
        self.action: str = action
        self.cgi_method: str = cgi_method
        self.request_method: str = request_method

    @property
    def fields(self) -> list[HtmlElement]:
        return [f for f in self._fields]

    @property
    def field_dict(self) -> dict[str, FieldBase]:
        return {field.name: field for field in self.fields}

    @property
    def css_style(self) -> str:
        return (
            "display: flex; flex-direction: column; gap: 10px; align-items: flex-start;"
        )

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

    def render_submit_button(self):
        return "<input type='submit' value='Filter' style='background: #E1703D; border-radius: 5px; padding: 5px; color: white; font-weight: bold; font-size: 1em; border: 0; cursor: pointer'>"

    def render(self) -> str:

        form_html = f"<form action='{self.action}' method='{self.request_method}', style='{self.css_style}'>"
        form_html += f"<input type='hidden' name='method' value='{self.cgi_method}'>"

        fields = self._fields

        for field in fields:
            form_html += field.render()

        form_html += self.render_submit_button()
        form_html += "</form>"

        return form_html
