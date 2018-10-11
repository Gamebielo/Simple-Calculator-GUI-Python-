import sys
from tkinter import *

#FUNÇÕES PARA OS BOTÕES DA CALCULADORA
def clear():
    global operator
    operator = ''
    text_input.set('')

def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def btn_igual():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''


root = Tk() #Criando uma janela principal
frame = Frame(root)
frame.pack()
root.title('Calculadora')
operator = ''
text_input = StringVar() #Area para escrever

txtDisplay = Entry(frame, textvariable = text_input, bd = 20, insertwidth = 1, font = 30, bg = 'powder blue')
txtDisplay.pack(side = TOP)
#======================================================================================

topframe = Frame(root)  #Primeira linha de botôes
topframe.pack(side = TOP)

btn7 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '7', fg = 'black', bg = 'powder blue',command = lambda:btnClick(7))
btn7.pack(side = LEFT)
btn8 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '8', fg = 'black', bg = 'powder blue', command = lambda:btnClick(8))
btn8.pack(side = LEFT)
btn9 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '9', fg = 'black', bg = 'powder blue',command = lambda:btnClick(9))
btn9.pack(side = LEFT)
btn_mais = Button(topframe, padx = 16, pady = 16, bd = 8, text = '+', fg = 'black', bg = 'powder blue',command = lambda:btnClick('+'))
btn_mais.pack(side = LEFT)
#=====================================================================================

frame1 = Frame(root)    #Segunda linha de botôes
frame1.pack(side = TOP)

btn4 = Button(frame1, padx = 16, pady = 16, bd = 8, text = '4', fg = 'black', bg = 'powder blue',command = lambda:btnClick(4))
btn4.pack(side = LEFT)
btn5 = Button(frame1, padx = 16, pady = 16, bd = 8, text = '5', fg = 'black', bg = 'powder blue',command = lambda:btnClick(5))
btn5.pack(side = LEFT)
btn6 = Button(frame1, padx = 16, pady = 16, bd = 8, text = '6', fg = 'black', bg = 'powder blue',command = lambda:btnClick(6))
btn6.pack(side = LEFT)
btn_menos = Button(frame1, padx = 16, pady = 16, bd = 8, text = '-', fg = 'black', bg = 'powder blue',command = lambda:btnClick('-'))
btn_menos.pack(side = LEFT)
#======================================================================================

frame2 = Frame(root)    #Terceira linha de botôes
frame2.pack(side = TOP)

btn1 = Button(frame2, padx = 16, pady = 16, bd = 8, text = '1', fg = 'black', bg = 'powder blue',command = lambda:btnClick(1))
btn1.pack(side = LEFT)
btn2 = Button(frame2, padx = 16, pady = 16, bd = 8, text = '2', fg = 'black', bg = 'powder blue',command = lambda:btnClick(2))
btn2.pack(side = LEFT)
btn3 = Button(frame2, padx = 16, pady = 16, bd = 8, text = '3', fg = 'black', bg = 'powder blue',command = lambda:btnClick(3))
btn3.pack(side = LEFT)
btn_vezes = Button(frame2, padx = 16, pady = 16, bd = 8, text = '*', fg = 'black', bg = 'powder blue',command = lambda:btnClick('*'))
btn_vezes.pack(side = LEFT)
#=====================================================================================

frame3 = Frame(root)    #Quarta linha de botôes
frame3.pack(side = TOP)

btn0 = Button(frame3, padx = 16, pady = 16, bd = 8, text = '0', fg = 'black', bg = 'powder blue',command = lambda:btnClick(0))
btn0.pack(side = LEFT)
btn_clear = Button(frame3, padx = 16, pady = 16, bd = 8, text = 'C', fg = 'black', bg = 'powder blue',command = clear)
btn_clear.pack(side = LEFT)
btn_result = Button(frame3, padx = 16, pady = 16, bd = 8, text = '=', fg = 'black', bg = 'powder blue',command = btn_igual)
btn_result.pack(side = LEFT)
btn_div = Button(frame3, padx = 16, pady = 16, bd = 8, text = '/', fg = 'black', bg = 'powder blue',command = lambda:btnClick('/'))
btn_div.pack(side = LEFT)



root.mainloop()
