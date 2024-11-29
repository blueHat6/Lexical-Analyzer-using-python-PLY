from ply.lex import lex

import ply.lex as lex

# Definisi tokens
tokens = (
    'PRINT', 'ID', 'NUMBER', 'IF', 'ELSE', 'FUNCTION',
    'ASSIGN', 'PLUS', 'MINUS', 'LPAREN', 'RPAREN',
    'LCURLY', 'RCURLY', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
    'COMMA', 'STRING'
)

# Keyword yang dipesan
reserved = {
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'function': 'FUNCTION'
}

# Regular expression untuk simbol dan operator
t_ASSIGN = r'<-'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_COMMA = r','
t_ignore = ' \t'

# Token untuk ID (identifier) dan keyword
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Periksa apakah ID adalah keyword
    return t

# Token untuk angka
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Token untuk string
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

# Token untuk newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Penanganan karakter ilegal
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Buat lexer
lexer = lex.lex()

# Contoh data input R-script-like
data = '''
x <- 1
y <- 100
print("List of Odd Numbers 1-100:")
for (i in seq(x, y)) {
  if (i %% 2 != 0) {
    print(i)
  }
}
'''

# Masukkan data ke lexer
lexer.input(data)

# Ambil dan cetak token satu per satu
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{tok.type}: {tok.value}")