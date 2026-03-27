from .field_base import FieldBase
from .util.label import Label


class Option:
    default_value = "ANY"

    def __init__(self, value: list[str], is_selected: bool = False):
        self.value = value
        self.is_selected = is_selected

    def render(self):
        if self.is_selected:
            option_html = f"<option value='{self.value}' selected>{self.value}</option>"
        else:
            option_html = f"<option value='{self.value}'>{self.value}</option>"

        if self.value == self.default_value:
            option_html += "<option disabled>---</option>"

        return option_html


class Select(FieldBase):
    def __init__(self, name: str, label_name: str, options: list[str], value=None):
        super().__init__(name=name, val=None)
        self.label_name = label_name
        options = [Option(value=o, is_selected=False) for o in options]
        default_option = Option(value=Option.default_value, is_selected=False)
        self._options = [default_option] + options
        self.reset()

        self.value = value if value else default_option.value

    @property
    def value(self) -> str:
        """curent selected option"""
        return self._value.value if self._value else None

    @value.setter
    def value(self, opt_val: str):
        """select option by value"""
        if opt_val is None:
            return
        self.reset()  # single selection
        for option in self.options:
            if str(option.value) == str(opt_val):
                option.is_selected = True
                self._value = option
                return
        raise ValueError(
            f"failed to select value '{opt_val}' in Select '{self.name}'. "
            f"available: {[o.value for o in self.options]}"
        )

    @property
    def options(self) -> list[Option]:
        return self._options

    def reset(self):
        for option in self.options:
            option.is_selected = False
        self._value = None

    def _render(self):
        select_html = f"<select name='{self.name}' id='{self.id}'>"
        for option in self.options:
            select_html += option.render()
        select_html += "</select>"
        return select_html

    def render(self):
        out_html = Label(target=self).render()
        return out_html
