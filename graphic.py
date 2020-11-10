import tkinter as tk
from table import Board
from algo import next_state,ROW,COL,cells



    

win = tk.Tk()
win.title('Game of Life')
win.geometry('1000x800')
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)
frm_board = tk.Frame()
frm_board.grid(column=0,row=0,sticky='s')
board = Board(frm_board)

frm_but = tk.Frame()
frm_but.grid(column=0,row=1,sticky='s')

def next_but_action():
    global cells
   
    for i in range(ROW):
        for j in range(COL):
            if [i,j] in board.choose_cells:
                cells[i][j] = 1    
            else:
                cells[i][j] = 0    
    next_state()
    
    for i in range(ROW):
        for j in range(COL):
            if cells[i][j] == 1:
                board.cells[i][j].configure(bg='LightBlue')
            else:
                board.cells[i][j].configure(bg='gray90')
            
    Board.choose_cells = []
    for i in range(ROW):
        for j in range(COL):
            if cells[i][j] == 1:
                board.choose_cells.append([i,j])
    

def start_but_action():
    if start_but.cget('text')=='Start': 
        start_but.configure(text='Stop')
    else:
        start_but.configure(text='Start')
   
    def show():
        if start_but.cget('text')=='Stop':
            next_but_action()
            win.after(1,show)
        
    
    show()

next_but = tk.Button(frm_but,text='Next',command=next_but_action)
next_but.grid(column=30,row=1,sticky='NE',columnspan=2)

start_but = tk.Button(frm_but,text=' Start ',command=start_but_action)
start_but.grid(column=40,row=1,sticky='NE',columnspan=2)





win.mainloop()

