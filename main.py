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
        str = str.replace(i, "{} ".format(dictionary[i]))
    return str

def unMorsIt(str):
    str = str.split(" ")
    a = 0
    for i in dictionary:
        if a >= len(str):
            break
        for mors in str:
            if(mors == dictionary[i]):
                str[str.index(mors)] = mors.replace(dictionary[i], i)
    for i in str:
        if i == "":
            str[str.index(i)] = " "
    return "".join(str)
