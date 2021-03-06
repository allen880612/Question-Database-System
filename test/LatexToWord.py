import latex2mathml.converter
#import pyperclip as pp

def parser_latex(latex_string):
    latex_input = latex_string #latex代码写在这里！！！！！
    mathml_output = latex2mathml.converter.convert(latex_input)
    #pp.copy(mathml_output)
    print(">>",mathml_output)

def main():
    print("欢迎使用latex转mathml程序，输入latex后就可以直接粘贴到word里用了\n")
    while True:
        option = input("请输入要解析的latex的代码:\n>> ")
        if option == 'exit' or option == 'quit':
            print(">> 退出！\n")
            break
        elif option == '':
            print(">> 输入为空\n")
        elif option == 'help' or option == '-h':
            print(">> 将latex代码粘贴过来，回车就可以解析成mathml\n")
        else:
            parser_latex(option)
            print("已经复制好了，去word里粘贴一下吧\n")


def test():
    import hashlib
    import os

    salt = os.urandom(32) # Remember this
    password = 'password123'

    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000, # It is recommended to use at least 100,000 iterations of SHA-256 
        dklen=128 # Get a 128 byte key
    )

    print (key)

if __name__ == '__main__':
    test()

