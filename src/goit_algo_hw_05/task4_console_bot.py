from __future__ import annotations

from functools import wraps
from typing import Callable, Dict, List, Tuple

Contacts = Dict[str, str]


def input_error(
    *,
    msg_value_error: str = "Give me name and phone please.",
    msg_key_error: str = "Contact not found.",
    msg_index_error: str = "Enter user name.",
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    """
    Декоратор обробляє помилки введення користувача і повертає дружні повідомлення,
    не перериваючи роботу програми.
    """
    def deco(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            try:
                return func(*args, **kwargs)
            except ValueError:
                return msg_value_error
            except KeyError:
                return msg_key_error
            except IndexError:
                return msg_index_error
        return wrapper
    return deco


# ---------- Команди (handlers) ----------

@input_error(msg_value_error="Give me name and phone please.")
def add_contact(args: List[str], contacts: Contacts) -> str:
    name, phone = args  # ValueError, якщо аргументів не 2
    contacts[name] = phone
    return "Contact added."


@input_error(
    msg_value_error="Give me name and new phone please.",
    msg_key_error="Contact not found.",
)
def change_phone(args: List[str], contacts: Contacts) -> str:
    name, phone = args  # ValueError, якщо не 2
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error(
    msg_index_error="Enter user name.",
    msg_key_error="Contact not found.",
)
def show_phone(args: List[str], contacts: Contacts) -> str:
    name = args[0]  # IndexError, якщо не вказано name
    return contacts[name]  # KeyError, якщо немає такого контакту


@input_error()
def show_all(args: List[str], contacts: Contacts) -> str:
    if not contacts:
        return "No contacts."
    rows = [f"{n}: {p}" for n, p in contacts.items()]
    return "\n".join(rows)


def hello(_: List[str], __: Contacts) -> str:
    return "How can I help you?"


def help_text(_: List[str], __: Contacts) -> str:
    return (
        "Available commands:\n"
        "  hello\n"
        "  add <name> <phone>\n"
        "  change <name> <new_phone>\n"
        "  phone <name>\n"
        "  all\n"
        "  help\n"
        "  exit | close | good bye"
    )


def exit_cmd(_: List[str], __: Contacts) -> str:
    return "Good bye!"


# ---------- Парсер і цикл ----------

COMMANDS: Dict[str, Callable[[List[str], Contacts], str]] = {
    "hello": hello,
    "help": help_text,
    "add": add_contact,
    "change": change_phone,
    "phone": show_phone,
    "all": show_all,
    "exit": exit_cmd,
    "close": exit_cmd,
    "good": exit_cmd,   # дозволимо "good bye"
}


def parse_command(user_input: str) -> Tuple[str, List[str]]:
    tokens = user_input.strip().split()
    if not tokens:
        return "", []
    cmd = tokens[0].lower()
    # Спеціальний випадок "good bye"
    if cmd == "good" and len(tokens) >= 2 and tokens[1].lower() == "bye":
        return "good", []
    return cmd, tokens[1:]


def run_bot() -> None:
    contacts: Contacts = {}
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            # Симуляція прикладу: просити аргументи при порожній команді
            print("Enter the argument for the command")
            continue

        cmd, args = parse_command(user_input)
        handler = COMMANDS.get(cmd)

        if handler is None:
            print("Unknown command. Type 'help' to see available commands.")
            continue

        result = handler(args, contacts)
        print(result)

        if handler is exit_cmd:
            break
