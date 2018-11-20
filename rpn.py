from functools import reduce
from typing import List, Dict, Callable, Any
from operator import add, sub, mul, truediv, pow

_operations: Dict[str, Callable[[Any, Any], Any]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "^": pow
}


def calculate(expression: str):
    def calc_stack(stack: List[float], token: str) -> List[float]:
        if token in _operations:
            h1 = stack.pop()
            h2 = stack.pop()
            res = _operations[token](h2, h1)
            stack.append(res)
        else:
            stack.append(float(token))
        return stack

    tokens = expression.split()
    res: List[float] = reduce(calc_stack, tokens, [])
    return res[0]

