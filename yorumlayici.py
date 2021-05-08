

def P():
    global islemlerStack
    print("P içinde")
    global token
    if token == ".":
        # program başarılı şekilde sonlandır.
        print("Accept")
    else:
        C()  # geri döndüğünde token değişkeninde nokta olmalı global token?
        print(islemlerStack)
        print(token)
        P()
        


def C():
    print("c içinde")
    global token
    global islemlerStack
    # işlem bittiğinde return .
    # C  → I | W | A | Ç | G
    if token == "[":
        token = getToken()
        I()

    elif token == "{":
        W()

    elif token == "<":
        Cikis()

    elif token == ">":
        G()

    elif kucukHarfMi(token) == True:  # token harf ise
        
        A()
        islemlerStack.pop()
        islemlerStack.append("C")
        print(islemlerStack)
        token=getToken()
        C()

    elif token == '$':
        
        son=islemlerStack.pop()
        son=islemlerStack.pop()
        if(son=='$'):
            token = '.'

    else:
        return "Hata !"


def I():
    global token
    # if
    # I   → '[' E '?'  C{C} ':' C{C} ']' | '[' E '?' C{C} ']'

    E()  # burada her türlü e çağrılacak iki ihtimal için


def W():
    global token
    # while
    # W → '{' E '?'  C{C} '}'
    print("a")


def A():
    print("a içinde")
    global token
    global islemlerStack
    # atama
    # A  → K '=' E ';'
    K()
    token = getToken()
    islemlerStack.append(token)
    if token == "=":
        token = getToken()
        islemlerStack.append(token)
        print(islemlerStack)
        E()
        # elimizde bir sonraki token var 
        print(islemlerStack)
        print(token)
        token = getToken() # noktalı virgülüde çıkarıyoruz
        if token==";":
            islemlerStack.pop()  # E çıktı
            islemlerStack.pop()  # = çıktı
            islemlerStack.pop()  # K çıktı
            islemlerStack.append("A")
            print(islemlerStack)
        else:
            print("atama hatası")
    else:
        print("Atama sembolü eksik")


def Cikis():
    global token  # def Ç()
    # çıktı
    # Ç  → '<' E ';'
    print("")


def G():
    global token
    # G → '>' K ';'
    print("")


def E():
    # E → T {('+' | '-') T}  {-,+,T} 

    global token
    global islemlerStack
    nonTerminal=["+","-"]

    if token in nonTerminal:
        islemlerStack.pop()#+ - çıkardı
        islemlerStack.pop()#son kalan T
        token=getToken()
        islemlerStack.append(token)
        print(islemlerStack)
        E()
    
    else:
        T()
        print(islemlerStack)
        islemlerStack.pop()
        islemlerStack.append("E")
        print(islemlerStack)
        #bir sonraki token + - den farklıysa bu işlem biter ama değilse e yeniden çağırılır
        token=getToken()
        if token in nonTerminal:
            islemlerStack.append(token)
            E()
        else:
            setToken(token)
        



def T():
    # T → U {('*' | '/' | '%') U} u*u u/u u%u
    print("t içinde")
    global token
    global islemlerStack
    
    nonTerminal=["*","/","%"]

    if token in nonTerminal:
        islemlerStack.pop()#+ - çıkardı
        islemlerStack.pop()#son kalan U
        token=getToken()
        islemlerStack.append(token)
        print(islemlerStack)
        T()
    
    else:
        U()
        islemlerStack.pop()
        islemlerStack.append("T")
        print(islemlerStack)
        #bir sonraki token + - den farklıysa bu işlem biter ama değilse e yeniden çağırılır
        token=getToken()
        print(token)
        if token in nonTerminal:
            islemlerStack.append(token)
            T()
        else:
            setToken(token)
        
            

def U():
    print("u içinde")
    global token
    global islemlerStack
    # U → F '^' U | F
    # ihtimal 1 yok
    F() 
    token =getToken()
    if token == "^":
        islemlerStack.pop()# F yi çıkar içerden
        token=getToken()
        islemlerStack.append(token)# yeni gelen eleman
        print(islemlerStack)
        U()
    else:
        setToken(token)
        son = islemlerStack.pop()
        if son == "F":
            islemlerStack.append("U")
            print(islemlerStack)


def F():
    # F → '(' E ')' | K |  R
    print("f içinde")
    global islemlerStack
    global token
   
    print(token)
    print(rakamMi(token))
    
    if rakamMi(token) == True:
        K()
        islemlerStack.pop()
        islemlerStack.append("F")
        print(islemlerStack)
    elif kucukHarfMi(token) == True:
        print("harf")
        R()
        islemlerStack.pop()
        islemlerStack.append("F")
        print(islemlerStack)
    elif token=="(":
        token= getToken()
        islemlerStack.append(token)
        E()
        token=getToken()
        islemlerStack.append(token)
        if(token==")"):
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("F")
            print(islemlerStack) 
    else:
        return "Hata ! Gecersiz string !"


def K():
    print("k içinde")
    global token
    global islemlerStack
    # harf
    # K → 'a'  |  'b'  | … |  'z'
    if kucukHarfMi(token):
        islemlerStack.pop()
        islemlerStack.append("K")
        print(islemlerStack)

    else:
        return False
        # print girilen hatalı


def R():
    print("r içinde")
    global token
    global islemlerStack
    # rakam
    # R → '0'  |  '1'  | … |  '9'
    if rakamMi(token):
        islemlerStack.pop()
        islemlerStack.append("R")
        print(islemlerStack)
    else:
        return False
        # print girilen hatalı


def rakamMi(rakam):
    rakamlarListesi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if rakam in rakamlarListesi:
        return True

    else:
        return False


def kucukHarfMi(harf):
    kucukHarflerListesi = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                           'h', 'i', 'j', 'k', 'l', 'm', 'n',
                           'o', 'p', 'r', 's', 't', 'u', 'v',
                           'y', 'z', 'x', 'w', 'q']

    if harf in kucukHarflerListesi:
        return True

    else:
        return False


def inputToStack():
    global stack
    global inputString
    for i in reversed(range(len(inputString))):
        stack.append(inputString[i])


def getToken():
    global stack
    top = stack.pop()
    return top

def setToken(token):
    global stack
    stack.append(token)


inputString = "n=(5+5)+5;"
inputs="n=0;{n-2*5?<n;n=n+1;}"
islemlerStack = ['$']
stack = ['$']

# Main buradan başlamaktadır.
inputToStack()  # Global tanimlama
token = getToken()
islemlerStack.append(token)

P()
