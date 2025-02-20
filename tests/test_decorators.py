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
    assert result == 3

    result = test_func(1, "2")
    assert result == "Произошла ошибка"


# def test_my_function_error():
#     @log()
#     def test_func_fail(x, y):
#         return x + y
#
#     result = test_func_fail(1)
#     with pytest.raises(Exception, match="my_function error unsupported operand type(s) for +: 'int' and 'str'. Input (1, '2')") as exc:
#        test_func_fail(1,'2')
