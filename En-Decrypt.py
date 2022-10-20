from tkinter import *


mainwindow = Tk()
mainwindow.title('Kyptografie interaktiv via Python GUI')
mainwindow.geometry('500x400')

eingabefeldKlartext = Entry(mainwindow, width=20)
eingabefeldCyphertext = Entry(mainwindow, width=20)

label1 = Label(mainwindow, text="Klartext:")
label2 = Label(mainwindow, text="Cyphertext:")

label1.pack()
eingabefeldKlartext.pack()

label2.pack()
eingabefeldCyphertext.pack()


#Caesar encrypt Funktion
def doCaesarEncrypt():
    Klartext = eingabefeldKlartext.get().upper()
    C = []
    for i in range(len(Klartext)):
        if ord(Klartext[i]) + 3 > ord('Z'):
            C.append(chr(ord(Klartext[i]) + 3 - 26))
        else:
            C.append(chr(ord(Klartext[i]) + 3))

    eingabefeldCyphertext.delete(0, END)
    eingabefeldCyphertext.insert(0, "".join(C))

#Caesar Decrypt Funktion
def doCaesarDecrypt():
    Cyphertext = eingabefeldCyphertext.get().upper()
    K = []
    for i in range(len(Cyphertext)):
        if ord(Cyphertext[i]) - 3 < ord('A'):
            K.append(chr(ord(Cyphertext[i]) - 3 + 26))
        else:
            K.append(chr(ord(Cyphertext[i]) - 3))

    eingabefeldKlartext.delete(0, END)
    eingabefeldKlartext.insert(0, "".join(K))

#Gartenzaun encrypt Funktion
def doGartenzaunEncrypt():
    Klartext = eingabefeldKlartext.get().upper()
    L1 = []
    L2 = []
    C = []
    for i in range(len(Klartext)):
        if (i % 2 == 0):
            L1.append(Klartext[i])
        else:
            L2.append(Klartext[i])
    C = L1 + L2

    eingabefeldCyphertext.delete(0, END)
    eingabefeldCyphertext.insert(0, "".join(C))

#Gartenzaun Decrypt Funktion
def doGartenzaunDecrypt():
    Cyphertext = eingabefeldCyphertext.get().upper()

    eingabefeldKlartext.delete(0, END)
    eingabefeldKlartext.insert(0, "".join(K))

#Delet Funktion
def dodelet():
    Klartext = eingabefeldKlartext.get().upper()
    Cyphertext = eingabefeldCyphertext.get().upper()
    K = []
    C = []
    eingabefeldCyphertext.delete(0, END)
    eingabefeldCyphertext.insert(0, "".join(C))
    eingabefeldKlartext.delete(0, END)
    eingabefeldKlartext.insert(0, "".join(K))

#Caesar Knopf
caesarEncButton = Button(mainwindow, text="Caesar encrypt", command=doCaesarEncrypt)
caesarEncButton.pack()
caesarDecButton = Button(mainwindow, text="Caesar decrypt", command=doCaesarDecrypt)
caesarDecButton.pack()

#Gartenzaun Knopf
caesarEncButton = Button(mainwindow, text="Gartenzaun encrypt", command=doGartenzaunEncrypt)
caesarEncButton.pack()
caesarDecButton = Button(mainwindow, text="Gartenzaun decrypt", command=doGartenzaunDecrypt)
caesarDecButton.pack()

#Delet Knopf
deletButoon = Button(mainwindow, text="Delet", command=dodelet)
deletButoon.pack()


mainwindow.mainloop()

