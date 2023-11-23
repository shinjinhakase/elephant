from data import *
from generator import Generator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

csv_file_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/data/csv_data.csv'
df = pd.read_csv(csv_file_path)
name_list = df['name']

get_data = []
gen = Generator()
for name in name_list:
    vectorized_name = gen.vectorize(name)
    get_data.append(vectorized_name)
input_data = np.array(get_data)
print(input_data)

output_data = df.drop('name', axis=1).values
print(output_data)

# ニューラルネットワークのモデル構築
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10,)))
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

save_model_path = 'C:/Users/shinj/Documents/Develop_Python/elephant/models'
model.save(save_model_path)
print("model save completed!")