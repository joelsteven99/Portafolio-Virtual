import cv2
import mediapipe as mp
import time

class FaceMeshDetector:
    def __init__(self, maxFace=1):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=maxFace)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(rgb_img)
        faces = []
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                face = []
                for lm in faceLms.landmark:
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append((x, y))
                faces.append(face)
                self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)
        return img, faces

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Cambia el backend de captura de video
    pTime = 0
    detector = FaceMeshDetector(maxFace=1)

    while True:
        ret, img = cap.read()
        if not ret:
            print("Error al capturar el fotograma")
            break
        img, faces = detector.findFaceMesh(img)

        if len(faces) != 0:
            print(faces[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
