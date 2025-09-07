from src.task4_console_bot import (
    add_contact,
    change_phone,
    show_phone,
    show_all,
)


def test_add_contact_ok():
    contacts = {}
    msg = add_contact(["Ann", "123"], contacts)
    assert msg == "Contact added."
    assert contacts["Ann"] == "123"


def test_add_contact_value_error():
    contacts = {}
    msg = add_contact(["Ann"], contacts)  # не вистачає телефону
    assert msg == "Give me name and phone please."
    assert "Ann" not in contacts


def test_show_phone_index_error():
    contacts = {"Ann": "123"}
    msg = show_phone([], contacts)
    assert msg == "Enter user name."


def test_show_phone_key_error():
    contacts = {"Ann": "123"}
    msg = show_phone(["Bob"], contacts)
    assert msg == "Contact not found."


def test_change_phone_ok():
    contacts = {"Ann": "123"}
    msg = change_phone(["Ann", "999"], contacts)
    assert msg == "Contact updated."
    assert contacts["Ann"] == "999"


def test_change_phone_missing_args():
    contacts = {"Ann": "123"}
    msg = change_phone(["Ann"], contacts)
    assert msg == "Give me name and new phone please."


def test_change_phone_not_found():
    contacts = {}
    msg = change_phone(["Ann", "999"], contacts)
    assert msg == "Contact not found."


def test_show_all_empty():
    contacts = {}
    msg = show_all([], contacts)
    assert msg == "No contacts."
