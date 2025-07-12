# 🤖 Semantic SLAM using YOLO + OpenCV + Streamlit

This project combines **Visual SLAM** (Simultaneous Localization and Mapping) using OpenCV with real-time **object detection** using YOLOv5 to build intelligent, annotated camera maps.

✅ Built with:
- Python
- OpenCV (ORB SLAM)
- Ultralytics YOLOv5
- Streamlit
- Matplotlib

---

## 🎥 What It Does

Upload a video file and the system will:

1. Track how the camera is moving using ORB-based Visual SLAM.
2. Use YOLOv5 to detect objects in every frame (e.g., chair, person, TV).
3. Show a live trajectory map and annotated video frames.
4. All from your browser — no setup needed if deployed via Streamlit Cloud!

---

## 🖼️ Example Output

| Annotated Frame (YOLO) | Trajectory Map |
|------------------------|----------------|
| ![sample_frame](demo/frame.png) | ![trajectory_map](demo/trajectory.png) |

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/semantic-slam-yolo.git
cd semantic-slam-yolo

### 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
streamlit run app.py

🌐 Deploy on Streamlit Cloud
  1.Push this repo to your GitHub (see below 👇)
  2.Go to streamlit.io/cloud
  3.Click New App, select this repo
  4.Set app.py as the entry point
  5.Done! You’ll get a public web link to test it from your phone.

🔎 Supported Video Requirements
  .Format: .mp4, .avi
  .Duration: 5–30 seconds recommended
  .Motion: Continuous and slow camera motion
  .Content: Visible real-world objects (chairs, people, desk, etc.)
  .Lighting: Well-lit for better detection and mapping

📦 Requirements
  streamlit
  opencv-python-headless
  numpy
  matplotlib
  ultralytics
  pandas

🧪 Test Video Sources
  You can try:
  YouTube indoor walkthroughs (download using yt-dlp)
  Your own phone-recorded 10-second video
  Example:
  yt-dlp -f mp4 "https://www.youtube.com/watch?v=sZ8gqy-QiWw"

📬 About Me
Made with ❤️ by Nahid Ansari

⭐ Like this project?
  .Give it a ⭐ on GitHub
  .Fork and modify it
  .Share your output screenshots on LinkedIn and tag me!




