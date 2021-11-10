from tkinter import *

# cores usadas na aplicação
cor1 = "#171616" # cinza escuro
cor2 = "#ffffff" # branco
cor3 = "#45a88b" # verde água
cor4 = "#2368ad" # azul
cor5 = "#c7c7c7" # cinza claro

# cria a janela, define título e tamanho
janela = Tk()
janela.title("Calculadora")
janela.geometry("350x450")

# divide a tela em dois frames
frame_display = Frame(janela, width=350, height=100, bg=cor2)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=380, bg=cor2)
frame_corpo.grid(row=1, column=0)


todos_valores = ''

# criando label
valor_texto = StringVar()

# função para calcular
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    

    # mostra na tela
    valor_texto.set(todos_valores)

# função para calcular
def calcular():
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função para limpar label
def limpar():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
    todos_valores = ""
    valor_texto.set("")
    

app_label = Label(frame_display, textvariable=valor_texto, width=20, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 22'))
app_label.place(x=0, y=0)


# botões 

# primeira linha
botao1 = Button(frame_corpo, command=limpar, text="C", width=20, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=1, y=0)
botao2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao2.place(x=176, y=0)

botao3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text="/", width=11, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x=267, y=0)

# segunda linha 
botao4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text="7", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=0, y=70)

botao5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text="8", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao5.place(x=85, y=70)

botao6 = Button(frame_corpo, command=lambda:entrar_valores('9'), text="9", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao6.place(x=176, y=70)

botao7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text="*", width=11, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=267, y=70)

# terceira linha 
botao8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text="4", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=140)

botao9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text="5", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=85, y=140)

botao10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text="6", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=176, y=140)

botao11 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=11, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=267, y=140)

# quarta linha 
botao12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text="1", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao12.place(x=0, y=210)

botao13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text="2", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao13.place(x=85, y=210)

botao14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text="3", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao14.place(x=176, y=210)

botao15 = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=11, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao15.place(x=267, y=210)

# quinta linha
botao16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text="0", width=20, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao16.place(x=1, y=280)

botao17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=11, height=3, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao17.place(x=176, y=280)

botao18 = Button(frame_corpo, command=calcular, text="=", width=11, height=3, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao18.place(x=267, y=280)


janela.mainloop()

