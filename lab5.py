import pytest
from practical_tasks.task_2 import prime_num_generator
from practical_tasks.task_3 import palindrom, validate_ip, get_os


@pytest.fixture
def primes_list():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


@pytest.fixture
def palindrome_input_texts():
    return ["aba", "abba", "racecar", "level", "repaper"]


@pytest.fixture
def palindrome_invalid_input_texts():
    return ["", "   ", "hello", "world", "not", "a", "palindrome"]


@pytest.mark.parametrize("n, expected_result", [(12, 37), (101, 547)])
def test_prime_num_generator(primes_list, n, expected_result):
    assert prime_num_generator(n) == expected_result


def test_palindrom_with_input_texts(palindrome_input_texts):
    for text in palindrome_input_texts:
        assert palindrom(text)


def test_palindrom_with_invalid_input_texts(palindrome_invalid_input_texts):
    for text in palindrome_invalid_input_texts:
        assert not palindrom(text)


@pytest.mark.parametrize("ip, expected_result", [("192.168.1.1", True), ("10.0.0.1", True),
                                                ("172.20.256.1", False), ("256.255.255.255", False),
                                                ("172.20.10.0/24", True), ("172.20.10.0/256", False),
                                                ("172.20.10.1/32", True), ("172.20.10.1/33", False)])
def test_validate_ip(ip, expected_result):
    assert validate_ip(ip) == expected_result


def test_get_os():
    os_name = get_os()
    assert isinstance(os_name, str) and os_name != ""