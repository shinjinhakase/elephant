from generator import Generator
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

category = ["male","female","land","horse","monster","none"]

save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/models'
model = tf.keras.models.load_model(save_model_path)
print("model loaded!")

generate_times = 30
gen = Generator()
name_list = []
vertorized_name_list = []
for i in range(generate_times):
    name_list.append(gen.generate())
for i in range(generate_times):
    vertorized_name_list.append(gen.vectorize(name_list[i]))
predictions = model.predict(np.array(vertorized_name_list))
max_indexes = np.argmax(predictions,axis=1)

for i in range(generate_times):
    print("{0} is maybe {1}".format(name_list[i],category[max_indexes[i]]))
