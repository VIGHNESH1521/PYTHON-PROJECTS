from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_info


def convert(f):
    c = (f - 32) * 5 / 9
    put_text('The Celsius is :%.1f.' % c)
    put_info("success",closable=True,position=-1)


f = input("Input your Fahrenheit value(cm)：", type=FLOAT)
if __name__ == '__main__':
    convert(f)
