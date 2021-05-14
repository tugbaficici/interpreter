from treelib import Tree
import sys
sys.tracebacklimit=0


def P():
    global islemlerStack, token, sonuc
    if token == ".":
        sonuc = "accept"
    else:
        C()
        P()


def C():
    C.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"

    global siralama, token, islemlerStack
    siralama.append("C")

    if token == "[":
        tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
        token = getToken()
        islemlerStack.append(token)
        I()
        islemlerStack.pop()
        cvarmi = islemlerStack.pop()
        if cvarmi != "C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token = getToken()
        if token != "$":
            islemlerStack.append(token)
        if checkIfCExists():
            P()
        else:
            C()

    elif token == "{":
        tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
        W()
        islemlerStack.pop()
        cvarmi = islemlerStack.pop()
        if cvarmi != "C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token = getToken()
        if token != "$":
            islemlerStack.append(token)
        if checkIfCExists():
            P()
        else:
            C()

    elif token == "<":
        tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
        noktaliC()
        islemlerStack.pop()
        cvarmi = islemlerStack.pop()
        if cvarmi != "C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token = getToken()
        if checkIfCExists():
            P()
        else:
            C()

    elif token == ">":
        tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
        G()
        islemlerStack.pop()
        cvarmi = islemlerStack.pop()
        if cvarmi != "C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token = getToken()
        if checkIfCExists():
            P()
        else:
            C()

    elif kucukHarfMi(token) == True:  # token harf ise
        tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
        A()
        islemlerStack.pop()
        cvarmi = islemlerStack.pop()
        if cvarmi != "C":
            islemlerStack.append(cvarmi)
        islemlerStack.append("C")
        token = getToken()
        if checkIfCExists():
            P()
        else:
            C()

    elif token == '$':
        son = islemlerStack.pop()
        son = islemlerStack.pop()
        if(son == '$'):
            token = '.'


def I():

    I.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    
    global siralama, token, islemlerStack
    siralama.append("I")

    E()
    token = getToken()
    if token == "?":
        islemlerStack.append(token)
        token = getToken()  # c
        islemlerStack.append(token)
        C()
        if token == ":":
            islemlerStack.append(token)
            token = getToken()  # c
            islemlerStack.append(token)
            C()
            islemlerStack.append(token)
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("I")

        elif token == "]":
            islemlerStack.append(token)
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("I")

        else:
            print("IF işlemlerinde beklenmedik token.")
    else:
        print("IF işlemlerinde '?' tokeni eksik.")


def W():
    W.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    
    global siralama, token, islemlerStack
    siralama.append("W")

    token = getToken()
    islemlerStack.append(token)
    E()
    token = getToken()
    if token == "?":
        islemlerStack.append(token)
        token = getToken()
        islemlerStack.append(token)
        C()
        token = getToken()
        islemlerStack.append(token)

        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.pop()
        islemlerStack.append("W")
        setToken(token)
    else:
        print("WHILE işlemlerinde '?' tokeni eksik.")


def A():
    A.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    

    global siralama, token, islemlerStack
    siralama.append("A")

    K()
    token = getToken()
    islemlerStack.append(token)
    if token == "=":
        token = getToken()
        islemlerStack.append(token)
        E()
        token = getToken() 
        if token == ";":
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("A")
        else:
            print("Atama işlemlerinde ';' tokeni eksik.")
    else:
        print("Atama işlemlerinde '=' tokeni eksik.")


def noktaliC(): 

    noktaliC.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    

    global siralama, token, islemlerStack
    siralama.append("Ç")

    token = getToken()
    islemlerStack.append(token)
    E()
    islemlerStack.pop()
    islemlerStack.pop()
    islemlerStack.append("Ç")
    token = getToken()
    if token != ";":
        print("Girdi işlemlerinde ';' tokeni eksik.")


def G():

    G.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    
    global siralama, token, islemlerStack
    siralama.append("G")

    token = getToken()
    islemlerStack.append(token)
    K()
    islemlerStack.pop()
    islemlerStack.pop()
    islemlerStack.append("G")
    token = getToken()
    if token != ";":
        print("Girdi işlemlerinde ';' tokeni eksik.")


