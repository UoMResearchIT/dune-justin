from abc import ABC, abstractmethod


class HtmlElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class FieldBase(HtmlElement):
    def __init__(
        self, name: str, val: str = None, id: str = None, validators: list[str] = None
    ):
        self.name = name
        self._value = val
        self._id = id
        self.validators = validators

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
