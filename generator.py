import random

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
            "ダ", "ヂ", "ヅ", "デ", "ド",
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
        self.little_letter = [
            "ャ", "ュ", "ョ"
        ]

    def generate(self):
        length = random.randint(2, 10)
        name = ""
        for i in range(length):
            name += self.char_list[random.randint(0, len(self.char_list) - 1)]
        return name

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

    def vectorize(self,name):
        vectorized_name = []
        split_name = self.char_split(name)
        for letter in split_name:
            vectorized_name.append(self.char_list.index(letter))
        while len(vectorized_name) < 10:
            vectorized_name.append(0)
        return vectorized_name
