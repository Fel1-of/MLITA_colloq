from typing import Tuple, List, Optional, Union
from string import ascii_lowercase
from .terms import (
    Term, Var, Arrow, And, Or, Not, Xor, Equal,
)


precedence = {
    '!': 4,
    '*': 3,
    '|': 2,
    '+': 1,
    '>': 0,
    '=': -1,
}

binary_operator = {
    '!': Not,
    '|': Or,
    '*': And,
    '+': Xor,
    '>': Arrow,
    '=': Equal,
}


def get_next_token(s: str) -> Tuple[Optional[Union[str, Var]], str]:
    if not s:
        return None, s
    if s[0] in precedence:
        return s[0], s[1:]
    if s[0] in ascii_lowercase:
        var = s[0]
        return Var(var), s[1:]
    if s[0] in '()':
        return s[0], s[1:]
    raise ValueError(f'Unexpected character: {s[0]}')


def process_operator(op: str, output: List[Term]) -> None:
    if op == '!':
        operand = output.pop() if output else None
        if operand is None:
            raise ValueError('Invalid expression: empty operand')
        output.append(Not(operand))
    else:
        right = output.pop() if output else None
        left = output.pop() if output else None
        if left is None or right is None:
            raise ValueError('Invalid expression: empty operand')
        output.append(binary_operator[op](left, right))


def parse(s: str) -> Term:
    s = s.replace(' ', '').replace('\t', '').replace('\n', '')
    stack: List[str] = []
    output: List[Term] = []

    while s:
        token, s = get_next_token(s)
        if token is None:
            break
        if isinstance(token, Var):
            output.append(token)
        elif token in '(!':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                op = stack.pop()
                process_operator(op, output)
            if not stack or stack[-1] != '(':
                raise ValueError('Mismatched parentheses')
            stack.pop()
            while stack and stack[-1] == '!':
                op = stack.pop()
                operand = output.pop() if output else None
                if operand is None:
                    raise ValueError('Invalid expression: empty operand')
                output.append(Not(operand))
        else:
            while (stack and
                   stack[-1] != '(' and
                   precedence.get(stack[-1], -1) >= precedence[token]):
                op = stack.pop()
                process_operator(op, output)
            stack.append(token)

    while stack:
        op = stack.pop()
        process_operator(op, output)

    if len(output) != 1:
        raise ValueError('Invalid expression')
    return output[0]
