import cv2

cap = cv2.VideoCapture(0) # Keep at 0

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            # Check for specific OpenCV errors here if possible
            break

        cv2.imshow('Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()