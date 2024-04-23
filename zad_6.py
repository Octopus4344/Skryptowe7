import datetime
import logging
import time
from functools import wraps


def log(log_level):
    def log_decorator(func_or_class):
        logger = logging.getLogger(__name__)

        @wraps(func_or_class)
        def wrapper(*args, **kwargs):
            start_date = datetime.datetime.now()
            start_time = time.time()
            result = func_or_class(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            logger.log(log_level,
                       f"{start_date}: Function {func_or_class.__name__} called with args: {args}, kwargs: {kwargs}; returned {result}; took {duration} seconds")
            return result

        return wrapper

    return log_decorator


if __name__ == "__main__":
    formatter = logging.Formatter('%(message)s')

    logging.basicConfig(level=logging.INFO)

    for handler in logging.root.handlers:
        handler.setFormatter(formatter)


    @log(logging.INFO)
    def slow_function(a, b):
        time.sleep(1)
        return a + b


    slow_function(1, 2)
    slow_function(1, 3)
