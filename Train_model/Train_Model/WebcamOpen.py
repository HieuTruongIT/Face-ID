import cv2 # thư viện mở webcam

cap=cv2.VideoCapture(0)      # mở webcam
#hàm kiểm tra đã mở web cam chưa ?
if not cap.isOpened():
    print("can't opend webcam")
    exit()  
#vòng lập vô tận 
while True:
    ret,frame = cap.read()
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # nhận q trên bàn phím để thoát
        break
cap.release()   
cv2.destroyAllWindows()
