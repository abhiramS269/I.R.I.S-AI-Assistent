import re
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def find_syntax_error(code):
    try:
        compile(code, filename='<string>', mode='exec')
        print(Fore.BLACK+Back.WHITE+"No syntax errors found.")
    except SyntaxError as e:
        #print(f"Syntax error found in line {e.lineno}:")
        # print(e.text)
        # print(" " * (e.offset - 1) + "^")
        # print(e)
        return e.lineno
    return None
#filter python code for gpt responce
def Filter(txt):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, txt, re.DOTALL)

    if matches:
        python_code = matches[0].strip()
        return python_code
    else:
        return None

def CodeFilter(txt:str):
    
    if "python\nCopy code" in txt:
        txt=txt[txt.find("python\nCopy code"):]
        code=txt.splitlines()
        code=code[code.index("Copy code")+1:]
        txtCode=""
        for i in code:
            txtCode+=f"{i}\n"
        while 1:
            this=find_syntax_error(txtCode)
            if this is None:
                break
            else:
                code=code[:this-1]
                txtCode=""
                for i in code:
                    txtCode+=f"{i}\n"
        return txtCode
    else:
        return None
