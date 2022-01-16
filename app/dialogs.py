from dataclasses import dataclass


@dataclass(frozen=True)
class Messages:
    start_text: str = "Привет {name}!\nКак ты?"
    help_test: str = "Это сообщение о помощи!"
    unknown_text: str = "Ничего не понятно, но очень интересно!\nПопробуй команду /help"


msg = Messages()
