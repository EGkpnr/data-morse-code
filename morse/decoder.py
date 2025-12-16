"""
This module provides functions to decode Morse code into text.

Functions:
- decode(morse_code): Decodes Morse code into text.
- decode_word(morse_word): Decodes a single word from Morse code.
"""

from morse.mapping import MORSE

MORSE_TO_LETTER = {v: k for k, v in MORSE.items()}

def decode(morse_code):
    """
    Decodes the given Morse code into text.
    Words are separated by a pipe (|) and letters by a space.
    """
    if not isinstance(morse_code, str):
        raise TypeError("Morse code must be a string")
    
    words = morse_code.split("|")
    decoded_list = [decode_word(word) for word in words]
    
    return " ".join(decoded_list)


def decode_word(morse_word):
    """
    Decodes a single word from Morse code.
    Letters are separated by a space.
    """
    letters = morse_word.split()
    decoded_chars = []
    
    for char in letters:
        if char in MORSE_TO_LETTER:
            decoded_chars.append(MORSE_TO_LETTER[char])
            
    return "".join(decoded_chars)


if __name__ == "__main__":
    print(decode_word("... --- ..."))  # SOS
    print(decode(".... . .-.. .-.. --- | .-- --- .-. .-.. -..")) # HELLO WORLD