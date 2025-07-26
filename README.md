# QR Code Reader Bot (ROS 2 - Humble)

This project is a basic ROS 2 (Humble) implementation of a QR Code Reader Bot using a webcam. It subscribes to camera image topics and detects QR codes using OpenCV and `pyzbar`. Ideal for beginners in ROS 2 vision projects.

## ✅ Features Completed
- Created ROS 2 Python package `qrcode_bot`
- Used `v4l2_camera` to access the laptop camera
- Subscribed to `/image_raw` topic using `image_transport`
- Detected and decoded QR codes using OpenCV + pyzbar
- Displayed output via `cv2.imshow()` and ROS 2 logs

## 🔧 Technologies Used
- ROS 2 Humble
- Python 3
- OpenCV
- pyzbar
- v4l2_camera package

## 🛠️ To-Do (Future)
- Add robot movement based on QR code content
- Add GUI overlay for visual feedback
- Launch file for automated setup
