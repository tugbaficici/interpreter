
inputString = "n=0;{n-2*5?<n;n=n+1;}"

stack = []

# Main buradan başlamaktadır.
inputToStack()
token = getToken()#global
P()


def inputToStack():
    for i in reversed(range(len(inputString))):
        stack.append(inputString[i])


def getToken():
    top = stack.pop()
    return top


def P():
    if token == ".":
        # program başarılı şekilde sonlandır.
        print("program başarılı");
    else:
        C()  # geri döndüğünde token değişkeninde nokta olmalı global token?


def C():
    # işlem bittiğinde return .
    # C  → I | W | A | Ç | G
    if token == "[":
        token=getToken()
        I()
    elif token == "{":
        W()
    elif token == "<":
        cikis()
    elif token == ">":
        G()
    else:  # token harf ise
        A()
    
    #token="."

def I():
    # if
    # I   → '[' E '?'  C{C} ':' C{C} ']' | '[' E '?' C{C} ']'
    E()#burada her türlü e çağrılacak iki ihtimal için


def W():
    # while
    # W → '{' E '?'  C{C} '}'


def A():
    # atama
    # A  → K '=' E ';'
    

def Cikis():  # def Ç()
    # çıktı
    # Ç  → '<' E ';'


def G():
    # G → '>' K ';'


def E():
    # expression
    # E → T {('+' | '-') T}  t-t t+t
    T()


def T():
    # T → U {('*' | '/' | '%') U} u*u u/u u%u
    U()

def U():
    # U → F '^' U | F
    F()

def F():
    # F → '(' E ')' | K | R
    if token == "(":
        E()
    elif token harf ise:
        K()
    elif token rakam ise:
        R()

def K():
    # harf
    # K → 'a'  |  'b'  | … |  'z'



def R():
    # rakam
    # R → '0'  |  '1'  | … |  '9'
