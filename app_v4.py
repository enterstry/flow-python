
# ============================================================================
# Elastic Event Components - Nachtrag zur Runtime
# ============================================================================
# http://www.enterstry.de/blog/elastic-event-components-nachtrag-zur-runtime
# ============================================================================

from v4.flow import Flow
from v4 import functions

flow = Flow[int]()
flow.Node('load', int, str, functions.load)
flow.Node('show', str, str, functions.show)
flow.Node('error', Exception, object, functions.error)
flow.Node('nil', object, object, lambda a, b, c: None)
flow.configure_by_file("v4/test.flow")

# gets the result
result = flow.run(1)
print("Return:", result)

# gets the result by callback
flow.run_callback(
    1, lambda result: print('Callback:', result))