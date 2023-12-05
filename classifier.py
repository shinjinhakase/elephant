from generator import Generator
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class Classifier:

    def __init__(self,model_name):
        self.category = ["male","female","land","horse","monster","none"]
        self.save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/' + model_name
        self.model = tf.keras.models.load_model(self.save_model_path)
        print("model loaded!")

    def generate(self,generate_times=30,length=2,arrow_rate=0.6,test_flag=False,cate=[]):
        gen = Generator()
        name_list = []
        while len(name_list) < generate_times:
            before_judge_list = gen.generate_list(length,request_amount=(generate_times - len(name_list)))
            vectorized_list = gen.vectorize_nparray(before_judge_list,length)
            predictions = self.model.predict(vectorized_list)
            for i in range(len(predictions)):
                # predictions[i][len(cate) - 1] = カテゴリが最後のものである確率
                if predictions[i][len(cate) - 1] < arrow_rate:
                    name_list.append(before_judge_list[i])
                    if test_flag == True:
                        print(before_judge_list[i])
                        percentage = []
                        for c in cate:
                            percentage.append(c + " " + str(round(predictions[i][cate.index(c)] * 100)) + "%")
                        print(*percentage)
            print(str(len(name_list)) + "/" + str(generate_times))
        return name_list

    def generate_for_more_learn(self,amount=100,length=2,cate=["good","bad"]):
        # 後で他カテゴリーにも対応する
        gen = Generator()
        result = []
        while len(result) < amount:
            before_judge = gen.generate_list(length,request_amount=(amount - len(result)))
            vectorized_list = gen.vectorize_nparray(before_judge,length)
            predictions = self.model.predict(vectorized_list)
            for i in range(len(predictions)):
                if predictions[i][0] > predictions[i][1]:
                    result.append([before_judge[i],cate[0]])
                else:
                    result.append([before_judge[i],cate[1]])
        return result

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
