import Dictionary as dct
import random
import Interface as it
import GetLetter as gl
import Graphics as gr


def main():
    word = random.choice(dct.dict_for_hanggame)
    list_of_letters = list(word)
    interface_object = it.Interface(word)
    answer_2or1_player = interface_object.two_player_offer()
    if answer_2or1_player == True:
        interface_object.enter_names()
        interface_object.create_scoreboard()
    else:
        interface_object.create_blokcs_for_letters(word)
    gr.CANVAS = interface_object.canvas
    interface_object.root.mainloop()

main()

