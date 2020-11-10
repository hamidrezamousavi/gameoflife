import tkinter as tk
from algo import ROW,COL

class Board():
    choose_cells = []
    
    class Cell(tk.Label):
        def __init__(self,frm,**kw):
           super().__init__(frm,kw)
           self.row = 0
           self.col = 0
        def event_handeler(self,event):
            
            if not self.cget('bg')=='LightBlue':
               
                self.configure(bg='LightBlue')
                Board.choose_cells.append([self.row,self.col])
                
            else:
                
                self.configure(bg='gray90')
                Board.choose_cells.remove([self.row,self.col])
                
    def __init__(self,root):
        self.root = root
        

        canvas = tk.Canvas( root,borderwidth=1, background="Gray",
                            width=990, height=780)          #place canvas on self
    
        viewPort = tk.Frame(canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
        
        canvas.grid(column=0,row=0)
        canvas_window = canvas.create_window((4,4), window=viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")
      






        
        
        self.cells = []
        for i in range(ROW):
            self.cells.append([])
            for j in range(COL):
                cell =Board.Cell(viewPort,height=1,width=2,padx=0,pady=0,
                              borderwidth = 1,relief="raised",bg='gray90'  )
                cell.row = i
                cell.col = j            

                self.cells[i].append(cell)
                self.cells[i][j].grid(column=j,row=i)
                   
                

                self.cells[i][j].bind('<Button-1>',self.cells[i][j].event_handeler)


