# MLITA_colloq

[![Coverage Status](https://coveralls.io/repos/github/Fel1-of/MLITA_colloq/badge.svg?branch=main)](https://coveralls.io/github/Fel1-of/MLITA_colloq?branch=main)

Задание 1.

Была разработана система классов для работы с логичискими выражениями и очелевеченного их вывода. 

```mermaid
classDiagram

class Term {
  <<Interface>>
  +__str__() str*
  +__copy__() Term*
  +__deepcopy__(memo) Term*
  +humanize() str*
  +to_implication_view() Term*
  +substitute(**kwargs) Term*
  +get_substitution_map(other) dict*
  +unify(alphabet) Term*
  +vars() OrderedSet[str]*
}

class Operator {
  <<Abstract>>
  +__copy__() Term*
  +__deepcopy__(memo) Term*
  +__eq__(other) bool
  +substitute(**kwargs) Term
  +get_substitution_map(other) dict*
  +unify(alphabet) Term*
  +vars() OrderedSet[str]*
}

class NullaryOperator {
  <<Abstract>>
  +constructor()
}

class UnaryOperator {
  <<Abstract>>
  +arg : Term
}

class BinaryOperator {
  <<Abstract>>
  +arg1 : Term
  +arg2 : Term
}

class Var {
  +name : str
  +__str__() str
  +substitute(**kwargs) Term
  +humanize() str
  +vars() OrderedSet[str]
  +unify(alphabet) Term
}

class Not {
  +to_implication_view() Not
  +humanize() str
}

class And {
  +to_implication_view() Not
  +humanize() str
}

class Or {
  +to_implication_view() Arrow
  +humanize() str
}

class Xor {
  +to_implication_view() Not
  +humanize() str
}

class Arrow {
  +to_implication_view() Arrow
  +humanize() str
}

class Equal {
  +to_implication_view() Not
  +humanize() str
}

Term <|.. Operator
Operator <|.. NullaryOperator
Operator <|.. UnaryOperator
Operator <|.. BinaryOperator
Term <|.. Var
UnaryOperator <|.. Not
BinaryOperator <|.. And
BinaryOperator <|.. Or
BinaryOperator <|.. Xor
BinaryOperator <|.. Arrow
BinaryOperator <|.. Equal
```

Произведена попытка реализовать программу, выводящую все выражения из исходных. К сожалению удалось вывести лишь А11: A∨¬A(преобразовано к !A->!A).


Протокол вывода А11.
