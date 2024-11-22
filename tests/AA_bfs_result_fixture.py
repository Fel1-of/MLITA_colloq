import pytest
from app.terms import Arrow, Var
from app.utils.syllogism_result import SyllogismResult


@pytest.fixture()
def AA_bfs_result():
    return [
        SyllogismResult(
            syllogism_name='axiom',
            input_terms=[],
            substitutions=[],
            output_term=Arrow(
                Arrow(Var('a'), Arrow(Var('b'), Var('c'))),
                Arrow(Arrow(Var('a'), Var('b')), Arrow(Var('a'), Var('c'))),
            ),
        ),
        SyllogismResult(
            syllogism_name='axiom',
            input_terms=[],
            substitutions=[],
            output_term=Arrow(Var('a'), Arrow(Var('b'), Var('a'))),
        ),
        SyllogismResult(
            syllogism_name='modus ponens',
            input_terms=[
                SyllogismResult(
                    syllogism_name='axiom',
                    input_terms=[],
                    substitutions=[],
                    output_term=Arrow(Var('a'), Arrow(Var('b'), Var('a'))),
                ),
                SyllogismResult(
                    syllogism_name='axiom',
                    input_terms=[],
                    substitutions=[],
                    output_term=Arrow(
                        Arrow(Var('a'), Arrow(Var('b'), Var('c'))),
                        Arrow(
                            Arrow(Var('a'), Var('b')), Arrow(Var('a'), Var('c'))
                        ),
                    ),
                ),
            ],
            substitutions=[{}, {'a': Var('A'), 'b': Var('B'), 'c': Var('A')}],
            output_term=Arrow(
                Arrow(Var('A'), Var('B')), Arrow(Var('A'), Var('A'))
            ),
        ),
        SyllogismResult(
            syllogism_name='axiom',
            input_terms=[],
            substitutions=[],
            output_term=Arrow(Var('a'), Arrow(Var('b'), Var('a'))),
        ),
        SyllogismResult(
            syllogism_name='modus ponens',
            input_terms=[
                SyllogismResult(
                    syllogism_name='axiom',
                    input_terms=[],
                    substitutions=[],
                    output_term=Arrow(Var('a'), Arrow(Var('b'), Var('a'))),
                ),
                SyllogismResult(
                    syllogism_name='modus ponens',
                    input_terms=[
                        SyllogismResult(
                            syllogism_name='axiom',
                            input_terms=[],
                            substitutions=[],
                            output_term=Arrow(Var('a'), Arrow(Var('b'), Var('a'))),
                        ),
                        SyllogismResult(
                            syllogism_name='axiom',
                            input_terms=[],
                            substitutions=[],
                            output_term=Arrow(
                                Arrow(Var('a'), Arrow(Var('b'), Var('c'))),
                                Arrow(
                                    Arrow(Var('a'), Var('b')),
                                    Arrow(Var('a'), Var('c')),
                                ),
                            ),
                        ),
                    ],
                    substitutions=[
                        {},
                        {'a': Var('A'), 'b': Var('B'), 'c': Var('A')},
                    ],
                    output_term=Arrow(
                        Arrow(Var('A'), Var('B')), Arrow(Var('A'), Var('A'))
                    ),
                ),
            ],
            substitutions=[{}, {'a': Var('A'), 'b': Arrow(Var('B'), Var('A'))}],
            output_term=Arrow(Var('A'), Var('A')),
        ),
    ]
