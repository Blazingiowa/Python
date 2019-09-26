import MeCab
import os, json, random

dict_file = "markov_dict.json"
dic = {}


def regist_dic(wordlist):
    global dic
    w1 = ""
    w2 = ""

    if len(wordlist) < 3: return

    for w in wordlist:
        word = w[0]
        if word == "" or word == "\r\n" or word == "\n": continue

        if w1 and w2:
            set_dic(dic, w1, w2, word)

        if word == "。" or word == "？" or word == "?":
            w1 = ""
            w2 = ""
            continue

        w1, w2 = w2, word

    json.dump(dic, open(dict_file, "w", encoding="utf=8"))


def set_dic(dic, w1, w2, w3):
    if w1 not in dic: dic[w1] = {}
    if w2 not in dic[w1]: dic[w1][w2] = {}
    if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0

    dic[w1][w2][w3] += 1


def make_response(word):
    res = []

    w1 = word
    res.append(w1)
    w2 = word_choice(dic[w1])
    res.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        res.append(w3)

        if w3 == "。" or w3 == "?" or w3 == "？" or w3 == "": break
        w1, w2 = w2, w3

    return "".join(res)


def word_choice(candidate):
    keys = candidate.keys()
    return random.choice(list(keys))


if os.path.exists(dict_file):
    dic = json.load(open(dict_file, "r"))

while True:
    text = input("You->")
    if text == "" or text == "さようなら":
        print("Bot-> さようなら")
        break

    if text[-1] != "。" and text[-1] != "?" and text[-1] != "？": text += "。"

    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse("")
    node = tagger.parseToNode(text)

    wordlist = []
    while node is not None:
        hinshi = node.feature.split(",")[0]
        if hinshi not in ["BOS/EOS"]:
            wordlist.append([node.surface, hinshi])
        node = node.next

    regist_dic(wordlist)

    for w in wordlist:
        word = w[0]
        hinshi = w[1]

        if hinshi in ["感動詞"]:
            print("Bot->" + word)
            break

        elif (hinshi in ["名詞", "形容詞", "動詞"]) and (word in dic):
            print("Bot->" + make_response(word))
            break
