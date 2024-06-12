import customtkinter as ctk
import Assets.Scripts.variables as vary
import random as rd


class GameOver(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color='#242424')
        vary.game_over = self
        self.text = ctk.CTkLabel(master=self, text='TicTacToe', font=('Showcard Gothic', 60))
        self.text_1 = ctk.CTkLabel(master=self, text='Game Over', font=('Showcard Gothic', 40))
        self.text_2 = ctk.CTkLabel(master=self, text='Do you like to play again?', font=('Showcard Gothic', 20))

        self.btn_1 = ctk.CTkButton(master=self, text='Yes')
        self.btn_2 = ctk.CTkButton(master=self, text='No')

        self.btn_1.bind('<Button-1>', lambda x: HomePage.play_again(HomePage))
        self.btn_2.bind('<Button-1>', lambda x: self.exit_action())

        array = [
            self.btn_1, self.btn_2
        ]

        for i in array:
            i.configure(font=('Showcard Gothic', 20), width=80, height=80, fg_color='#303030', hover_color='#292929')

        self.text.grid(row=0, column=0, padx=5, pady=20, columnspan=2)
        self.text_1.grid(row=1, column=0, padx=5, pady=20, columnspan=2)
        self.text_2.grid(row=2, column=0, padx=5, pady=30, columnspan=2)
        self.btn_1.grid(row=3, column=0, padx=20, pady=40)
        self.btn_2.grid(row=3, column=1, padx=20, pady=40)

    def exit_action(self):
        self.quit()


