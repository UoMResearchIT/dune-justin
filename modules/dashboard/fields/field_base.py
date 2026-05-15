from abc import ABC, abstractmethod


class HtmlElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class FieldBase(HtmlElement):
    def __init__(
        self, name: str, val: str = None, id: str = None, validators: list[str] = None, conditional_display: list[str] = None,
    ):
        self.name = name
        self._value = val
        self._id = id
        self.validators = validators
        self.conditional_display = conditional_display

    @property
    @abstractmethod
    def value(self) -> str:
        pass

    @value.setter
    @abstractmethod
    def value(self, new_value):
        pass

    @property
    def id(self):
        return self._id if self._id else self.name

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def validator_js(self) -> str:
        if not self.validators: return None
        args = " ".join((self.validators))
        return args

    @property
    def conditional_display_js(self) -> str:
        if not self.conditional_display: return None
        args = " ".join((self.conditional_display))
        return args
