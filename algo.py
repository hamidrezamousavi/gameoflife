import copy



ROW = 34
COL = 55
cells = [[0 for _ in range(COL)] for _ in range(ROW)]


def neighbores(cell):
    neighbore = []
    draft_neighbore = [   [cell[0]-1,cell[1]-1],
                          [cell[0]-1,cell[1]],
                          [cell[0]-1,cell[1]+1],
                          [cell[0],cell[1]-1],
                          [cell[0],cell[1]+1],
                          [cell[0]+1,cell[1]-1],
                          [cell[0]+1,cell[1]],
                          [cell[0]+1,cell[1]+1],
                        ]
  
    for item in draft_neighbore:
        if not (item[0] < 0 or item[0] > ROW-1 or item[1] < 0 or item[1] > COL-1 ):
            neighbore.append(item)
    
    return neighbore

def next_state():
    global cells
    
    after_evol_cells = copy.deepcopy(cells)
   
    for i  in range(0,ROW):
        for j in range(0,COL):
            on_neighbors = 0
            on_neighbors =sum( [cells[item[0]][item[1]] for item in neighbores([i,j])])
            
            
            if on_neighbors <= 1:
                after_evol_cells[i][j] = 0
            if on_neighbors >= 4:
                after_evol_cells[i][j] = 0
            if on_neighbors == 3:
                after_evol_cells[i][j] = 1
   
    for i  in range(0,ROW):
        for j in range(0,COL):
            cells[i][j] =after_evol_cells[i][j]

   




