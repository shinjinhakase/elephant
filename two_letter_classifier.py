from data.two_letter_data import *
from generator import Generator
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

csv_files_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/data/two_letter_data/*.csv'
df = pd.DataFrame(columns=["name","male","female","land","horse","monster","none"])
for csv_path in glob.glob(csv_files_path):
    read_new_df = pd.read_csv(csv_path)
    print("loaded {0}".format(csv_path))
    df = pd.concat([df,read_new_df])
name_list = df['name']

get_data = []
gen = Generator()
for name in name_list:
    vectorized_name = gen.vectorize(name,2)
    get_data.append(vectorized_name)
input_data = np.array(get_data,dtype='float32')
print(input_data)

output_data = df.drop('name', axis=1).values.astype('float32')
print(output_data)

# ニューラルネットワークのモデル構築
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(2,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(6, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

input_train, input_test, output_train, output_test = train_test_split(input_data, output_data, test_size=0.2, random_state=42)

history = model.fit(input_data, output_data, epochs=30, batch_size=50)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.xlabel('Epoch')
plt.legend()
plt.show()

save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/two_letter_model'
model.save(save_model_path)
print("model save completed!")