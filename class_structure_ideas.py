from abc import ABC, abstractmethod


class Term(ABC):
    '''Term interface (abstract class) for all logic expressions'''

    @abstractmethod
    def to_CDN(self) -> 'Term':
        '''Returns an equivalent term using only conjunction, disjunction and negation'''
        return self
    
    @abstractmethod
    def to_IN(self) -> 'Term':
        '''Returns an equivalent term using only implication and negation'''
        return self
    
    @abstractmethod
    def substitute(self, **kwargs: dict[str, 'Term']) -> 'Term':
        pass

    # Будет надо для резолюции
    # @abstractmethod
    # def evaluate(self, **kwargs: dict[str, bool]) -> bool:
    #    pass

    @abstractmethod
    def humanize(self) -> str:
        return ''
    
    @abstractmethod
    def __str__(self) -> str:
        return ''


class Literal(Term):
    '''Boolean variable class'''
    def __init__(self, char: str):
        self.name = char

    def substitute(self, **kwargs: dict[str, Term]) -> Term:
        return kwargs.get(self.name, self.copy())
    
    def copy(self) -> 'Literal':
        return Literal(self.name)

class Operator(Term):
    '''Boolean function abstract class'''
    def __init__(self, *args: Term | str) -> None:
        self.args = []
        for arg in args:
            if isinstance(arg, Term):
                self.append(arg)
                continue
            if isinstance(arg, str):
                self.args.append(Literal(arg))
                continue
            raise TypeError(f'Operator argument must be Term or str')
    
    
    def substitute(self, **kwargs: dict[str, 'Term']) -> Term:
        return Operator(arg.substitute(**kwargs) for arg in self.args)

class NullaryOperator(Operator):
    def __init__(self):
        super().__init__()

class UnaryOperator(Operator):
    def __init__(self, arg: Term) -> None:
        self().__init__(arg)
        self.arg = self.args[0]

class BinaryOperator(Operator):
    def __init__(self, arg1: Term, arg2: Term) -> None:
        super().__init__(arg1, arg2)
        self.arg1 = self.args[0]
        self.arg2 = self.args[1]

class VariadicOperator(Operator):
    '''Boolean functions with two or more arguments (all associative functions, exaple: conjunction, XOR)'''
    def __init__(self, *args):
        if len(args) < 2:
            raise TypeError('Variadic operator need at least 2 arguments')
        super().__init__(*args)

'''
@dataclass
class info_modus:
    input: [Term]
    modus: str
    output: Term

class Method:
    name: str
    def value()
    def info() -> info_modus

class ModusPenis(Method):
    ...

class Solver(ISolver):
    def __init__(methods: Methods)
    def prove()
        method.

class Solver(ISolver):
    def modus_penis() -> dict[input]
'''

def cnf(term: Term) -> Term:
    pass

def dnf(term: Term) -> Term:
    pass

def parse(string: str) -> Term:
    pass

