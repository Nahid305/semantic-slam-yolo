
import streamlit as st
import tempfile
from ultralytics import YOLO
from main import run_slam
from yolo_detect import detect_objects_yolo
import cv2

st.set_page_config(page_title="Semantic SLAM", layout="centered")
st.title("📍 Semantic SLAM: YOLO + Visual Mapping")

uploaded_file = st.file_uploader("Upload a video file (MP4 preferred)", type=["mp4", "avi"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        video_path = tmp.name

    st.info("Loading YOLOv5 model...")
    model = YOLO("yolov5s.pt")  # Uses YOLOv5 small model from Ultralytics

    st.success("Model loaded. Running SLAM + YOLO...")
    trajectory, snapshots = run_slam(video_path)

    if trajectory is not None:
        for i, (frame, traj) in enumerate(snapshots[::20]):  # Show every 20th frame
            detections = detect_objects_yolo(frame, model)
            for _, row in detections.iterrows():
                x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                label = row['name']
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
                cv2.putText(frame, label, (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
            st.image(frame, caption=f"Frame {i*20} with YOLO Annotations", channels="BGR")

        st.image(trajectory, caption="Trajectory Map", use_column_width=True)
    else:
        st.error("Could not process video. Try another file.")