from typing import Callable

def load(data: int,
         output: Callable[[str, str], None],
         error: Callable[[str, Exception], None]):
    try:
        print('load')
        # TODO: Load data...
        output('OUT', str(data))
    except Exception as e:
        error('ERR', e)

def show(data: str,
         output: Callable[[str, str], None],
         error: Callable[[str, Exception], None]):
    try:
        print('show')
        # TODO: Load data...
        output('OUT', data)
    except Exception as e:
        error('ERR', e)

def error(data: Exception,
          output: Callable[[str, str], None],
          error: Callable[[str, Exception], None]):
    print(data)