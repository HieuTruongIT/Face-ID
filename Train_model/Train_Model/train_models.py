import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# import file bên ngoài
import identification  # chưa xử dụng

# build mô hình học máy
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))

# biên dịch mô hình
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# chuẩn bị dữ liệu
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'DataBase/image',
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary'
)

# lấy hình ảnh test bằng đường dẫn
validation_generator = test_datagen.flow_from_directory(
    'Train_model/Checking',
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary'
)

# huấn luyện mô hình
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# lưu mô hình
model.save('image_recognition_model.h5')
