import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
def example_program():
    return """
int a = 135;
int b = 25;
intr res1 = a + b;
printf("%i", res1);
float a2 = 2.15;
float b2 = 2.55;
intr res2 = a2 * b2;
printf("%f", res2);
int x = 3;
switch(x) {
    case 1:
        printf("One");
        break;
    case 2:
        printf("Two");
        break;
    case 3:
        printf("Three");
        break;
    default:
        printf("Other");
}
int age;
printf("Enter age: ");
scanf("%i", age);
printf("Age is %i", age);
"""
def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
    else:
        code = example_program()
        print("=== Example Program ===\n")
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse_program()
    interpreter = Interpreter()
    interpreter.interpret(ast)
if __name__ == "__main__":
    main()
