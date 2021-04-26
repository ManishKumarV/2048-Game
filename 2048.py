from tkinter import Frame,Label,CENTER

import logic
import configure as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:logic.move_up,c.KEY_DOWN:logic.move_down,c.KEY_LEFT:logic.move_left,c.KEY_RIGHT:logic.move_right}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

        pass
    
    def init_grid(self):
        background =Frame(self,bg=c.BG_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame( background, bg=c.BG_COLOR_CELL_EMPTY, width=c.SIZE / c.GRID_LEN, height=c.SIZE / c.GRID_LEN ) 
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                t=Label(master=cell,text="",bg=c.BG_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,widt=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
        pass
    
    def init_matrix(self):
        self.matrix=logic.start_game()
        logic.add_new_2(self.matrix)
        logic.add_new_2(self.matrix)
        pass

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_num=self.matrix[i][j]
                if new_num==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BG_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_num),bg=c.BG_COLOR_DICT[new_num],fg=c.CELL_COLOR_DICT[new_num])
        self.update_idletasks()
        pass
    
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,change=self.commands[repr(event.char)](self.matrix)
            if change:
                logic.add_new_2(self.matrix)
                self.update_grid_cells()
                change=False
                if logic.game_status(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BG_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="WON!",bg=c.BG_COLOR_CELL_EMPTY)
                if logic.game_status(self.matrix)=="LOSE":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BG_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="LOST!",bg=c.BG_COLOR_CELL_EMPTY)
        pass 

game=Game2048()