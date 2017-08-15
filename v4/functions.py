from typing import Callable

def load(data: int,
         output: Callable[[str, str], None],
         error: Callable[[str, Exception], None]):
    try:
        print('load', data)
        # TODO: Load data...
        output('out', str(data))
    except Exception as e:
        error('err', e)

def show(data: str,
         output: Callable[[str, str], None],
         error: Callable[[str, Exception], None]):
    try:
        print('show', data)
        # TODO: Load data...
        output('out', "My data...")
    except Exception as e:
        error('err', e)

def error(data: Exception,
          output: Callable[[str, str], None],
          error: Callable[[str, Exception], None]):
    print(data)