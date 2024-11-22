from app.terms import Arrow, Not, Var

A = Var('A')
B = Var('B')
C = Var('C')

A1 = Arrow(A, Arrow(B, A))
A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))


modus_ponens_axioms = [A1, A2, A3]
