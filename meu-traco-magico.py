from tkinter import *

## vars
quadro_x = 600
quadro_y = 400
quadro_cor = 'black'

p1_x = quadro_x/2
p1_y = quadro_y/2
linha_x = 5
linha_y = 5


## funcs
def p1_mov_UP(self):
    global p1_y
    quadro.create_line(p1_x, p1_y, p1_x, (p1_y-linha_y), width=linha_x, fill="green") 
    p1_y-=linha_y

def p1_mov_DOWN(self):
    global p1_y
    quadro.create_line(p1_x, p1_y, p1_x, (p1_y+linha_y), width=linha_x, fill="blue")
    p1_y+=linha_y

def p1_mov_LEFT(self):
    global p1_x
    quadro.create_line(p1_x, p1_y, (p1_x-linha_x), p1_y, width=linha_x, fill="red")
    p1_x-=linha_y

def p1_mov_RIGHT(self):
    global p1_x
    quadro.create_line(p1_x, p1_y, (p1_x+linha_x), p1_y, width=linha_x, fill="yellow")
    p1_x+=linha_y

def erase_all(self):
    quadro.delete(ALL)

def reset_pos(self):
    global p1_x
    p1_x = quadro_x/2
    global p1_y
    p1_y = quadro_y/2



## janela
janela = Tk()

janela.title('Meu Traço Mágico')
quadro = Canvas(bg=quadro_cor, width=quadro_x, height=quadro_y, highlightthickness=0)

quadro.pack()

janela.bind("<Up>", p1_mov_UP)
janela.bind("<Down>", p1_mov_DOWN)
janela.bind("<Left>", p1_mov_LEFT)
janela.bind("<Right>", p1_mov_RIGHT)
janela.bind("u", erase_all)
janela.bind("r",reset_pos)

janela.mainloop()