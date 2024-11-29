from ply.lex import lex

# Daftar token
tokens = (
    'NUMBER',    
    'ID',        
    'ASSIGN',    
    'PLUS',      
    'MINUS',    
    'TIMES',     
    'DIVIDE',    
    'MODULO',    
    'LPAREN',    
    'RPAREN',    
    'LCURLY',    
    'RCURLY',    
    'SEMICOLON', 
    'CAT',       
    'WHILE',     
    'IF',        
)

t_ASSIGN    = r'<-'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MODULO    = r'%%'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LCURLY    = r'\{'
t_RCURLY    = r'\}'
t_SEMICOLON = r';'

reserved = {
    'cat': 'CAT',
    'while': 'WHILE',
    'if': 'IF',
}


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Cek jika identifier adalah keyword
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

source_code = """
cat("List of Odd Number 1-100: \n")
num <- 1
while (num <= 100) {
    sisa <- (num %% 2)
    if (sisa != 0) {
        oddnum <- num
        cat(oddnum, "  ")
    }
    num <- num + 1
}
"""

lexer.input(source_code)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
