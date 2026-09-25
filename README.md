# 📸 SNAPCLASS — AI-Powered Classroom Attendance System

SNAPCLASS is a modern, multi-modal attendance system built with **Streamlit**, **Supabase**, **dlib**, and **facial/voice recognition pipelines**. It allows teachers to effortlessly take classroom attendance via photo uploads or voice prompts, while providing students with an automated biometric portal for registration and enrollment tracking.

---

## ✨ Features

### 👨‍🏫 Teacher Module
* **Multi-Modal Attendance:**
  * **Face Recognition Pipeline:** Upload or capture classroom photos to detect and mark multiple enrolled students simultaneously using dlib facial feature embeddings.
  * **Voice Recognition Pipeline:** Record or upload audio clips to verify presence using student voice signatures.
* **Subject Management:** Create subjects, generate shareable join codes, and create instant QR codes for quick student joining.
* **Attendance Analytics:** View consolidated reports, total attendance counts, and timestamped historical logs.

### 👨‍🎓 Student Module
* **Biometric Login & Onboarding:** Login instantly via camera feed scanning; un-registered faces are seamlessly prompted to create a profile and save facial/voice embeddings.
* **Subject Self-Enrollment:** Enroll in courses using subject join codes or direct link parsing (`?join-code=...`).
* **Attendance Tracker:** Track total classes and attendance stats across all enrolled subjects.

---

## 🛠️ Tech Stack

* **Frontend Framework:** [Streamlit](https://streamlit.io/)
* **Database & Auth:** [Supabase](https://supabase.com/) (PostgreSQL backend)
* **Computer Vision / AI:**
  * `dlib` & `face_recognition_models` (128-dimensional facial embeddings)
  * `scikit-learn` (SVC classifier for face identification)
* **QR Code Generation:** `segno`
* **Data Handling:** `pandas`, `numpy`, `Pillow`
* **Security:** `bcrypt` for password hashing

---

## 📁 Project Structure

```text
SNAPCLASS/
├── app.py                            # Main application routing
├── config.py                         # Supabase configuration & credentials
├── db.py                             # Database interactions (CRUD ops)
├── face_pipeline.py                  # dlib face detection & classification
├── voice_pipeline.py                 # Voice embedding extraction & matching
├── home_screen.py                    # Home page portal selection
├── student_screen.py                 # Student dashboard & biometric login
├── teacher_screen.py                 # Teacher dashboard, attendance scanning & records
├── dialog_add_photo.py               # Photo capture/upload dialog
├── dialog_attendance_results.py      # Attendance preview & confirmation dialog
├── dialog_auto_enroll.py             # QR link quick enrollment dialog
├── dialog_create_subject.py          # Subject creation dialog
├── dialog_enroll.py                  # Student manual code enrollment dialog
├── dialog_share_subject.py           # QR code generator & link sharing dialog
├── dialog_voice_attendance.py        # Audio processing dialog
├── base_layout.py                    # Global CSS styling & layout rules
├── footer.py                         # UI dashboard footer component
├── header.py                         # UI dashboard header component
└── subject_card.py                   # Reusable UI component for course display