class Game(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color='#242424')
        vary.game = self
        self.frame = ctk.CTkFrame(master=self, fg_color='#242424')
        self.text = ctk.CTkLabel(master=self, text='TicTacToe', font=('Showcard Gothic', 60))
        self.lbl_1 = ctk.CTkLabel(
            master=self, text=f'You: {vary.player}', font=('Showcard Gothic', 20), anchor='w', width=200
        )
        self.lbl_2 = ctk.CTkLabel(
            master=self, text=f'Computer: {vary.computer}', font=('Showcard Gothic', 20), anchor='e', width=200
        )

        self.btn_1 = ctk.CTkButton(master=self.frame, text='')
        self.btn_2 = ctk.CTkButton(master=self.frame, text='')
        self.btn_3 = ctk.CTkButton(master=self.frame, text='')
        self.btn_4 = ctk.CTkButton(master=self.frame, text='')
        self.btn_5 = ctk.CTkButton(master=self.frame, text='')
        self.btn_6 = ctk.CTkButton(master=self.frame, text='')
        self.btn_7 = ctk.CTkButton(master=self.frame, text='')
        self.btn_8 = ctk.CTkButton(master=self.frame, text='')
        self.btn_9 = ctk.CTkButton(master=self.frame, text='')

        self.array = [
            self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9
        ]

        for i in self.array:
            i.configure(font=('Showcard Gothic', 30), width=80, height=80, fg_color='#303030', hover_color='#292929')

        self.btn_1.bind('<Button-1>', lambda x: self.clicked(1, self.btn_1))
        self.btn_2.bind('<Button-1>', lambda x: self.clicked(2, self.btn_2))
        self.btn_3.bind('<Button-1>', lambda x: self.clicked(3, self.btn_3))
        self.btn_4.bind('<Button-1>', lambda x: self.clicked(4, self.btn_4))
        self.btn_5.bind('<Button-1>', lambda x: self.clicked(5, self.btn_5))
        self.btn_6.bind('<Button-1>', lambda x: self.clicked(6, self.btn_6))
        self.btn_7.bind('<Button-1>', lambda x: self.clicked(7, self.btn_7))
        self.btn_8.bind('<Button-1>', lambda x: self.clicked(8, self.btn_8))
        self.btn_9.bind('<Button-1>', lambda x: self.clicked(9, self.btn_9))

        self.text.grid(row=0, column=0, padx=5, pady=20, columnspan=2)
        self.lbl_1.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lbl_2.grid(row=1, column=1, padx=5, pady=5, sticky='e')
        self.frame.grid(row=2, column=0, padx=5, pady=10, columnspan=2)

        self.btn_1.grid(row=0, column=0, padx=10, pady=10)
        self.btn_2.grid(row=0, column=1, padx=10, pady=10)
        self.btn_3.grid(row=0, column=2, padx=10, pady=10)

        self.btn_4.grid(row=1, column=0, padx=10, pady=10)
        self.btn_5.grid(row=1, column=1, padx=10, pady=10)
        self.btn_6.grid(row=1, column=2, padx=10, pady=10)

        self.btn_7.grid(row=2, column=0, padx=10, pady=10)
        self.btn_8.grid(row=2, column=1, padx=10, pady=10)
        self.btn_9.grid(row=2, column=2, padx=10, pady=10)

    def clicked(self, event, btn):
        if btn.cget('text') == '':
            btn.configure(text=vary.player, state='disabled')
            vary.array.remove(event)
            if not len(vary.array) == 0:
                if self.btn_1.cget('text') == self.btn_2.cget('text') == vary.player:
                    num = 3
                elif self.btn_1.cget('text') == self.btn_3.cget('text') == vary.player:
                    num = 2
                elif self.btn_2.cget('text') == self.btn_3.cget('text') == vary.player:
                    num = 1
                elif self.btn_4.cget('text') == self.btn_5.cget('text') == vary.player:
                    num = 6
                elif self.btn_4.cget('text') == self.btn_6.cget('text') == vary.player:
                    num = 5
                elif self.btn_5.cget('text') == self.btn_6.cget('text') == vary.player:
                    num = 4
                elif self.btn_7.cget('text') == self.btn_8.cget('text') == vary.player:
                    num = 9
                elif self.btn_7.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 8
                elif self.btn_8.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 7
                elif self.btn_1.cget('text') == self.btn_4.cget('text') == vary.player:
                    num = 7
                elif self.btn_1.cget('text') == self.btn_7.cget('text') == vary.player:
                    num = 4
                elif self.btn_4.cget('text') == self.btn_7.cget('text') == vary.player:
                    num = 1
                elif self.btn_2.cget('text') == self.btn_5.cget('text') == vary.player:
                    num = 8
                elif self.btn_2.cget('text') == self.btn_8.cget('text') == vary.player:
                    num = 5
                elif self.btn_5.cget('text') == self.btn_8.cget('text') == vary.player:
                    num = 2
                elif self.btn_3.cget('text') == self.btn_6.cget('text') == vary.player:
                    num = 9
                elif self.btn_3.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 6
                elif self.btn_6.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 3
                elif self.btn_1.cget('text') == self.btn_5.cget('text') == vary.player:
                    num = 9
                elif self.btn_1.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 5
                elif self.btn_5.cget('text') == self.btn_9.cget('text') == vary.player:
                    num = 1
                elif self.btn_3.cget('text') == self.btn_5.cget('text') == vary.player:
                    num = 7
                elif self.btn_3.cget('text') == self.btn_7.cget('text') == vary.player:
                    num = 5
                elif self.btn_5.cget('text') == self.btn_7.cget('text') == vary.player:
                    num = 3
                else:
                    num = rd.randrange(0, len(vary.array))
                    num = vary.array[num]
                if num not in vary.array:
                    num = rd.randrange(0, len(vary.array))
                    num = vary.array[num]
                vary.array.remove(num)
                self.array[num - 1].configure(text=vary.computer, state='disabled')
            self.check_for_win()

    def check_for_win(self):
        if not len(vary.array) == -1:
            win = ''
            if self.btn_1.cget('text') == self.btn_2.cget('text') == self.btn_3.cget('text') == vary.player:
                win = vary.player
            elif self.btn_1.cget('text') == self.btn_2.cget('text') == self.btn_3.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_4.cget('text') == self.btn_5.cget('text') == self.btn_6.cget('text') == vary.player:
                win = vary.player
            elif self.btn_4.cget('text') == self.btn_5.cget('text') == self.btn_6.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_7.cget('text') == self.btn_8.cget('text') == self.btn_9.cget('text') == vary.player:
                win = vary.player
            elif self.btn_7.cget('text') == self.btn_8.cget('text') == self.btn_9.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_1.cget('text') == self.btn_4.cget('text') == self.btn_7.cget('text') == vary.player:
                win = vary.player
            elif self.btn_1.cget('text') == self.btn_4.cget('text') == self.btn_7.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_2.cget('text') == self.btn_5.cget('text') == self.btn_8.cget('text') == vary.player:
                win = vary.player
            elif self.btn_2.cget('text') == self.btn_5.cget('text') == self.btn_8.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_3.cget('text') == self.btn_6.cget('text') == self.btn_9.cget('text') == vary.player:
                win = vary.player
            elif self.btn_3.cget('text') == self.btn_6.cget('text') == self.btn_9.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_1.cget('text') == self.btn_5.cget('text') == self.btn_9.cget('text') == vary.player:
                win = vary.player
            elif self.btn_1.cget('text') == self.btn_5.cget('text') == self.btn_9.cget('text') == vary.computer:
                win = vary.computer
            elif self.btn_3.cget('text') == self.btn_5.cget('text') == self.btn_7.cget('text') == vary.player:
                win = vary.player
            elif self.btn_3.cget('text') == self.btn_5.cget('text') == self.btn_7.cget('text') == vary.computer:
                win = vary.computer

            if win == vary.player:
                vary.game_over.text_1.configure(text='You Won')
            elif win == vary.computer:
                vary.game_over.text_1.configure(text='Computer Won')
            else:
                vary.game_over.text_1.configure(text='Game Over')
            if not win == '':
                HomePage.btn_pressed_one(HomePage)
            if win == '' and len(vary.array) == 0:
                HomePage.btn_pressed_one(HomePage)


