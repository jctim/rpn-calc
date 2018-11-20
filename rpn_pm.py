from functools import reduce
from typing import List 
from pampy import match, TAIL, _ # type: ignore

def calculate(expression: str):
    def calc_stack(stack: List[float], token: str) -> List[float]:
        newStack: List[float] = match((token, stack),
            ('+', [_, _, TAIL]), lambda a, b, tail: [b + a] + tail,
            ('-', [_, _, TAIL]), lambda a, b, tail: [b - a] + tail,
            ('*', [_, _, TAIL]), lambda a, b, tail: [b * a] + tail,
            ('/', [_, _, TAIL]), lambda a, b, tail: [b / a] + tail,
            ('^', [_, _, TAIL]), lambda a, b, tail: [pow(b, a)] + tail,
            (_, list), lambda x, s: [float(x)] + s
        )
        return newStack

    tokens = expression.split()
    res: List[float] = reduce(calc_stack, tokens, [])
    return res[0]

