
# ============================================================================
# Elastic Event Components - Typensicherheit
# ============================================================================
# http://www.enterstry.de/blog/elastic-event-components-konzept
# ============================================================================

from v2.flow import Flow
from v2 import functions

flow = Flow[int]()
node1 = flow.Node(int, str, functions.int_to_str)
node2 = flow.Node(str, int, functions.str_to_int)
node3 = flow.Node(int, str, lambda data, _: print(data, type(data)))

node1.on('out', node2)
node2.on('out', node3)

flow.run(1)