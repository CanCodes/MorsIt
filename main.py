# Q: Why did you even make this Can???
# A: Cause I was bored and trying to learn Mors Alphabet and I am dumb.

dictionary = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "y": "-.--",
    "z": "--..",
    "x": "-..-",
    "w": ".--",
    "ö": "---.",
    # "ı": "",
    # "ş": "",
    "q": "--.-",
    # "ğ": "",
    "ü": "..--",
    # "ç": "",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}
def morsIt(str):
    str.lower()
    for i in dictionary:
        str = str.replace(i, dictionary[i])
    return str