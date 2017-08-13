
# ============================================================================
# Elastic Event Components - Runtime
# ============================================================================
# http://www.enterstry.de/blog/elastic-event-components-runtime
# ============================================================================

from v3.flow import Flow
from v3 import functions

Flow[int]().node(
    'load', int, str, functions.load).node(
    'show', str, str, functions.show).node(
    'error', Exception, object, functions.error).node(
    'nil', object, object, lambda a, b, c: None). \
    configure_by_file("v3/test.flow").run(1)