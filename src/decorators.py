from time import time
from functools import wraps


def log(filename=None):
    """Декоратор log, который автоматически логирует начало и конец выполнения функции,а также ее результаты
    или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                result = "Произошла ошибка"
                end_time = time()
                log_message = f"{func.__name__} error {str(e)}. Input {args} {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                raise e

        return wrapper

    return decorator
