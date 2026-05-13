from .field_base import FieldBase
from datetime import datetime as dt
from .util.label import Label


class DateSelector(FieldBase):
    date_format = "%Y-%m-%d"

    def __init__(self, name: str, label_name: str, value: str = None, conditional_display: list[str] | None = None):
        super().__init__(
            name, value if value else dt.today().strftime(self.date_format), conditional_display = conditional_display
        )
        self.label_name = label_name if label_name else name.replace("_", " ")

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_dt_value: str):
        if new_dt_value is None:
            return
        try:
            dt.strptime(new_dt_value, self.date_format)  # validation
            self._value = new_dt_value
        except Exception:
            raise ValueError(
                f"[Failed to set DateSelector value]: Invalid date format for '{new_dt_value}'. Expected format: {self.date_format}"
            )

    def _render(self):
        if self.conditional_display:
            data_selector_html = f"<input class='date-selector'type='date' id='{self.id}' name='{self.name}' value='{self.value}' id='datepicker' data-display='{self.conditional_display_js}'>"
        else:
            data_selector_html = f"<input class='date-selector'type='date' id='{self.id}' name='{self.name}' value='{self.value}' id='datepicker'>"
        return data_selector_html

    def render(self):
        return Label(target=self).render()
