from tkinter import *

###
janela = Tk()
janela.title('Glossário do Programador')

glossario = { 
    'algorithm': 'Step by step instructions o perform a task that a computer could understand',
    'bug':'A piece of code that is causing a program to fail to run properly or at all',
    'binary number':'A number represented in base 2',    
}

###
def click():
    texto_entrada = entrada.get()
    saida.delete(0.0, END)
    try:
        etiqueta2 = glossario[texto_entrada]
    except:
        etiqueta2 = 'There is no entry for this word'
    saida.insert(END, etiqueta2)

###
etiqueta1 = Label(janela, text='')
entrada = Entry(janela)
botao = Button(janela, text= 'Submit', width= 5, command= click)
etiqueta2 = Label(janela, text='\nDefinição')
saida = Text(janela, width= 75, height= 6, wrap= WORD, bg='light green')

###
etiqueta1.pack
entrada.grid(row= 1, column= 0, sticky= W)
botao.grid(row= 2, column= 0, sticky= W)
etiqueta2.grid(row= 3, column= 0, sticky= W)
saida.grid(row= 4, column= 0, columnspan= 2, sticky= W)

janela.mainloop()
