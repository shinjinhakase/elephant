from generator import Generator
from classifier import Classifier
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# category = ["male","female","land","horse","monster","none"]
# not_arrowed_cat = 5
category = ["good","bad"]
not_arrowed_cat = 1
generate_times = 30
arrow_rate = 0.6
LENGTH = 2

save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/' + str(LENGTH) + 'let_gb_model'
model = tf.keras.models.load_model(save_model_path)
print("model loaded!")

gen = Generator()
name_list = []
vertorized_name_list = []
for i in range(generate_times):
    name_list.append(gen.generate(length=LENGTH))
for i in range(generate_times):
    vertorized_name_list.append(gen.vectorize(name_list[i],LENGTH))
predictions = model.predict(np.array(vertorized_name_list))
max_indexes = np.argmax(predictions,axis=1)

for i in range(generate_times):
    ans = "{0} is maybe {1}".format(name_list[i],category[max_indexes[i]])
    if category[max_indexes[i]] == "none" and predictions[i][not_arrowed_cat] < arrow_rate:
        ans += " but by any chance {0}".format(category[np.argmax(predictions[i][0:not_arrowed_cat])])
    print(ans)
    percentage = []
    for c in category:
        percentage.append(c + " " + str(round(predictions[i][category.index(c)] * 100)) + "%")
    print(*percentage)

print("---------------------------------")
print("arrow rate {0}% test".format(round(arrow_rate * 100)))
print("---------------------------------")

cla = Classifier(str(LENGTH) + 'let_gb_model')
a = cla.generate(generate_times,LENGTH,arrow_rate,test_flag=True,cate=category)
