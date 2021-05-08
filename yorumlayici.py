inputString = "n=0;{n-2*5?<n;n=n+1;}"
islemlerStack = ['$']
stack = ['$']

# Main buradan başlamaktadır.
inputToStack() # Global tanimlama
token = getToken() 
islemlerStack.append(token)

sonuc = P()
print(sonuc)

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

    P()

def C():
    # işlem bittiğinde return .
    # C  → I | W | A | Ç | G
    if token == "[":
        token=getToken()
        I()

    elif token == "{":
        W()
        cikti += '+' 

    elif token == "<":
        cikis()

    elif token == ">":
        G()

    elif K(token) == True:  # token harf ise
        A()
    
    elif token == '$':
        token == '.'
        P()

    else:
        return "Hata !"

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
    degisken = F()

n = 0
K = E
A  
C
P
def F():
    # F → '(' E ')' | K | R
    global token

    if token == "(":
        E()

    elif K(token) == True:
        return 'K'

    elif R(token) == True:
        return 'R'    
    
    else:
        return "Hata ! Gecersiz string !"

def K(harf):
    # harf
    # K → 'a'  |  'b'  | … |  'z'
    kucukHarflerListesi = ['a','b','c','d','e','f','g',
                           'h','i','j','k','l','m','n',
                           'o','p','r','s','t','u','v',
                           'y','z','x','w','q']

    if harf in kucukHarflerListesi:
        return True
    
    else:
        return False

def R(rakam):
    # rakam
    # R → '0'  |  '1'  | … |  '9'
    rakamlarListesi = [0,1,2,3,4,5,6,7,8,9]

    if rakam in rakamlarListesi:
        return True
    
    else:
        return False