from typing import Callable, Generic, Dict, List, TypeVar, Type
from .fnode import FNode

Request = TypeVar('Request')
Response = TypeVar('Response')
Value = TypeVar('Value')


class Flow(Generic[Value]):
    def __init__(self):
        self.start_node = None
        self.nodes: Dict[str, FNode] = {}

    def configure(self, lines: List[str]) -> 'Flow[Value]':
        for line in lines:
            line = line.replace('\n', '').replace(' ', '').strip()
            if not line or line.startswith('//'):
                continue
            output, input_name = line.split("--")
            output_name, output_channel = output.split('.')
            self.nodes[output_name].on(
                output_channel, self.nodes[input_name])
        return self

    def configure_by_file(self, filename: str) -> 'Flow[Value]':
        with open(filename, 'r') as f:
            return self.configure(f.readlines())

    def Node(self, name: str, s: Type[Request], t: Type[Response],
             input: Callable[[Request, Callable[[str, Response], None], Callable[
                 [str, Exception], None]], None]) -> 'FNode[Request, Response]':
        node = FNode[Request, Response](input)
        self.nodes[name] = node
        self.start_node = self.start_node or node
        return node

    def node(self,
             name: str, s: Type[Request], t: Type[Response],
             input: Callable[[Request, Callable[[str, Response], None], Callable[
                 [str, Exception], None]], None]) -> 'Flow[Value]':
        self.Node(name, s, t, input)
        return self

    def run(self, value: Value = None):
        self.start_node.run(value)
