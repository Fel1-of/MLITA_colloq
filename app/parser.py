from .terms import (
    Term,
    Var,
    Arrow,
    And,
    Or,
    Not,
    Xor,
    Equal
)

precedence = {
    '!': 4,
    '*': 3,
    '|': 2,
    '+': 1,
    '>': 0,
    '=': -1,
}


def get_next_token(s):
    if not s:
        return None, s

    if s[0] in precedence:
        return s[0], s[1:]

    if s[0].isalnum():
        var = s[0]
        return Var(var), s[1:]

    if s[0] == '(':
        return '(', s[1:]

    if s[0] == ')':
        return ')', s[1:]

    raise ValueError(f'Unexpected character: {s[0]}')


def parse(string: str) -> Term:
    s = string.replace(' ', '')
    stack = []
    output = []

    while s:
        token, s = get_next_token(s)
        if token is None:
            break

        if isinstance(token, Var):
            output.append(token)
        elif token == '!':
            operand = output.pop() if output else None
            output.append(Not(operand))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                op = stack.pop()
                right = output.pop() if output else None
                left = output.pop() if output else None
                if left is None or right is None:
                    raise ValueError('Invalid expression: empty operand')
                if op == '*':
                    output.append(And(left, right))
                elif op == '|':
                    output.append(Or(left, right))
                elif op == '+':
                    output.append(Xor(left, right))
                elif op == '>':
                    output.append(Arrow(left, right))
                elif op == '=':
                    output.append(Equal(left, right))
            if not stack or stack[-1] != '(':
                raise ValueError('Mismatched parentheses')
            stack.pop()

            if not output or (len(output) > 0 and isinstance(output[-1], Not)):
                raise ValueError('Invalid expression: empty parentheses')

        else:
            while stack and precedence.get(stack[-1], -1) >= precedence[token]:
                op = stack.pop()
                right = output.pop() if output else None
                left = output.pop() if output else None
                if left is None or right is None:
                    raise ValueError('Invalid expression: empty operand')
                if op == '*':
                    output.append(And(left, right))
                elif op == '|':
                    output.append(Or(left, right))
                elif op == '+':
                    output.append(Xor(left, right))
                elif op == '>':
                    output.append(Arrow(left, right))
                elif op == '=':
                    output.append(Equal(left, right))
            stack.append(token)

    while stack:
        op = stack.pop()
        right = output.pop() if output else None
        left = output.pop() if output else None
        if left is None or right is None:
            raise ValueError('Invalid expression: empty operand')
        if op == '*':
            output.append(And(left, right))
        elif op == '|':
            output.append(Or(left, right))
        elif op == '+':
            output.append(Xor(left, right))
        elif op == '>':
            output.append(Arrow(left, right))
        elif op == '=':
            output.append(Equal(left, right))

    if len(output) != 1:
        raise ValueError('Invalid expression')

    return output[0]
