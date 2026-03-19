import ply.lex as lex
import ply.yacc as yacc

# ---------------- LEXER ---------------- #

tokens = ['ID', 'NUMBER', 'EQUALS', 'DOT']

reserved = {
    'DELETE': 'DELETE',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'JOIN': 'JOIN',
    'ON': 'ON',
    'SELECT': 'SELECT',
    'GROUP': 'GROUP',
    'BY': 'BY'
}

tokens = tokens + list(reserved.values())

t_EQUALS = r'='
t_DOT = r'\.'
t_ignore = ' \t'

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise Exception(f"Invalid symbol '{t.value[0]}' at position {t.lexpos}")

lexer = lex.lex()

# ---------------- PARSER ---------------- #

def p_statement(p):
    '''statement : delete_statement
                 | join_statement
                 | groupby_statement'''
    p[0] = p[1]

def p_delete_statement(p):
    'delete_statement : DELETE FROM ID WHERE condition'
    p[0] = ('DELETE', p[3], p[5])

def p_condition(p):
    '''condition : ID EQUALS NUMBER
                 | ID EQUALS ID'''
    p[0] = (p[1], p[2], p[3])

def p_join_statement(p):
    'join_statement : ID JOIN ID ON condition'
    p[0] = ('JOIN', p[1], p[3], p[5])

def p_groupby_statement(p):
    'groupby_statement : SELECT ID FROM ID GROUP BY ID'
    p[0] = ('GROUP_BY', p[2], p[4], p[7])

def p_error(p):
    if p:
        raise Exception(f"Syntax error near '{p.value}'")
    else:
        raise Exception("Syntax error at end of input")

parser = yacc.yacc()

# ---------------- HELPER FUNCTION ---------------- #

def parse_query(query):
    lexer.input(query)
    list(lexer)  # Force lexing errors
    return parser.parse(query)
