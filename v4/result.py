from typing import Callable, TypeVar

Request = TypeVar('Request')
Response = TypeVar('Response')


class Result(object):
    def __init__(self):
        self.value = None
        self.value_callback = None

    def run(self, data: object,
         output: Callable[[str, str], None],
         error: Callable[[str, Exception], None]) -> None:
        if self.value_callback:
            self.value_callback(data)
        else:
            self.value = data

    def sync(self):
        return self.value
