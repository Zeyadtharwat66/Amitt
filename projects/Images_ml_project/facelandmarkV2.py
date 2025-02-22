import cv2
import mediapipe as mp
image = cv2.imread(r"C:\D\Amitt\projects\Images_ml_project\13.jpg")
mp_face_mesh = mp.solutions.face_mesh
face_mesh_model = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = face_mesh_model.process(rgb_image)
image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image,
            face_landmarks,
            connections=None,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=-3 , circle_radius=3)
        )
cv2.imshow("Face Landmarks (Only Points, No Connections)", image)
cv2.waitKey(0)
cv2.destroyAllWindows()