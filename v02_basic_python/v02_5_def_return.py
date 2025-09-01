# pyfigel + termcolor 를 적용한 함수!
import pyfiglet
from termcolor import colored

# 함수 정의
def decorate_text(text : str, color : str):
    '''
    함수 설명 : 1. 폰트 적용 2. 색상 적용 3. 출력
    매개 변수 : 1. text(str) 2. color(str)
    '''
    py_sentence = pyfiglet.figlet_format(text)
    decorate_sentence = colored(py_sentence, color, "on_white", ['bold', 'blink'])
    # print(decorate_sentence)
    return decorate_sentence
    
# 출력
result1 = decorate_text("PINK", (255, 105, 180))
result2 = decorate_text("YELLOW", "yellow")
print("\n꾸미기 결과:" + result1 + result2)