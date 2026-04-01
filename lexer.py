import re
from tokens import Token, TokenType
#niggre
class Lexer:
  def __init__(self, source):
    self.source = source 
    self.pos = 0
    self.line = 1
    self.col = 1
    self.patterns = [
        (r'\d+\.\d+', TokenType.FLOAT_NUMBER),
        (r'\d+', TokenType.NUMBER),
        (r'"[^"]*"', TokenType.STRING),
        (r'int\b', TokenType.INT),
        (r'float\b', TokenType.FLOAT),
        (r'intr\b', TokenType.INTR),
        (r'switch\b', TokenType.SWITCH),
        (r'case\b', TokenType.CASE),
        (r'default\b', TokenType.DEFAULT),
        (r'break\b', TokenType.BREAK),
        (r'printf\b', TokenType.PRINTF),
        (r'scanf\b', TokenType.SCANF),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', TokenType.IDENTIFIER),
        (r'\+', TokenType.PLUS),
        (r'-', TokenType.MINUS),
        (r'\*', TokenType.MULTIPLY),
        (r'/', TokenType.DIVIDE),
        (r'=', TokenType.ASSIGN),
        (r'==', TokenType.EQUALS),
        (r'\(', TokenType.LPAREN),
        (r'\)', TokenType.RPAREN),
        (r'\{', TokenType.LBRACE),
        (r'\}', TokenType.RBRACE),
        (r';', TokenType.SEMICOLON),
        (r',', TokenType.COMMA),
        (r':', TokenType.COLON),
    ]


def next.token(self):
    if self.pos >= len(self.source):
      return Token(TokenType.EOF, None, self.line
, sel.col)
      
      for pattern, token_type in self.patterns:
        regex = re.compile(pattern)
        match = regex.match(self source, self pos)

