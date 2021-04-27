import random
from urllib.request import urlopen
abc = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ABC = ["A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = [abc, ABC, nums]

class TgAccount():

    def __init__(self, letters_count):
        global abc
        global ABC
        global symbols
        self.link = "https://t.me/"
        for i in range(letters_count):
            lisT = random.randint(0, 1)
            letter = random.randint(0, len(abc) - 1)
            self.link = self.link + symbols[lisT][letter]
        self.html = str(urlopen(self.link).read(), "utf-8")
        self.exists = True
        self.info = {
            "link": self.link,
            "exists": self.exists,
            "desc": self.html.split('<meta property="og:description" content="')[1].split('"')[0]
        }
        if '"og:description" content=""' in self.html:
            # print(html)
            self.exists = False
        self.info["exists"] = self.exists
def generate(count, letters_count):
    for i in range(count):
        info = TgAccount(letters_count).info
        if info["exists"]:
            print(info["link"])
            print(info["desc"])
# https://us02web.zoom.us/j/337352510?pwd=c21XWUkrZjRHWFlNMGxlaWNCSDJMQT09
# https://us02web.zoom.us/j/118501324?pwd=CJikgef8r7AcjAq9077uF95W3lTuFr33
# https://us02web.zoom.us/j/277724480?pwd=6j8Wr7Bz80H4rKSc8AtMu67kOt6KMs9B  
class ZoomLink():
    def __init__(self):
        self.link = "https://us02web.zoom.us/j/"
        for i in range(9):
            num = random.randint(0, 8)
            self.link = self.link + str(symbols[2][num])
        self.link = self.link+ "?pwd="
        for i in range(32):
            sym = random.randint(0, 2)
            num = random.randint(0, len(symbols[sym]) - 1)
            self.link = self.link + str(symbols[sym][num])
        self.html = str(urlopen(self.link).read())
        print(self.link)

def choose(q):
    quest = input(q)
    isTrue = None
    if quest == "y":
        isTrue = True
    elif quest == 'n':
        isTrue = False
    return isTrue

def main():
    executed = True
    while executed:
        mode = input("какие ссылки вы бы хотели генерировать?(z/t): ")
        if mode == "t":
            count = int(input("кол-во генерируемых аккаунтов: "))
            letters_count = int(input("скольки-значные ники генерировать: "))

            generate(count, letters_count)
        elif mode == "z":
            for i in range(100):
                link = ZoomLink()
        executed = choose("продолжить? (y/n) ")
main()