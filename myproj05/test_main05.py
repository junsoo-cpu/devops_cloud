# TDD 테스트 주도 개발
from main05 import make_powered_list

# 이 테스트가 이 함수에 대한 스펙(요구사항)


def test_make_powered_list():
    numbers = [0, 1, 2, 3, 4]
    expected = [0, 1, 4, 9, 16]
    assert make_powered_list(numbers) == expected


def test_make_powered_list2():
    numbers = [0, 1, 2, 3, 4]
    expected = [0, 1, 4, 9, 16]
    assert make_powered_list2(numbers) == expected
