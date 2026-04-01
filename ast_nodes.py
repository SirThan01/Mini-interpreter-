from dataclasses import dataclass
from typing import List, Any, Optional
#niggre
@dataclass
class Node:
    pass

@dataclass
class Number(Node):
    value: Any

@dataclass
class Variable(Node):
    name: str

@dataclass
class BinaryOp(Node):
    left: Node
    op: str
    right: Node

@dataclass
class Declaration(Node):
    var_type: str 
    name: str
    value: Optional[Node]

@dataclass
class Printf(Node):
    format_str: str
    args: List[Node]

@dataclass
class Scanf(Node):
    format_str: str
    args: List[str]

@dataclass
class Switch(Node):
    expr: Node
    cases: List['Case']
    default: Optional[List[Node]]

@dataclass
class Case(Node):
    value: Any
    body: List[Node]

@dataclass
class Program(Node):
    statements: List[Node]
