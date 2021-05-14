
def P():
    global islemlerStack,token
    if token == ".":
        # program başarılı şekilde sonlandır.
        print("Accept")
    else:    
        C()  # geri döndüğünde token değişkeninde nokta olmalı global token?
        P()
        


def C():
    global siralama,token,islemlerStack
    siralama.append("C")
    # işlem bittiğinde return .
    # C  → I | W | A | Ç | G 

    if token == "[":
        token = getToken()
        islemlerStack.append(token)
        I()
        islemlerStack.pop()
        cvarmi=islemlerStack.pop()
        if cvarmi!="C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token=getToken()
        if token != "$":
            islemlerStack.append(token)
        C()

    elif token == "{":
        W()
        islemlerStack.pop()
        cvarmi=islemlerStack.pop()
        if cvarmi!="C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token=getToken()
        if token != "$":
            islemlerStack.append(token)
        C()

    elif token == "<":
        noktaliC()
        islemlerStack.pop()
        cvarmi=islemlerStack.pop()
        if cvarmi!="C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token=getToken()
        C()

    elif token == ">":
        G()
        islemlerStack.pop()
        cvarmi=islemlerStack.pop()
        if cvarmi!="C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token=getToken()
        C()

    elif kucukHarfMi(token) == True:  # token harf ise
        A()
        islemlerStack.pop()
        cvarmi=islemlerStack.pop()
        if cvarmi!="C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
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
    # I   → '[' E '?'  C{C} ':' C{C} ']' 
    # I   → '[' E '?' C{C} ']'
    global siralama,token,islemlerStack
    siralama.append("I")

    E() 
    token=getToken()
    if token == "?":
        islemlerStack.append(token)
        token=getToken()#c
        islemlerStack.append(token)
        C()# tek c geliyo
        if token== ":":
            islemlerStack.append(token)
            token =getToken()#c
            islemlerStack.append(token)
            C()# tek c geliyo
            islemlerStack.append(token)
            #[E?C:C]
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("I")

        elif token=="]":
            #[E?C]
            islemlerStack.append(token)
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("I")

        else:
            print("sembol hatası")

def W():
    # W → '{' E '?'  C{C} '}'
    global siralama,token,islemlerStack
    siralama.append("W")

    token=getToken()
    islemlerStack.append(token)
    E()
    token=getToken()
    if token == "?":
        islemlerStack.append(token)
        token=getToken()#c
        islemlerStack.append(token)
        C()# tek c geliyo
        token=getToken()#}
        islemlerStack.append(token)
        #{E?C}
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.append("W")
        setToken(token)

def A():
    global siralama,token,islemlerStack
    siralama.append("A")
    # atama
    # A  → K '=' E ';'
    K()
    token = getToken()
    islemlerStack.append(token)
    if token == "=":
        token = getToken()
        islemlerStack.append(token)
        E()
        token = getToken() # noktalı virgülüde çıkarıyoruz
        if token==";":
            islemlerStack.pop()  # E çıktı
            islemlerStack.pop()  # = çıktı
            islemlerStack.pop()  # K çıktı
            islemlerStack.append("A")
        else:
            print("atama hatası")
    else:
        print("Atama sembolü eksik")

def noktaliC():# def Ç()
    # Ç  → '<' E ';'
    global siralama,token,islemlerStack
    siralama.append("Ç")

    token= getToken()
    islemlerStack.append(token)
    E()
    islemlerStack.pop()
    islemlerStack.pop()
    islemlerStack.append("Ç")
    token = getToken()#noktalı virgün çıksın
    
def G():
    # G → '>' K ';'
    global siralama,token,islemlerStack
    siralama.append("G")
    
    token= getToken()
    islemlerStack.append(token)
    K()
    islemlerStack.pop()
    islemlerStack.pop()
    islemlerStack.append("G")
    token = getToken()#noktalı virgün çıksın
   
def E():
    # E → T {('+' | '-') T}  {-,+,T} 
    global siralama,token,islemlerStack
    siralama.append("E")

    nonTerminal=["+","-"]
    
    if token in nonTerminal:
        islemlerStack.pop()#+ - çıkardı
        islemlerStack.pop()#son kalan T
        token=getToken()
        islemlerStack.append(token)
        E()
    
    else:
        T()
        islemlerStack.pop()
        islemlerStack.append("E")
        #bir sonraki token + - den farklıysa bu işlem biter ama değilse e yeniden çağırılır
        token=getToken()
        if token in nonTerminal:
            islemlerStack.append(token)
            E()
        else:
            setToken(token)
        
def T():
    # T → U {('*' | '/' | '%') U} u*u u/u u%u
    global siralama,token,islemlerStack
    siralama.append("T")

    nonTerminal=["*","/","%"]

    if token in nonTerminal:
        islemlerStack.pop()#+ - çıkardı
        islemlerStack.pop()#son kalan U
        token=getToken()
        islemlerStack.append(token)
        T()
    
    else:
        U()
        islemlerStack.pop()
        islemlerStack.append("T")
        #bir sonraki token + - den farklıysa bu işlem biter ama değilse e yeniden çağırılır
        token=getToken()
        if token in nonTerminal:
            islemlerStack.append(token)
            T()
        else:
            setToken(token)
              
def U():
    global siralama,token,islemlerStack
    siralama.append("U")
    # U → F '^' U | F
    # ihtimal 1 yok
    F() 
    token =getToken()
    if token == "^":
        islemlerStack.pop()# F yi çıkar içerden
        token=getToken()
        islemlerStack.append(token)# yeni gelen eleman
        U()
    else:
        setToken(token)
        son = islemlerStack.pop()
        if son == "F":
            islemlerStack.append("U")

def F():
    # F → '(' E ')' | K |  R
    global siralama,token,islemlerStack
    siralama.append("F")
 
    if rakamMi(token) == True:
        R()
        islemlerStack.pop()
        islemlerStack.append("F")

    elif kucukHarfMi(token) == True:
        K()
        islemlerStack.pop()
        islemlerStack.append("F")

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

    else:
        return "Hata ! Gecersiz string !"


def K():
    global siralama,token,islemlerStack
    siralama.append("K")
    # harf
    # K → 'a'  |  'b'  | … |  'z'
    if kucukHarfMi(token):
        islemlerStack.pop()  
        islemlerStack.append("K")

    else:
        return False
        # print girilen hatalı

def R():
    global siralama,token,islemlerStack
    siralama.append("R")
    # rakam
    # R → '0'  |  '1'  | … |  '9'
    if rakamMi(token):
        islemlerStack.pop()
        islemlerStack.append("R")
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
    global stack,inputString
    for i in reversed(range(len(inputString))):
        stack.append(inputString[i])

def getToken():
    global stack
    top = stack.pop()
    return top

def setToken(token):
    global stack
    stack.append(token)


inputString = "n=5;n=5;{n-2*5?<n;n=n+1;}{n-2*5?<n;n=n+1;}[n-2?<n;][n-2?<n;]<n;>g;>g;"
inputs="n=0;{n-2*5?<n;n=n+1;}"
islemlerStack = ['$']
stack = ['$']

# Main buradan başlamaktadır.
inputToStack()  # Global tanimlama
token = getToken()
islemlerStack.append(token)
#---------------------

#Agaç çizimi için treelib eklendi.
from treelib import Node, Tree
siralama=['P']
tree = Tree()
tree.create_node("P", "P") 

#---------------------

P()

print(siralama)
#Ağacı göster
tree.show()