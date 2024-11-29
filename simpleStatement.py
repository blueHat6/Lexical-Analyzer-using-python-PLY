import ply.lex as lex

tokens = (
    'PROGRAM', 'IDENTIFIER', 'BEGIN', 'END', 'WRITELN', 'SEMICOLON', 'STRING'
)

t_ignore = ' \t'  
t_SEMICOLON = r';'
t_STRING = r'\'[^\']*\''  

def t_PROGRAM(t):
    r'PROGRAM'
    return t

def t_BEGIN(t):
    r'BEGIN'
    return t

def t_END(t):
    r'END\.'
    return t

def t_WRITELN(t):
    r'WRITELN'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Karakter tidak dikenal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data = """
PROGRAM HELLOWORLD;
BEGIN
    WRITELN('Hello, world!');
END.
"""

lexer.input(data)

print("Hasil Tokenisasi:")
for tok in lexer:
    print(tok)
