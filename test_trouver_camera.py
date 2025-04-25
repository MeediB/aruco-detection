import cv2

# Teste les indices de caméra de 0 à 5
for i in range(1,15):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Caméra trouvée à l'index {i}")
        cap.release()
    else:
        print(f"Aucune caméra trouvée à l'index {i}")