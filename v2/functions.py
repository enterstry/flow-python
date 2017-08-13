from typing import Callable


def int_to_str(data: int, output: Callable[[str, str], None]):
    # hier muss nun eine Typenkonvertierung stattfinden,
    # da der Eingang vom Typ Integer und der Ausgang vom Typ String ist.
    print("int_to_str", type(data))
    output('out', str(data))


def str_to_int(data: str, output: Callable[[str, int], None]):
    # hier muss nun eine Typenkonvertierung stattfinden,
    # da der Eingang vom Typ String und der Ausgang vom Typ Integer ist.
    print("str_to_int", type(data))
    output('out', int(data))
