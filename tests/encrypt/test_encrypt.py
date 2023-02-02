import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    check_key()
    check_message()
    check_encrypt()


def check_key():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("123456", "1")


def check_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 1)


def check_encrypt():
    assert encrypt_message("123456", 10) == "654321"

    assert encrypt_message("vanessa", 3) == "nav_asse"

    assert encrypt_message("vanessa", 4) == "ass_enav"