def E():

    E.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)

    global siralama, token, islemlerStack
    siralama.append("E")

    nonTerminal = ["+", "-"]

    if token in nonTerminal:
        islemlerStack.pop()
        islemlerStack.pop()
        token = getToken()
        islemlerStack.append(token)
        E()

    else:
        T()
        islemlerStack.pop()
        islemlerStack.append("E")
        token = getToken()
        if token in nonTerminal:
            islemlerStack.append(token)
            E()
        else:
            setToken(token)


def T():

    T.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)

    global siralama, token, islemlerStack
    siralama.append("T")

    nonTerminal = ["*", "/", "%"]

    if token in nonTerminal:
        islemlerStack.pop()
        islemlerStack.pop()
        token = getToken()
        islemlerStack.append(token)
        T()

    else:
        U()
        islemlerStack.pop()
        islemlerStack.append("T")
        token = getToken()
        if token in nonTerminal:
            islemlerStack.append(token)
            T()
        else:
            setToken(token)


def U():

    U.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    

    global siralama, token, islemlerStack
    siralama.append("U")
    F()
    token = getToken()
    if token == "^":
        islemlerStack.pop()
        token = getToken()
        islemlerStack.append(token)
        U()
    else:
        setToken(token)
        son = islemlerStack.pop()
        if son == "F":
            islemlerStack.append("U")


def F():

    F.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    
    global siralama, token, islemlerStack
    siralama.append("F")

    if rakamMi(token) == True:
        R()
        islemlerStack.pop()
        islemlerStack.append("F")

    elif kucukHarfMi(token) == True:
        K()
        islemlerStack.pop()
        islemlerStack.append("F")

    elif token == "(":
        token = getToken()
        islemlerStack.append(token)
        E()
        token = getToken()
        islemlerStack.append(token)
        if(token == ")"):
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.pop()
            islemlerStack.append("F")
        else:
            print("Gruplama işleminde ')' tokeni eksik.")

    else:
        print("Gruplama işleminde beklenmedik token.")


def K():
    K.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    

    global siralama, token, islemlerStack
    siralama.append("K")

    if kucukHarfMi(token):
        islemlerStack.pop()
        islemlerStack.append("K")

    else:
        print("Gelen token küçük harf değil.")


def R():

    R.counter += 1
    parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter}"
    childid = sys._getframe().f_code.co_name + str(globals()[sys._getframe().f_code.co_name].counter)
    if parentid == childid:
        parentid = f"{sys._getframe(1).f_code.co_name}{globals()[sys._getframe(1).f_code.co_name].counter - 1}"
    
    tree.create_node(sys._getframe().f_code.co_name, childid, parent=parentid)
    

    global siralama, token, islemlerStack
    siralama.append("R")

    if rakamMi(token):
        islemlerStack.pop()
        islemlerStack.append("R")
    else:
        print("Gelen token rakam değil.")


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
    global stack, inputString
    for i in reversed(range(len(inputString))):
        stack.append(inputString[i])


def getToken():
    global stack
    top = stack.pop()
    return top


def setToken(token):
    global stack
    stack.append(token)


def checkIfCExists():
    global islemlerStack
    stack_ = set(islemlerStack)
    if(len(stack_) == 2):
        if ('$' in stack_) and ('C' in stack_) :
            return True
        else:
            return False
    else:
        return False


for func in ["P", "F", "U", "T", "E", "W", "I", "noktaliC", "G", "A", "C", "K", "R"]:
    globals()[func].counter = 0


inputString = "n=0;{n-2*5?<n;n=n+1;}"
islemlerStack = ['$']
stack = ['$']


inputToStack()
token = getToken()
islemlerStack.append(token)

siralama = ['P']
tree = Tree()
tree.create_node("P", "P0")


P()
print("Sıralama: ", siralama)

print("Tree: ")
tree.show()

print("Sonuç: ", sonuc)
