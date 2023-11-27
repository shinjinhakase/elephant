from generator import Generator
from classifier import Classifier
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

category = ["male","female","land","horse","monster","none"]

save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/two_letter_model'
model = tf.keras.models.load_model(save_model_path)
print("model loaded!")

generate_times = 30
gen = Generator()
name_list = []
vertorized_name_list = []
for i in range(generate_times):
    name_list.append(gen.generate(length=2))
for i in range(generate_times):
    vertorized_name_list.append(gen.vectorize(name_list[i],2))
predictions = model.predict(np.array(vertorized_name_list))
max_indexes = np.argmax(predictions,axis=1)

for i in range(generate_times):
    ans = "{0} is maybe {1}".format(name_list[i],category[max_indexes[i]])
    if category[max_indexes[i]] == "none" and predictions[i][5] < 0.6:
        ans += " but by any chance {0}".format(category[np.argmax(predictions[i][0:5])])
    print(ans)
    percentage = []
    for c in category:
        percentage.append(c + " " + str(round(predictions[i][category.index(c)] * 100)) + "%")
    print(*percentage)

arrow_rate = 0.4
print("---------------------------------")
print("arrow rate {0}% test".format(arrow_rate * 100))
print("---------------------------------")

cla = Classifier()
a = cla.generate(30,2,arrow_rate,True)

