import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np

# import file bên ngoài
import identification  # chưa xử dụng

# Tải mô hình đã lưu
loaded_model = tf.keras.models.load_model('image_recognition_model.h5')

# Tải và tiền xử lý hình ảnh mới
new_image_path = 'đường/dẫn/đến/hình/ảnh/mới.jpg'
new_image = cv2.imread(new_image_path)
new_image = cv2.resize(new_image, (150, 150))
new_image = np.expand_dims(new_image, axis=0) / 255.0  # Chuẩn hóa giá trị pixel

# Đưa ra dự đoán
prediction = loaded_model.predict(new_image)

# Tương tác với cơ sở dữ liệu dựa trên kết quả nhận diện
if prediction > 0.5:  # Giả sử ngưỡng cho lớp tích cực là 0.5
    # Lấy thông tin từ cơ sở dữ liệu bằng cách sử dụng mô-đun identification
    result_info = identification.fetch_info_from_database()
    print("Thông tin từ cơ sở dữ liệu:", result_info)
else:
    print("Hình ảnh không được nhận diện.")
