from typing import Callable, TypeVar, Generic, Dict, Any

Request = TypeVar('Request')
Response = TypeVar('Response')


class FNode(Generic[Request, Response]):
    def __init__(self, input: Callable[
        [Request,
         Callable[[str, Response], None],
         Callable[[str, Exception], None]
         ], None]) -> None:
        self._call = input
        self._on: Dict[str, Any] = {}

    def on(self, channel: str, node) -> 'FNode[Request, Response]':
        if channel not in self._on:
            self._on[channel] = []
        self._on[channel].append(node)
        return self

    def _write(self, channel, value):
        if not channel in self._on:
            raise Exception('Missing Node on channel %s' % channel)
        for stream in self._on[channel]:
            stream.run(value)

    def run(self, value: Request):
        self._call(value, self._write, self._write)
