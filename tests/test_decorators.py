import pytest
from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_success(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_my_function_success():
    @log(filename="mylog.txt")
    def test_func(x, y):
        return x + y

    result = test_func(1, 2)
    with open("mylog.txt", "r") as f:
        all_lines = f.readlines()
        message = all_lines[-1]
    assert message == "test_func ok\n"


def test_my_function_error(capsys):
    @log()
    def func_fail(x, y):
        return x + y

    with pytest.raises(TypeError) as exc:
        func_fail(1, "2")

        captured = capsys.readouterr()
        assert (
            captured.out == "my_function error unsupported operand type(s) for +: 'int' and 'str'. Input (1, '2') {}"
        )


def test_my_function_write_log():
    @log()
    def func_fail(x, y):
        return x + y

    with pytest.raises(TypeError) as exc:
        func_fail(1, "2")

        with open("mylog.txt", "r") as f:
            all_lines = f.readlines()
            message = all_lines[-1]
        assert message == "my_function error unsupported operand type(s) for +: 'int' and 'str'. Input (1, '2') {}"
