from generator import Generator
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class Classifier:

    def __init__(self):
        self.category = ["male","female","land","horse","monster","none"]
        self.save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/two_letter_model'
        self.model = tf.keras.models.load_model(self.save_model_path)
        print("model loaded!")

    def generate(self,generate_times=30,length=2,arrow_rate=0.6,test_flag=False):
        gen = Generator()
        name_list = []
        while len(name_list) < generate_times:
            before_judge_list = gen.generate_list(length,request_amount=(generate_times - len(name_list)))
            vectorized_list = gen.vectorize_nparray(before_judge_list,length)
            predictions = self.model.predict(vectorized_list)
            for i in range(len(predictions)):
                # predictions[i][5] = カテゴリがnoneである確率
                if predictions[i][5] < arrow_rate:
                    name_list.append(before_judge_list[i])
                    if test_flag == True:
                        print(before_judge_list[i])
                        percentage = []
                        for c in self.category:
                            percentage.append(c + " " + str(round(predictions[i][self.category.index(c)] * 100)) + "%")
                        print(*percentage)
            print(str(len(name_list)) + "/" + str(generate_times))
        return name_list

    def treasure(self,generate_times=30,length=2,arrow_rate=0.7):
        gen = Generator()
        name_list = []
        while len(name_list) < generate_times:
            before_judge_list = gen.generate_list(length, request_amount=(generate_times - len(name_list)))
            vectorized_list = gen.vectorize_nparray(before_judge_list,length)
            predictions = self.model.predict(vectorized_list)
            for i in range(len(predictions)):
                # predictions[i][5] = カテゴリがnoneである確率
                if predictions[i][5] > arrow_rate:
                    name_list.append(before_judge_list[i])
            print(str(len(name_list)) + "/" + str(generate_times))
        return name_list
