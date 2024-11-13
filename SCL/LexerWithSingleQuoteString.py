import re

# 更新词法单元的正则表达式，包括单引号字符串字面量
token_specification_with_single_quote_string = [
    ('ID',       r'[a-zA-Z_]\w*'), 
    ('NUMBER',   r'\d+\.\d+|\d+'),  # 浮点数或整数
    ('ASSIGN',   r'='),
    ('END',      r';'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('LBRACE',   r'\{'),            # 左花括号
    ('RBRACE',   r'\}'),            # 右花括号
    ('LPAREN',   r'\('),            # 左括号
    ('RPAREN',   r'\)'),            # 右括号
    ('DOT',      r'\.'),            # 点号
    ('STRING',   r'"[^"]*"'),       # 双引号字符串字面量
    ('SINGLE_QUOTE_STRING', r"'[^']*'"),  # 单引号字符串字面量
    ('MISMATCH', r'.')              # 其他字符
]

# 构建包含单引号字符串字面量的正则表达式
token_regex_with_single_quote_string = '|'.join('(?P<%s>%s)' % pair for pair in token_specification_with_single_quote_string)

# 创建包含单引号字符串字面量的词法分析器
def lexer_with_single_quote_string(code):
    pos = 0
    while pos < len(code):
        match = re.match(token_regex_with_single_quote_string, code[pos:])
        if match is not None:
            type = match.lastgroup
            value = match.group(type)
            if type == 'SKIP':
                pass
            elif type == 'NEWLINE':
                pass
            elif type == 'MISMATCH':
                raise RuntimeError(f'Unexpected character {value}')
            else:
                yield type, value
            pos += match.end()
        else:
            yield "error","error"
