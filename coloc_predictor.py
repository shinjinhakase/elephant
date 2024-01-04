from generator import Generator
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

class ColocPredictor:

    def __init__(self):
        self.gen = Generator()
        self.save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/coloc_gb_model'
        self.model = tf.keras.models.load_model(self.save_model_path)

    def generate_sort(self,length_limit=2,amount=100):
        result = []
        name_list = self.gen.generate_list(length_limit=length_limit,request_amount=amount)
        for name in name_list:
            result.append(self.predict(name))
        return sorted(result,key=lambda x: x[2],reverse=True)

    def predict(self,name):
        cate = ["good", "bad"]
        coloc_list = self.gen.colocation(name,is_predict=True)
        coloc_pred = self.model.predict(coloc_list)
        pred_np = np.array(coloc_pred)
        good_percentage = np.mean(pred_np,axis=0)[0]
        bad_percentage = np.mean(pred_np,axis=0)[1]
        if good_percentage > bad_percentage:
            return [name, cate[0], round(good_percentage * 100)]
        else:
            return [name, cate[1], round(good_percentage * 100)]

