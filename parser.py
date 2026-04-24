from tokens import TokenType
from ast_nodes import *
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    def current(self):
        return self.tokens[self.pos]
    def eat(self, token_type):
        if self.current().type == token_type:
            self.pos += 1
            return True
        return False
    def expect(self, token_type):
        if self.current().type == token_type:
            token = self.current()
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {token_type}, got {self.current().type}")
    def parse_program(self):
        stmts = []
        while self.current().type != TokenType.EOF:
            stmts.append(self.parse_statement())
        return Program(stmts)
    def parse_statement(self):
        token = self.current()
        if token.type in [TokenType.INT, TokenType.FLOAT, TokenType.INTR]:
            return self.parse_declaration()
        elif token.type == TokenType.PRINTF:
            return self.parse_printf()
        elif token.type == TokenType.SCANF:
            return self.parse_scanf()
        elif token.type == TokenType.SWITCH:
            return self.parse_switch()
        elif token.type == TokenType.IDENTIFIER:
            return self.parse_assignment()
        elif token.type == Token.Type.TUER:
            return self.parse_assignment()
        else:
            return self.parse_tuer()
    def parse_declaration(self):
        var_type = self.current().type.name.lower()
        self.pos += 1
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return Declaration(var_type, name, value)
    def parse_assignment(self):
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return Declaration(None, name, value)  
    def parse_printf(self):
        self.eat(TokenType.PRINTF)
        self.expect(TokenType.LPAREN)
        format_str = self.expect(TokenType.STRING).value
        args = []
        if self.current().type == TokenType.COMMA:
            self.eat(TokenType.COMMA)
            args.append(self.parse_expression())
            while self.current().type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                args.append(self.parse_expression())
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)
        return Printf(format_str, args)
    def parse_scanf(self):
        self.eat(TokenType.SCANF)
        self.expect(TokenType.LPAREN)
        format_str = self.expect(TokenType.STRING).value
        args = []
        if self.current().type == TokenType.COMMA:
            self.eat(TokenType.COMMA)
            args.append(self.expect(TokenType.IDENTIFIER).value)
            while self.current().type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                args.append(self.expect(TokenType.IDENTIFIER).value)
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)
        return Scanf(format_str, args)
    def parse_switch(self):
        self.eat(TokenType.SWITCH)
        self.expect(TokenType.LPAREN)
        expr = self.parse_expression()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.LBRACE)
        cases = []
        default = None
        while self.current().type != TokenType.RBRACE:
            if self.current().type == TokenType.CASE:
                self.eat(TokenType.CASE)
                value_token = self.expect(TokenType.NUMBER)
                self.expect(TokenType.COLON)
                body = []
                while self.current().type not in [TokenType.CASE, TokenType.DEFAULT, TokenType.RBRACE]:
                    body.append(self.parse_statement())
                cases.append(Case(value_token.value, body))
            elif self.current().type == TokenType.DEFAULT:
                self.eat(TokenType.DEFAULT)
                self.expect(TokenType.COLON)
                body = []
                while self.current().type not in [TokenType.CASE, TokenType.DEFAULT, TokenType.RBRACE]:
                    body.append(self.parse_statement())
                default = body
            else:
                raise SyntaxError("Expected case or default")
        self.expect(TokenType.RBRACE)
        return Switch(expr, cases, default)
    def parse_expression(self):
        return self.parse_add_sub()
    def parse_add_sub(self):
        left = self.parse_mul_div()
        while self.current().type in [TokenType.PLUS, TokenType.MINUS]:
            op = self.current()
            self.pos += 1
            right = self.parse_mul_div()
            left = BinaryOp(left, op.type.name, right)
        return left
    def parse_mul_div(self):
        left = self.parse_primary()
        while self.current().type in [TokenType.MULTIPLY, TokenType.DIVIDE]:
            op = self.current()
            self.pos += 1
            right = self.parse_primary()
            left = BinaryOp(left, op.type.name, right)
        return left
    def parse_primary(self):
        token = self.current()
        if token.type in [TokenType.NUMBER, TokenType.FLOAT_NUMBER]:
            self.pos += 1
            return Number(token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.pos += 1
            return Variable(token.value)
        elif token.type == TokenType.LPAREN:
            self.pos += 1
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
    def parse_tuer(self):
        self.eat(TokenType.TUER)
        self.expect(TokenType.LPAREN)
        format_str = self.expect(TokenType.STRING).value
        self.expect(TokenType.COMMA)
        var_name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)
        return ('tuer', format_str, var_name)
    else:
        raise SyntaxError(f"Unexpected token: {token}")
