import random
import numpy as np

class Generator:

    def __init__(self):
        self.char_list = [
            "ア", "イ", "ウ", "エ", "オ",
            "カ", "キ", "ク", "ケ", "コ",
            "サ", "シ", "ス", "セ", "ソ",
            "タ", "チ", "ツ", "テ", "ト",
            "ナ", "ニ", "ヌ", "ネ", "ノ",
            "ハ", "ヒ", "フ", "ヘ", "ホ",
            "マ", "ミ", "ム", "メ", "モ",
            "ヤ", "ユ", "ヨ",
            "ラ", "リ", "ル", "レ", "ロ",
            "ワ", "ン", "ッ", "ー", "ヴ",
            "ガ", "ギ", "グ", "ゲ", "ゴ",
            "ザ", "ジ", "ズ", "ゼ", "ゾ",
            "ダ", "デ", "ド",
            "バ", "ビ", "ブ", "ベ", "ボ",
            "パ", "ピ", "プ", "ペ", "ポ",
            "ァ", "ィ", "ゥ", "ェ", "ォ",
            "キャ", "キュ", "キョ",
            "シャ", "シュ", "ショ",
            "チャ", "チュ", "チョ",
            "ニャ", "ニュ", "ニョ",
            "ヒャ", "ヒュ", "ヒョ",
            "ミャ", "ミュ", "ミョ",
            "リャ", "リュ", "リョ",
            "ギャ", "ギュ", "ギョ",
            "ジャ", "ジュ", "ジョ",
            "ビャ", "ビュ", "ビョ",
            "ピャ", "ピュ", "ピョ"
        ]
        self.no_head = [
            "ン", "ッ", "ー", "ァ", "ィ", "ゥ", "ェ", "ォ"
        ]
        self.no_chain = [
            "ッ", "ー", "ァ", "ィ", "ゥ", "ェ", "ォ", "ャ", "ュ", "ョ"
        ]
        self.little_letter = [
            "ャ", "ュ", "ョ"
        ]

    def generate(self,length=random.randint(2,10)):
        name = ""
        while len(self.char_split(name)) < length:
            new_char = self.char_list[random.randint(0, len(self.char_list) - 1)]
            if name == "":
                if new_char in self.no_head:
                    continue # 頭に来ない文字が頭に来たら引き直し
            if len(self.char_split(name)) >= 1:
                last_char = name[len(name) - 1]
                if last_char in self.no_chain and new_char in self.no_chain:
                    continue # 連続しない文字が連続したら引き直し
            if len(self.char_split(name)) >= 2:
                last_char = name[len(name) - 1]
                last2_char = name[len(name) - 2]
                if last_char == last2_char and last_char == new_char:
                    continue # 3文字同じ文字が連続したら引き直し
            if len(self.char_split(name)) == length - 1:
                if new_char == "ッ":
                    continue # 小さいツで終わろうとしていたら引き直し
            name += new_char
        return name

    def generate_list(self,length_limit=10,request_amount=10):
        name_list = []
        for i in range(request_amount):
            name_list.append(self.generate(random.randint(2,length_limit)))
        return name_list

    def char_split(self,name):
        split_name = list(name)
        answer = []
        check = len(split_name) - 1
        while 0 <= check:
            if split_name[check] in self.little_letter:
                answer.append(split_name[check - 1] + split_name[check])
                check -= 2
            else:
                answer.append(split_name[check])
                check -= 1
        answer.reverse()
        return answer

    def vectorize(self,name,requested_size):
        vectorized_name = []
        split_name = self.char_split(name)
        for letter in split_name:
            vectorized_name.append(self.char_list.index(letter))
        while len(vectorized_name) < requested_size:
            vectorized_name.append(0)
        return vectorized_name

    def vectorize_nparray(self,name_list,requested_size):
        vec_list = []
        for name in name_list:
            vec_list.append(self.vectorize(name,requested_size))
        return np.array(vec_list)

    def colocation(self,name,is_predict=False):
        split_name = self.char_split(name)
        colocated_list = []
        for i in range(len(split_name)):
            if not i == len(split_name) - 1:
                colocated_list.append([self.char_list.index(split_name[i]),self.char_list.index(split_name[i + 1])])
        if is_predict:
            return np.array(colocated_list)
        return colocated_list
