import WebcamOpen

import cv2
import os

def capture_and_save_image(save_path):

    # Lưu frame vào đường dẫn cụ thể
    cv2.imwrite(os.path.join(save_path, "captured_image.jpg"), WebcamOpen.frame)



# đường dẫn thư mục
save_path = "Train_model/Checking"

# Gọi hàm để chụp ảnh và lưu vào đường dẫn
capture_and_save_image(save_path)
