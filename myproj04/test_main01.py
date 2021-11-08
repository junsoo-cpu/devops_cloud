import pytest
from main01 import get_word_count, get_ch_count_except_space, get_rounded_number


@pytest.mark.parametrize(  # 테스트를 두개의 케이스로 나타내는 방법
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("Python Family", 2),
    ],
)
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected
    # assert 뒷 문장이 참이기를 기대하는 문법


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 10),
        ("Python Family", 12),
    ],
)
def test_get_ch_count_excpet_space(sentence, expected):
    assert get_ch_count_except_space(sentence) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        (123456, 123000),
        (1234, 1000),
    ],
)
def test_get_rounded_number(sentence, expected):
    assert get_rounded_number(sentence) == expected
