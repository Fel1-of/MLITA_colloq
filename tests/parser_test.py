import pytest

from app.parser import parse
from app.terms import And, Arrow, Not, Or, Var, Xor


def test_order():
    assert str(Or(Var('A'), Var('B'))) == str(parse('A|B'))
    assert str(Or(Var('A'), Var('B'))) != str(parse('B|A'))


@pytest.mark.parametrize('expression', ['', '()', '()()', 'b > ()'])
def test_empty_parenthesis_sequence(expression):
    with pytest.raises(ValueError):
        parse(expression)


@pytest.mark.parametrize(
    'expression',
    [
        '(',
        ')',
        '(()',
        '(a',
        ')a > c',
        'b > (',
    ],
)
def test_incorrect_parenthesis_sequence(expression):
    with pytest.raises(ValueError):
        parse(expression)


@pytest.mark.parametrize(
    'expression, expected_output',
    [
        ('A', Var('A')),
        ('!A', Not(Var('A'))),
        ('A > B', Arrow(Var('A'), Var('B'))),
        ('A | B', Or(Var('A'), Var('B'))),
        ('A * B', And(Var('A'), Var('B'))),
        ('A + B', Xor(Var('A'), Var('B'))),
    ],
)
def test_base_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize(
    'expression, expected_output',
    [
        ('!!!A', Not(Not(Not(Var('A'))))),
        (
            '(A > B) | (B + D)',
            Or(Arrow(Var('A'), Var('B')), Xor(Var('B'), Var('D'))),
        ),
        (
            'A > B * (B | C)',
            Arrow(Var('A'), And(Var('B'), Or(Var('B'), Var('C')))),
        ),
        (
            '(A > B) * (B | C)',
            And(Arrow(Var('A'), Var('B')), Or(Var('B'), Var('C'))),
        ),
        ('A | B * C', Or(Var('A'), And(Var('B'), Var('C')))),
    ],
)
def test_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize(
    'expression, expected_output',
    [
        ('!!!A', Not(Not(Not(Var('A'))))),
        ('!A', Not(Var('A'))),
        ('!(!A)', Not(Not(Var('A')))),
        ('A|!B', Or(Var('A'), Not(Var('B')))),
        ('!(A|B)', Not(Or(Var('A'), Var('B')))),
        ('!A|B', Or(Not(Var('A')), Var('B'))),
    ],
)
def test_negation_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize(
    'expression, expected_output',
    [
        (  # A1
            '(A > (B > C)) > ((A > B) > (A > C))',
            Arrow(
                Arrow(Var('A'), Arrow(Var('B'), Var('C'))),
                Arrow(Arrow(Var('A'), Var('B')), Arrow(Var('A'), Var('C'))),
            ),
        ),
        (  # A2
            'A > (B > A)',
            Arrow(Var('A'), Arrow(Var('B'), Var('A'))),
        ),
        (  # A3
            '(!B > !A) > ((!B > A) > B)',
            Arrow(
                Arrow(Not(Var('B')), Not(Var('A'))),
                Arrow(Arrow(Not(Var('B')), Var('A')), Var('B')),
            ),
        ),
        (  # A4
            'A * B > A',
            Arrow(And(Var('A'), Var('B')), Var('A')),
        ),
        (  # A5
            'A * B > B',
            Arrow(And(Var('A'), Var('B')), Var('B')),
        ),
        (  # A6
            'A > (B > (A * B))',
            Arrow(Var('A'), Arrow(Var('B'), And(Var('A'), Var('B')))),
        ),
        (  # A7
            'A > (A | B)',
            Arrow(Var('A'), Or(Var('A'), Var('B'))),
        ),
        (  # A8
            'B > (A | B)',
            Arrow(Var('B'), Or(Var('A'), Var('B'))),
        ),
        (  # A9
            '(A > C) > ((B > C) > ((A | B) > C))',
            Arrow(
                Arrow(Var('A'), Var('C')),
                Arrow(
                    Arrow(Var('B'), Var('C')),
                    Arrow(Or(Var('A'), Var('B')), Var('C')),
                ),
            ),
        ),
        (  # A10
            '!A > (A > B)',
            Arrow(Not(Var('A')), Arrow(Var('A'), Var('B'))),
        ),
        (  # A11
            'A | !A',
            Or(Var('A'), Not(Var('A'))),
        ),
    ],
)
def test_axioms(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)
