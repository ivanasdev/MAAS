import cv2
import time

#Detectar rostros

def abrir_camara_reconocimiento():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Reconocimiento Facial', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def abrir_camara_y_reconocer_rostros():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return {"error": "No se pudo abrir la cámara"}

    # Cargar el modelo preentrenado Haar Cascade para detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Configurar grabación
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_faces.mp4', fourcc, 20.0, (640, 480))

    start_time = time.time()
    seconds_to_record = 5

    while int(time.time() - start_time) < seconds_to_record:
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir a escala de grises (mejor para detección)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostros
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Dibujar rectángulos alrededor de las caras detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        out.write(frame)  # Guardar el frame modificado (con rectángulos)

        # Si quieres también verlo en vivo mientras graba
        cv2.imshow('Reconocimiento Facial', frame)

        # Salir si presionas 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return {"message": "Grabación y reconocimiento completos", "video_path": "output_faces.mp4"}

def abrir_camara_y_grabar():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return {"error": "No se pudo abrir la cámara"}

    # Configurar grabación para MP4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec mp4v para archivos .mp4
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    start_time = time.time()
    seconds_to_record = 5  # segundos a grabar

    while int(time.time() - start_time) < seconds_to_record:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)  # Guardar el frame en el archivo de video

    cap.release()
    out.release()

    return {"message": "Grabación completa", "video_path": "output.mp4"}