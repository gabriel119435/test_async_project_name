import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


@pytest.mark.parametrize(
    "input, output",
    [
        (1, 2),
        (3, 4),
        (100, 101)
    ]
)
def test_answer(input, output):
    assert func(input) == output


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClassDemoInstance:
    value = 2

    def test_one(self):
        self.value = 1
        assert self.value == 1
        self.value = 0

    def test_two(self):
        assert self.value == 2
