
# ============================================================================
# Elastic Event Components - Erste Gedanken
# ============================================================================
# http://www.enterstry.de/blog/elastic-event-components-konzept
# ============================================================================

# ============================================================================
# INSTALL: install.sh
#
# ACTIVATE VIRTUAL ENVIRONMENT: venv/bin/activate
# ============================================================================
#
# RUN: python app_v1 v1/test.dat
#
# ============================================================================


from v1.stream import Stream
from v1 import functions

parse = Stream(functions.func_parse)
load_file = Stream(functions.func_load_file)
error = Stream(functions.func_error)
print_content = Stream(lambda stream: print(stream.read()))

parse.on(
    'OUT', load_file).on(
    'ERR', error)

load_file.on(
    'OUT', print_content).on(
    'ERR', error)

parse.run(None)
