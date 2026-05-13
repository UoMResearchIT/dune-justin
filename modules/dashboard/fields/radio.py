from .field_base import FieldBase
from .util.label import Label

class Radio(FieldBase):
    def __init__(
        self, 
        name: str, 
        value: str, 
        label_name: str, 
        id: str = None, 
        checked: bool = False,
        conditional_display: list[str] = None
    ):
        super().__init__(name=name, val=value, id=id, conditional_display=conditional_display)
        self.label_name = label_name
        self.checked = checked

    @property
    def value(self):
        return self._value if self.checked else None
    
    @value.setter
    def value(self, value: str):
        self._value = value

    def reset(self):
        self.checked = False

    def _render(self):
        checked_attr = " checked" if self.checked else ""
        
        if self.conditional_display:
            radio_html = f"<input type='radio' id='{self.id}' name='{self.name}' value='{self.value}' {checked_attr} data-display='{self.conditional_display_js}'>"
        else:
            radio_html = f"<input type='radio' id='{self.id}' name='{self.name}' value='{self.value}' {checked_attr}>"
        
        return radio_html
        

    def render(self):
        return Label(target=self, is_target_after_label=True).render()
    

class RadioGroup(FieldBase):
    def __init__(
        self,
        name: str,
        options: list[dict[str, str]],
        value: str = None,
        validators: list[str] = None,
        conditional_display: list[str] = None,
    ):
        super().__init__(name=name)
        self.validators = validators
        self._radios = [
            Radio(
                name=name,
                value=opt['value'],
                label_name=opt['label'],
                id=opt['id'],
                checked=(opt['value'] == value),
                conditional_display=conditional_display
            )
            for opt in options
        ]

    @property
    def value(self):
        for radio in self._radios:
            if radio.checked:
                return radio.value
        return None

    @value.setter
    def value(self, value: str):
        if value is None:
            return
        
        self.reset()

        for radio in self._radios:
            radio.checked = (radio._value == value)
   
    def reset(self):
        for radio in self._radios:
            radio.reset()
 
    def render(self):
        return "".join(radio.render() for radio in self._radios)