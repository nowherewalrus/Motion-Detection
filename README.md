# 🚗 Real-Time Motion Detection System

A computer vision application that detects and tracks moving objects in video streams using background subtraction. This system is particularly useful for traffic monitoring, security surveillance, and motion analysis.


## 📋 Features

- **Background Subtraction**: Uses MOG2 algorithm for robust motion detection
- **Real-time Processing**: Processes video streams with minimal latency
- **Noise Reduction**: Implements Gaussian blur and thresholding for clean detection
- **Object Tracking**: Draws bounding boxes around detected moving objects
- **Adaptive Scaling**: Adjustable frame resizing for performance optimization
- **Multiple Input Sources**: Works with webcams, video files, and IP cameras

## 🛠️ Technologies Used

- **OpenCV**: Computer vision library for image processing
- **Python**: Main programming language
- **NumPy**: Numerical operations on image data
- **MOG2 Algorithm**: Mixture of Gaussians for background subtraction

## 📁 Project Structure

```
motion-detection/
├── main.py      # Main application file
├── requirements.txt         # Dependencies
├── README.md               # This file
├── street_camera.mp4       # Sample video (optional)
```

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nowherewalrus/Motion-Detection.git
cd main
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage
Run the motion detection on a video file:
```bash
python main.py
```

### Using Different Video Sources

1. **Webcam** (default):
```python
cap = cv.VideoCapture(0)  # 0 for default camera
```

2. **Video File**:
```python
cap = cv.VideoCapture('your_video.mp4')
```

3. **IP Camera**:
```python
cap = cv.VideoCapture('street_camera.mp4')
```

### Controls
- **ESC**: Exit the application
- **Frame Scaling**: Adjust the `percent` parameter in `rescale_frame()` function
- **Detection Sensitivity**: Modify `cv.contourArea(contour) > 3000` threshold

## 🔧 Configuration

### Adjustable Parameters

| Parameter | Location | Default | Description |
|-----------|----------|---------|-------------|
| Frame Scale | `rescale_frame(percent=20)` | 20% | Reduce for better performance |
| Blur Kernel | `cv.GaussianBlur(fg_mask, (9, 9), 0)` | (9, 9) | Adjust for noise reduction |
| Threshold | `cv.threshold(fg_mask, 50, 255)` | 50 | Motion sensitivity |
| Min Area | `cv.contourArea(contour) > 3000` | 3000 | Minimum object size |
| Bounding Box Offset | `(x + w - 100, y + h - 50)` | (100, 50) | Rectangle positioning |

### Customizing Detection

To adjust the motion detection sensitivity, modify these key parameters:

```python
# For more sensitive detection (smaller objects)
if cv.contourArea(contour) > 1000:  # Reduced from 3000

# For less sensitive detection (larger objects only)
if cv.contourArea(contour) > 5000:  # Increased from 3000

# Adjust motion detection threshold
_, mask = cv.threshold(fg_mask, 30, 255, cv.THRESH_BINARY)  # More sensitive
```

## 📊 How It Works

### Algorithm Pipeline

1. **Frame Capture**: Read video frames from source
2. **Resizing**: Scale down frames for faster processing
3. **Background Subtraction**: Apply MOG2 algorithm to detect foreground
4. **Noise Reduction**: Use Gaussian blur to smooth the mask
5. **Thresholding**: Convert to binary image
6. **Contour Detection**: Find boundaries of moving objects
7. **Filtering**: Remove small contours (noise)
8. **Visualization**: Draw bounding boxes around detected motion
9. **Display**: Show processed frames in real-time

### MOG2 Algorithm
The Mixture of Gaussians (MOG2) algorithm:
- Models each pixel as a mixture of Gaussian distributions
- Adapts to lighting changes and dynamic backgrounds
- Maintains a history of pixel values
- Classifies pixels as background or foreground

## 📈 Performance Optimization

### For Better Performance:
```python
# Reduce frame size further
resized_frame = rescale_frame(frame, percent=15)

# Use simpler background subtractor
backSub = cv.createBackgroundSubtractorKNN()

# Skip frames for faster processing (add frame counter)
frame_counter = 0
if frame_counter % 2 == 0:  # Process every other frame
    # processing code
frame_counter += 1
```

### For Better Accuracy:
```python
# Increase frame size for more detail
resized_frame = rescale_frame(frame, percent=40)

# Use morphological operations to clean mask
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
```

## 🧪 Testing

### Test with Sample Videos
1. Download sample traffic videos
2. Place in project directory
3. Update the video file path in the code

### Test Different Scenarios
- Indoor vs outdoor environments
- Daytime vs nighttime lighting
- Crowded vs sparse scenes
- Fast vs slow moving objects

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- OpenCV community for the excellent computer vision library
- Contributors to the background subtraction algorithms
- Sample video providers for testing purposes

## 📞 Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Contact: pkhaghani916@example.com

## 🔮 Future Enhancements

- [ ] Object classification (car, person, animal)
- [ ] Speed estimation for moving objects
- [ ] Direction tracking and path prediction
- [ ] Multiple camera support
- [ ] Web interface for remote monitoring
- [ ] Data logging and analytics
- [ ] Alert system for specific motion patterns

## 📚 Additional Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [Background Subtraction Techniques](https://docs.opencv.org/3.4/db/d5c/tutorial_py_bg_subtraction.html)
- [Computer Vision Tutorials](https://pyimagesearch.com/)

---

**Note**: Replace `street_camera.mp4` with your own video file or modify the code to use a webcam by changing `cv.VideoCapture('street_camera.mp4')` to `cv.VideoCapture(0)`.

**Happy Motion Detecting!** 🎥🚶🚗
