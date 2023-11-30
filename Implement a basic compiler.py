# Implement a basic compiler (Lexer and Parser)
import re

def lexer(program):
    tokens = re.findall(r'\b\w+\b|[\(\)\{\};]', program)
    return [token.strip() for token in tokens]

def parser(tokens):
    if tokens[0] == 'int' and tokens[2] == ';':
        return ('declaration', tokens[1])
    elif tokens[0] == 'if' and tokens[2] == '{' and tokens[4] == '}':
        return ('if_statement', tokens[1])
    else:
        return ('unknown',)

# Example usage:
program_code = "int x;"
tokens = lexer(program_code)
print("Tokens:", tokens)

parsed_result = parser(tokens)
print("Parsed result:", parsed_result)