from ast_nodes import *
#burger nnnfhjgs
class Interpreter:
    def __init__(self):
        self.variables = {}
        self.types = {}
    def interpret(self, node):
        if isinstance(node, Program):
            return self.visit_program(node)
        elif isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, BinaryOp):
            return self.visit_binary_op(node)
        elif isinstance(node, Declaration):
            return self.visit_declaration(node)
        elif isinstance(node, Printf):
            return self.visit_printf(node)
        elif isinstance(node, Scanf):
            return self.visit_scanf(node)
        elif isinstance(node, Switch):
            return self.visit_switch(node)
    def visit_program(self, node):
        for stmt in node.statements:
            self.interpret(stmt)
    def visit_number(self, node):
        return node.value
    def visit_variable(self, node):
        if node.name not in self.variables:
            raise NameError(f"Variable '{node.name}' not defined")
        return self.variables[node.name]
    def visit_binary_op(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)
        if node.op == 'PLUS':
            return left + right
        elif node.op == 'MINUS':
            return left - right
        elif node.op == 'MULTIPLY':
            return left * right
        elif node.op == 'DIVIDE':
            return left / right
    def visit_declaration(self, node):
        value = self.interpret(node.value)
        if node.var_type:
            if node.var_type == 'int':
                value = int(value)
            elif node.var_type == 'float':
                value = float(value)
            # intr stores result but keeps original type
        self.variables[node.name] = value
        if node.var_type:
            self.types[node.name] = node.var_type
        return value
    def visit_printf(self, node):
        values = [self.interpret(arg) for arg in node.args]
        result = node.format_str
        for i, val in enumerate(values):
            if '%i' in result:
                result = result.replace('%i', str(int(val)), 1)
            elif '%f' in result:
                result = result.replace('%f', str(float(val)), 1)
        print(result, end='')
        return None
    def visit_scanf(self, node):
        for var_name in node.args:
            if var_name not in self.variables:
                raise NameError(f"Variable '{var_name}' not defined")
            if '%i' in node.format_str:
                val = int(input())
                self.variables[var_name] = val
            elif '%f' in node.format_str:
                val = float(input())
                self.variables[var_name] = val
        return None
    def visit_switch(self, node):
        expr_val = self.interpret(node.expr)
        for case in node.cases:
            if expr_val == case.value:
                for stmt in case.body:
                    self.interpret(stmt)
                break
        else:
            if node.default:
                for stmt in node.default:
                    self.interpret(stmt) 
        return None
