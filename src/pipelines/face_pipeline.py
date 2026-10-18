import dlib
import numpy as np
import face_recognition_models
import streamlit as st
from PIL import Image
from src.database.db import get_all_students

MATCH_THRESHOLD = 0.58   # dlib default is 0.6; raise toward 0.6 if still missing people


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())
    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())
    return detector, sp, facerec


def _to_rgb(image_np):
    """Ensure uint8 RGB with 3 channels."""
    img = Image.fromarray(image_np).convert("RGB")
    return np.array(img, dtype=np.uint8)


def get_face_embeddings(image_np, num_jitters=5):
    detector, sp, facerec = load_dlib_models()
    image_np = _to_rgb(image_np)
    faces = detector(image_np, 1)

    encodings = []
    for face in faces:
        shape = sp(image_np, face)
        descriptor = facerec.compute_face_descriptor(image_np, shape, num_jitters)
        encodings.append(np.array(descriptor))
    return encodings


@st.cache_resource
def get_trained_model():
    X, y = [], []
    for student in get_all_students() or []:
        emb = student.get('face_embedding')
        if emb:
            X.append(np.array(emb))
            y.append(student['student_id'])

    if not X:
        return None
    return {'X': np.array(X), 'y': y}


def train_classifier():
    get_trained_model.clear()          # only clears this cache, not dlib models
    return bool(get_trained_model())


def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected = {}

    model = get_trained_model()
    if not model:
        return detected, [], len(encodings)

    X, y = model['X'], model['y']
    all_students = sorted(set(y))

    for enc in encodings:
        dists = np.linalg.norm(X - enc, axis=1)     # vectorized distance to everyone
        best = int(np.argmin(dists))
        if dists[best] <= MATCH_THRESHOLD:
            detected[y[best]] = True

    return detected, all_students, len(encodings)
