# 👁️ Eye Tracking Mouse Control(XEyeTracker)

Control your computer mouse and perform actions using just your eyes and head movements! This Python application uses your webcam to track eye movements for cursor control, detect blinks for clicking, and recognize head nods for scrolling.

## ✨ Features

- **👀 Eye-Controlled Cursor**: Move your mouse cursor by looking around the screen
- **😉 Blink to Click**: Close your left eye to perform a mouse click
- **🙂 Head Nod Scrolling**: 
  - Nod down to scroll down
  - Nod up to scroll up
- **🎯 Smooth Movement**: Built-in cursor smoothing for precise control

## 📦 Required Packages

Before running the application, install these dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

**requirements.txt**:
```
opencv-python
mediapipe
pyautogui
```
You can also use opencv-contrib-python instead of opencv-python.
## 🚀 How to Use

### 1. Fork & Clone the Repository

```bash
# Fork this repo on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/eye-tracking-control.git
cd eye-tracking-control
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python eye_tracking_control.py
```

### 4. Controls

- **Move cursor**: Look at different parts of your screen
- **Click**: Blink your left eye
- **Scroll down**: Nod your head down
- **Scroll up**: Nod your head up
- **Exit**: Press `ESC` key

## ⚙️ Customization

You can adjust these parameters in the code for better performance:

- `smooth_limit`: Number of points averaged for smoother cursor movement (default: 5)
- `nod_threshold`: Sensitivity of head nod detection (default: 0.015)
- Blink threshold: Adjust the value `0.004` for click sensitivity

## 🖥️ System Requirements

- **Python**: 3.7 or higher but lower than 3.12(as mediapipe got depreciated in 3.12 releases)
- **Webcam**: Required for face tracking
- **OS**: Windows, macOS, or Linux

## ⚠️ Important Notes

- Ensure good lighting for accurate face tracking
- Position yourself at a comfortable distance from the webcam
- The application needs camera permissions to run
- Cursor control may take a moment to calibrate to your movements

## 🛠️ Technologies Used

- **OpenCV**: Video capture and image processing
- **MediaPipe**: Face mesh detection and landmark tracking
- **PyAutoGUI**: Mouse control automation

## 📝 License

MIT License - Feel free to modify and distribute!

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---
