import tkinter as tk
import random
from tkinter import messagebox as mb
import Dictionary as dct



class Interface:
    """
    Это класс, который отвечает за интерфейс игры. В __инит__ создаются все элементы интерфейса игры
    """
    def __init__(self, word):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.canvas = tk.Canvas(self.root, bg = 'white')
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.word = word
        self.list_of_str_var = []
        self.frame_bottom = tk.Frame(self.canvas)
        self.frame_bottom.pack(side = tk.BOTTOM)
        self.frame_top = tk.Frame(self.canvas, borderwidth = 2, relief = 'solid')
        self.letter_field = tk.Entry(self.frame_top, borderwidth = 2, relief = 'solid')
        self.label_enter_the_letter = tk.Label(self.frame_top,
                                               text = 'Введите букву в поле справа')
        self.get_button = tk.Button(self.frame_top, text = 'ОК', command = self.create_check_button)
        self.label_enter_the_letter.pack(side = tk.LEFT)
        self.frame_top.pack(side = tk.BOTTOM)
        self.letter_field.pack(side = tk.LEFT)
        self.get_button.pack(side = tk.LEFT)
        self.flag_of_checker = 0
        self.checker_object = 0
        self.player_name1 = tk.StringVar() #эти 2 варинта для Лейбла в скореборд
        self.player_name2 = tk.StringVar()
        self.player1 = '' # эти 2 варианта имени игрока для обозначения, чей ход
        self.player2 = ''
        self.player_flag = 1
        self.game_flag = 0 #этот флаг показывает, какой режим вклчюен 1 или 2 игрока. 0 - один игрок
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label = 'Сменить режим игры', command = self.change_mod)
        self.root.config(menu = self.menu)

    def create_blokcs_for_letters(self, word):
        """
        эта функция рисует квадраты - объекты tk.Label, в которые будут вписаны буквы.
        У Лейблов в качестве значений изначально заданы переменные СтрингВар()
        """
        word = word
        self.list_of_str_var = []
        if not self.frame_bottom:
            self.frame_bottom = tk.Frame(self.canvas)
            self.frame_bottom.pack(side = tk.BOTTOM)
        for i in range(len(word)):
            future_letter = tk.StringVar()
            self.list_of_str_var.append(future_letter)
            label = tk.Label(self.frame_bottom, height = 2, width = 5,
                     textvariable = self.list_of_str_var[i], 
                     bg = 'white', borderwidth = 2,
                     relief = 'solid',
                     font = ('Timew New Roman', 13))
            label.pack(side = tk.LEFT)
            
    def raise_letter_error(self):
        """
        Эта функция генерирует ошибку, если в поле
        введено несколько букв, цифра или буква латинксого или другого алфавита
        """
        self.letter_field.delete(0, tk.END)
        mb.showerror('Ошибка', 'Введите ОДНУ букву РУССКОГО алфавита')

    def raise_new_game_offer(self):
        """
        Эта функция предлагает сыграть снова после поражения
        """
        self.letter_field.delete(0, tk.END)
        return mb.askyesno(title = 'Вы проиграли',
                           message = 'Хотите сыграть еще?')

    def destroy_root(self):
        """
        Эта функция уничтожает рут, если пользователь откажется начинать новую игру
        """
        self.root.destroy()

    def create_check_button(self):
        """
        импортирует ГетЛеттер (если импортировать в начале модуля, будет ошибка).
        проверяет, привязана ли к кнопке команда из класса Чекер, если нет,
        то привязывает. После этого в любом случае запускает функцию Чекера
        по проверка
        """
        import GetLetter as gl
        if self.flag_of_checker == 0:
            self.checker_object = gl.Checker(self.word, self.letter_field,
                                             self.list_of_str_var, self)
            self.flag_of_checker = 1
        self.checker_object.check_letter()
        
    def clean_canvas(self):
        """
        эта функция удаляет с холста рисунки, а также фрейм с квадратами
        для буквы
        """
        self.canvas.delete('all')
        self.frame_bottom.destroy()
        self.frame_bottom = 0
        if self.player1 and self.game_flag == 0:
            self.frame_board.destroy()

    def victory(self):
        """
        функция вызывает всплывающее окно, которое предлагает сыграть снова
        """
        self.letter_field.delete(0, tk.END)
        return mb.askyesno(title = 'Вы выиграли!', message = 'Хотите сыграть еще?')

    def two_player_offer(self):
        return mb.askyesno(title = 'Выберите режим игры', message = 'Играете вдвоем?')

    def enter_names(self):
        """
        эта функция вызывает всплывающее окно для ввода имен игроков
        """
        self.game_flag = 1
        window_for_name = tk.Toplevel()
        window_for_name.geometry('200x120+300+200')
        tk.Label(window_for_name, text = 'Введите имена игроков').pack()
        frame1 = tk.Frame(window_for_name)
        frame1.pack()
        frame2 = tk.Frame(window_for_name)
        frame2.pack()
        entry_for_name1 = tk.Entry(frame1)
        entry_for_name1.pack(side = tk.LEFT)
        def get_1st_name():
            self.player_name1.set(entry_for_name1.get())
            self.player1 = entry_for_name1.get()
            print(self.player1)
            if self.player1 == '':
                self.player_name1.set('Игрок 1')
                self.player1 = 'Игрок 1'
            entry_for_name1.delete(0, tk.END)
        entry_for_name2 = tk.Entry(frame2)
        entry_for_name2.pack(side = tk.LEFT)
        def get_2nd_name():
            self.player_name2.set(entry_for_name2.get())
            self.player2 = entry_for_name2.get()
            if self.player2 == '':
                self.player_name2.set('Игрок 2')
                self.player2 = 'Игрок 2'
            entry_for_name2.delete(0, tk.END)
        def close_window():
            get_1st_name()
            get_2nd_name()
            self.enter_the_word()
            window_for_name.destroy()
        tk.Button(window_for_name, text = 'Закрыть', command = close_window).pack()

    def create_scoreboard(self):
        """
        эта функция создает доску с очками игроков. Используются тк.СтрингВар()
        для того, чтобы на ходу менять значения Лейблов
        """
        self.frame_board = tk.Frame(self.canvas)
        self.frame_board.pack(anchor = tk.NE)
        self.str_var_for_player1 = tk.StringVar()
        self.player_name_label1 = tk.Label(self.frame_board,
                                           textvariable = self.player_name1)
        self.player_name_label1.pack(side = tk.LEFT)
        self.label_for_player1 = tk.Label(self.frame_board,
                                     textvariable = self.str_var_for_player1,
                                     font = ('Timew New Roman', 13))
        self.label_for_player1.pack(side = tk.LEFT)
        self.str_var_for_player2 = tk.StringVar()
        self.player_name_label2 = tk.Label(self.frame_board,
                                           textvariable = self.player_name2)
        self.player_name_label2.pack(side = tk.LEFT)
        self.label_for_player2 = tk.Label(self.frame_board,
                                     textvariable = self.str_var_for_player2,
                                     font = ('Timew New Roman', 13))
        self.label_for_player2.pack(side = tk.LEFT)

    def enter_the_word(self):
        """
        эта функция создает окно с полем, в которое указанный на Лейбле игрок
        должен ввести загадываемое слово. После этого вызывает конструктор
        блоков. Первый раз функция запускается цепочкой из Мейна, второй и
        последующие - уже из Чекера
        """
        window_for_word_field = tk.Toplevel()
        window_for_word_field.geometry('400x80+300+200')
        def is_it_empty():
            """эта функция используется для проверки, ввел ли пользователь слово
            в поле для ввода загадываемого слова. Если слово не введено,
            выводит ошибку"""
            if self.word == '':
                mb.showerror('Ошибка', 'Загадайте слово!')
            else:
                window_for_word_field.destroy()
        window_for_word_field.protocol("WM_DELETE_WINDOW", is_it_empty)
        if self.player_flag == 0:
            tk.Label(window_for_word_field,
                     text = '{}, введите загадываемое слово. Отгадывать будет {}'.format(
                         self.player2, self.player1)).pack()
        if self.player_flag == 1:
            tk.Label(window_for_word_field,
                     text = '{}, введите загадываемое слово. Отгадывать будет {}'.format(
                         self.player1, self.player2)).pack()
        word_field = tk.Entry(window_for_word_field)
        word_field.pack()
        word_field.delete(0, tk.END)
        def destroy_window():
            """
            эта функция закрывает окно ТопЛевел для ввода слова
            """
            self.word = word_field.get()
            if self.word == '':
                mb.showerror('Ошибка', 'Загадайте слово!')
            else:
                self.word = self.word.lower()
                word_field.delete(0, tk.END)
                if self.player_flag == 1:
                    self.player_flag = 0
                elif self.player_flag == 0:
                    self.player_flag = 1
                self.create_blokcs_for_letters(self.word)
                window_for_word_field.destroy()
        tk.Button(window_for_word_field, text = 'OK',
                  command = destroy_window).pack()
    def get_word(self):
        """
        эта функция используется в модуле ГетЛеттер в функции релоад_гейм, которая
        перезагружает игру (начинает новую).
        """
        return self.word

    def change_mod(self):
        if self.game_flag == 1:
            self.game_flag = 0
            self.clean_canvas()
            self.word = random.choice(dct.dict_for_hanggame)
            self.create_blokcs_for_letters(self.word)
        elif self.game_flag == 0:
            self.game_flag = 1
            self.clean_canvas()
            self.enter_names()
            self.create_scoreboard()

    def show_word(self):
        mb.showerror('Вы проиграли', ('Вы не отгадали слово "{}"').format(self.word))
