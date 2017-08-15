from typing import Callable, Generic, Dict, List, TypeVar, Type
from .fnode import FNode
from .result import Result

Request = TypeVar('Request')
Response = TypeVar('Response')
Value = TypeVar('Value')

ALL = '*'
RUN = '.run'
END = '.'
EDGE = '--'
COMMENT = '//'

class Flow(Generic[Value]):
    def __init__(self):
        self.nodes: Dict[str, FNode] = {}
        self.result = Result()
        self.start_nodes: List[FNode] = []
        self.end_node = self.Node(END, object, Exception, self.result.run)

    def configure(self, lines: List[str]) -> 'Flow[Request, Response]':
        for line in lines:
            line = line.replace('\n', '').replace(' ', '').strip()
            if not line or line.startswith(COMMENT):
                continue

            output, input_name = line.split(EDGE)
            output_name, output_channel = output.split('.', 1)

            if output_channel == RUN:
                self.start_nodes.append(self.nodes[input_name])
            elif output_name == ALL:
                self._connect_all(output_channel, self.nodes[input_name])
            else:
                self.nodes[output_name].on(
                    output_channel, self.nodes[input_name])
        return self

    def _connect_all(self, output_channel: str, input_node: FNode[Request, Response]):
        for node in self.nodes.values():
            if node is not input_node:
                node.on(output_channel, input_node)

    def configure_by_file(self, filename: str) -> 'Flow[Value]':
        with open(filename, 'r') as f:
            return self.configure(f.readlines())

    def Node(self, name: str, s: Type[Request], t: Type[Response],
             input: Callable[[Request, Callable[[str, Response], None], Callable[
                 [str, Exception], None]], None]) -> 'FNode[Request, Response]':
        node = FNode[Request, Response](input)
        self.nodes[name] = node
        return node

    def run(self, value: Request = None) -> Response:
        for node in self.start_nodes:
            node.run(value)
        return self.result.value

    def run_callback(self, value: Request = None, result: Callable[[Response], None] = None):
        self.result.value_callback = result
        for node in self.start_nodes:
            node.run(value)