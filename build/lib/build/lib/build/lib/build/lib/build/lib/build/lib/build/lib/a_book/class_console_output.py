from abc import ABC, abstractmethod
import types
from enum import Enum, auto


class Terminals(Enum):
    TERMINAL = auto()
    TELEGRAM = auto()
    VIBER = auto()


class ConsoleOutputAbstract(ABC):
    service: Enum

    @abstractmethod
    def output(self, text: str, *args) -> str:
        ...


class TerminalOutput(ConsoleOutputAbstract):
    service = Terminals.TERMINAL

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        print(f"Send to TerminalOutput: {text}")


class Telegram:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Telegram")


class TelegramOutput(ConsoleOutputAbstract):
    service = Terminals.TELEGRAM

    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)
        super().__init__()

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        self.telegram_client.send_message(text)


class Viber:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Viber")


class ViberOutput(ConsoleOutputAbstract):
    service = Terminals.VIBER

    def __init__(self, token) -> None:
        self.viber_client = Viber(token)
        super().__init__()

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        self.viber_client.send_message(text)


class FactoryOutput:
    def __init__(self):
        self._output = {}

    def register_output(self, output: ConsoleOutputAbstract):
        if output and issubclass(output, ConsoleOutputAbstract):
            service = output.service
            if service:
                self._output[service] = output
                return
        raise ValueError("Problem registration of service")

    def get_registered_services(self):
        return list(self._output.keys())

    def unregister_output(self, output: ConsoleOutputAbstract):
        self._output.remove(output)

    def create_output(self, service: Enum, *args, **kwargs):
        if service in self._output:
            return self._output[service](*args, **kwargs)
        else:
            raise ValueError(f"Invalid service of output ({service.name})")
