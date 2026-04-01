from Enum import Enum, auto 
from datac classes import dataclass
#class
class TokenType(Enum):
  INT = auto()
  FLOAT = auto()
  INTR = auto()
  SWITCH = auto()
  CASE = auto()
  DEFAULT = auto()
  BREAK = auto()
  PRINTF = auto()
  SCANF = auto()
  PLUS = auto()
  MINUS = auto()
  DIVISION = auto()
  MULTIPLY = auto()
  DIVIDE = auto()
  ASSIGH = auto()
  EQUALS = auto()
  LPAPEN = auto()
  RPAREN = auto()
  SEMICOLON = auto()
  COMMA = auto()
  COLON = auto()
  NUMBER = auto()
  FLOAT_NUMBER = auto()
  IDENTIFIER = auto()
  STRING = auto()
  EOF = auto()
#burger
@dataclass
class Token:
  type: TokenType
  line: int
  collum: int
