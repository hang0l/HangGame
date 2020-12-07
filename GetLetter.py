import Graphics as gr
import importlib
import Interface as it
import tkinter as tk
import Dictionary as dct
import random


alphabet = ['а', 'А', 'б', 'Б', 'в', 'В', 'г', 'Г', 'д', 'Д',
            'е', 'Е', 'ё', 'Ё', 'ж', 'Ж', 'з', 'З', 'и', 'И', 'к',
            'К', 'л', 'Л', 'м', 'М', 'н', 'Н', 'о', 'О', 'п', 'П',
            'р', 'Р', 'с', 'С', 'т', 'Т', 'у', 'У', 'ф', 'Ф', 'х', 'Х',
            'ц', 'Ц', 'ч', 'Ч', 'ш', 'Ш', 'щ', 'Щ', 'э', 'Э',
            'ъ', 'Ъ', 'ю', 'Ю', 'я', 'Я', 'й', 'Й', 'ь', 'Ь', 'ы', 'Ы']



class Checker(it.Interface):
    def __init__(self, word, letter_field,
                 list_of_str_var, it_obj):
       """
       виктори_каунтер увеличивается, когда пользователь угадывает букву. Когда он равен
       лен(селф.ворд), засчитывается победа
       дифит_каунтер увеличивается, когда пользователь ошибается. Кроме того, с его помощью
       вызываются функции для рисования виселицы (они находятся в файле Графикс в списке)
       каунтер_ту_траверс_сек (секвенс - последовательность) используется в главной функции
       модуля для проверки членства буквы в слове. Этот счетчик используется для обхода
       списка с буквами слова
       индекс - когда в цикле "фор i ин список_букв" i == буква, индекс - это индекс буквы,
       эта буква заменяется на '', чтобы ее больше не находило
       нью_гейм_флаг это флаг новой игры. Он становится 1, когда перезагружается игра.
       Тогда функция чек_леттер обновляет слово (берет его из Интерфейса), и снова делает
       флаг нулем
       """
       self.victory_counter = 0 
       self.defeat_counter = 0
       self.counter_to_travers_seq = 0
       self.index = 0
       self.letter = ''
       self.word = word
       self.letter_field = letter_field
       self.list_of_letters_in_word = list(self.word)
       self.list_of_str_var = list_of_str_var
       self.it_obj = it_obj
       self.player1_score = 0
       self.player2_score = 0
       self.len_word = 0
       self.new_game_flag = 0

    def reload_game(self):
        """
        эта функция начинает новую игру. Вызывает функцию
        из Интерфейса - очищает холст, генерирует новое слово,
        новый список букв, вызывает функцию создания блоков для
        нового слова
        """
        self.it_obj.clean_canvas()
        self.new_game_flag = 1
        if self.it_obj.game_flag == 0:
            self.word = random.choice(dct.dict_for_hanggame)
            self.list_of_letters_in_word = list(self.word)
            self.it_obj.create_blokcs_for_letters(self.word)
        elif self.it_obj.game_flag == 1:
            self.list_of_letters_in_word = list(self.word)
            self.it_obj.enter_the_word()
            
        
    def check_letter(self):
        """
        эта функция проверяет, есть ли буква в загадываемом слове.
        здесь же проверяется, соответстует ли набранный символ требованиям
        """
        if self.new_game_flag == 1:
            self.word = self.it_obj.get_word()
            self.len_word = len(self.word)
            self.list_of_letters_in_word = list(self.word)
            self.new_game_flag = 0
        counter_to_travers_seq = 0
        self.letter = self.letter_field.get()
        self.letter_field.delete(0, tk.END)
        if len(self.letter) == 1 and self.letter in alphabet:
            if self.letter in self.list_of_letters_in_word:
                for i in self.list_of_letters_in_word:
                    if i == self.letter:
                        self.it_obj.list_of_str_var[counter_to_travers_seq].set(self.letter)
                        self.index = self.list_of_letters_in_word.index(i)
                        self.list_of_letters_in_word[self.index] = ''
                        counter_to_travers_seq += 1
                        self.victory_counter += 1
                    else:
                        counter_to_travers_seq += 1
            else:
                self.letter_not_in_word()
            if self.victory_counter == len(self.word):
                self.victory_getted()
        else:
            self.raise_letter_error()

    def letter_not_in_word(self):
        print(self.defeat_counter)
        gr.list_of_graphics[self.defeat_counter]()
        self.defeat_counter += 1
        if self.defeat_counter == 10:
            self.victory_counter = 0
            self.defeat_counter = 0
            self.it_obj.show_word()
            defeat_answer = self.raise_new_game_offer()
            if defeat_answer == True:
                self.reload_game()
            elif defeat_answer == False:
                self.it_obj.destroy_root()
        
    def victory_getted(self):
        self.defeat_counter = 0
        self.victory_counter = 0
        if self.it_obj.player_flag == 1:
            self.player1_score += 1
            self.it_obj.str_var_for_player1.set(self.player1_score)
        if self.it_obj.player_flag == 0:
            self.player2_score += 1
            self.it_obj.str_var_for_player2.set(self.player2_score)
        victory_answer = self.victory()
        if victory_answer == True:
            self.reload_game()
        elif victory_answer == False:
            self.it_obj.destroy_root()

