# Python Program to Remove Punctuations From a String

from string import punctuation as punc

def punctation_remover(string):
    l = list(string)

    for i,ch in enumerate(l):
        if ch in punc:
            l.remove(ch)

    return (''.join(l))

if __name__ == '__main__':
    string = input('Enter a string for removal of punctuations : ')
    print(f"Before : {string} , After : {punctation_remover(string)}")

