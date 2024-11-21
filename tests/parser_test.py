import pytest
from app.parser import parse
from app.terms import And, Arrow, Not, Or, Var, Xor, Equal


def test_order():
    assert str(Or(Var('a'), Var('b'))) == str(parse('a|b'))
    assert str(Or(Var('a'), Var('b'))) != str(parse('b|a'))


@pytest.mark.parametrize('expression', [
   '',
   '()',
   '()()',
   'b > ()'
])
def test_empty_parenthesis_sequence(expression):
    with pytest.raises(ValueError):
        parse(expression)


@pytest.mark.parametrize('expression', [
   '(',
   ')',
   '(()',
   '(a',
   ')a > c',
   'b > (',
])
def test_incorrect_parenthesis_sequence(expression):
    with pytest.raises(ValueError):
        parse(expression)


@pytest.mark.parametrize('expression, expected_output', [
   ('a', Var('a')),
   ('!a', Not(Var('a'))),
   ('a > b', Arrow(Var('a'), Var('b'))),
   ('a | b', Or(Var('a'), Var('b'))),
   ('a * b', And(Var('a'), Var('b'))),
   ('a + b', Xor(Var('a'), Var('b'))),
])
def test_base_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize('expression, expected_output', [
   ('!!!a', Not(Not(Not(Var('a'))))),
   (
       '\t(a > b) | (b + d)',
       Or(Arrow(Var('a'), Var('b')), Xor(Var('b'), Var('d')))
   ),
   (
       'a > b * \n(b | c)',
       Arrow(Var('a'), And(Var('b'), Or(Var('b'), Var('c'))))
   ),
   (
       '(a > b) * (b | c)',
       And(Arrow(Var('a'), Var('b')), Or(Var('b'), Var('c')))
   ),
   ('a |\t\t\t b * c', Or(Var('a'), And(Var('b'), Var('c')))),
   (
       '(a > b) * (c | d) + (e * f)',
       Xor(
           And(Arrow(Var('a'), Var('b')), Or(Var('c'), Var('d'))),
           And(Var('e'), Var('f'))
       )
   ),
   (
       '!(a > b) * !(c | d) + !(e * f)',
       Xor(
           And(
               Not(Arrow(Var('a'), Var('b'))),
               Not(Or(Var('c'), Var('d')))
           ),
           Not(And(Var('e'), Var('f')))
       )
   ),
   (
       '!(!a > !b) * (!c | !d) + (!e * !f)',
       Xor(
           And(
               Not(Arrow(Not(Var('a')), Not(Var('b')))),
               Or(Not(Var('c')), Not(Var('d')))
           ),
           And(Not(Var('e')), Not(Var('f')))
       )
   ),
   (
       '(a|b|c|d) * (e|f|g|h) * (i|j|k|l)',
       And(
           And(
               Or(Or(Or(Var('a'), Var('b')), Var('c')), Var('d')),
               Or(Or(Or(Var('e'), Var('f')), Var('g')), Var('h'))
           ),
           Or(Or(Or(Var('i'), Var('j')), Var('k')), Var('l'))
       )
   ),
   (
       '!(a+b) * !(c+d) > !(e+f) * !(g+h)',
       Arrow(
           And(
               Not(Xor(Var('a'), Var('b'))),
               Not(Xor(Var('c'), Var('d')))
           ),
           And(
               Not(Xor(Var('e'), Var('f'))),
               Not(Xor(Var('g'), Var('h')))
           )
       )
   ),
   (
       '!(a=b) * !(c=d) = !(e=f) * !(g=h)',
       Equal(
           And(
               Not(Equal(Var('a'), Var('b'))),
               Not(Equal(Var('c'), Var('d')))
           ),
           And(
               Not(Equal(Var('e'), Var('f'))),
               Not(Equal(Var('g'), Var('h')))
           )
       )
   ),
])
def test_сomplex_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize('expression, expected_output', [
   ('!!!a', Not(Not(Not(Var('a'))))),
   ('!a', Not(Var('a'))),
   ('!(!a)', Not(Not(Var('a')))),
   ('a|!b', Or(Var('a'), Not(Var('b')))),
   ('!(a|b)', Not(Or(Var('a'), Var('b')))),
   ('!a|b', Or(Not(Var('a')), Var('b'))),
])
def test_negation_expressions(expression, expected_output):
    assert str(parse(expression)) == str(expected_output)


@pytest.mark.parametrize('expression', [
   '!A',
   'A > B > л',
   '?',
   'ф | E'
])
def test_invalid_literals(expression):
    with pytest.raises(ValueError):
        parse(expression)
