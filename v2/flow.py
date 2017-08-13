from typing import Callable, TypeVar, Generic, Type
from .fnode import FNode

Value = TypeVar('Value')
Request = TypeVar('Request')
Response = TypeVar('Response')

class Flow(Generic[Value]):
    def __init__(self):
        self.start_node = None

    def Node(self, req: Type[Request], res: Type[Response], input: Callable[[Request, Callable[[str, Response], None]], None]) -> FNode[Request, Response]:
        node = FNode[Request, Response](input)
        self.start_node = self.start_node or node
        return node

    def run(self, value: Value = None):
        self.start_node.run(value)