class Start(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color='#242424')

        self.text = ctk.CTkLabel(master=self, text='TicTacToe', font=('Showcard Gothic', 60))
        self.text_1 = ctk.CTkLabel(master=self, text='What will you be?', font=('Showcard Gothic', 20))

        self.btn_1 = ctk.CTkButton(master=self, text='x')
        self.btn_2 = ctk.CTkButton(master=self, text='o')

        self.btn_1.bind('<Button-1>', lambda x: HomePage.btn_pressed(HomePage, self.btn_1.cget('text')))
        self.btn_2.bind('<Button-1>', lambda x: HomePage.btn_pressed(HomePage, self.btn_2.cget('text')))

        array = [
            self.btn_1, self.btn_2
        ]

        for i in array:
            i.configure(font=('Showcard Gothic', 30), width=80, height=80, fg_color='#303030', hover_color='#292929')

        self.text.grid(row=0, column=0, padx=5, pady=100, columnspan=2)
        self.text_1.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        self.btn_1.grid(row=2, column=0, padx=20, pady=40)
        self.btn_2.grid(row=2, column=1, padx=20, pady=40)


class HomePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color='#242424')
        vary.home = self

        self.start = Start(master=self)
        self.game = Game(master=self)
        self.game_over = GameOver(master=self)

        self.start.pack()

    def btn_pressed(self, event):
        vary.player = event
        if event == 'x':
            vary.computer = 'o'
        elif event == 'o':
            vary.computer = 'x'

        vary.game.lbl_1.configure(text=f'You: {vary.player}')
        vary.game.lbl_2.configure(text=f'Computer: {vary.computer}')

        vary.home.start.pack_forget()
        vary.home.game.pack()

    def btn_pressed_one(self):
        vary.home.game.pack_forget()
        vary.home.game_over.pack()

    def play_again(self):
        vary.array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in vary.game.array:
            i.configure(state='normal', text='')
        vary.home.game_over.pack_forget()
        vary.home.game.pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        x = (self.winfo_screenwidth() / 2) - (vary.width / 2)
        y = ((self.winfo_screenheight() - 120) / 2) - (vary.height / 2)
        self.configure(fg_color='#242424')
        self.title('TicTacToe')
        self.geometry(f'{vary.width}x{vary.height}+{int(x)}+{int(y)}')
        self.resizable(0, 0)

        self.home = HomePage(master=self)
        self.home.pack()
