import pytest


def func(x):
    return x + 1


def t_est_answer():
    assert func(3) == 5


def f_():
    raise SystemExit(1)


def t_est_mytest():
    with pytest.raises(SystemExit):
        f_()


class TestClass(object):

    def t_est_one(self):
        x = "this"
        assert 'h' in x

    def t_est_two(self):
        x = "hello"

        assert hasattr(x, 'check')


def t_est_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def t_est_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)


def myfunc(x):

    if x>3:
        raise  Exception("new")
    #raise ValueError("Exception 123 raised")


def test_match():
    pytest.raises(Exception,myfunc,4)

