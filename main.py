"""
Motion Detection using Background Subtraction
This script captures live video from a webcam and detects moving objects
using the MOG2 background subtraction algorithm.
"""

import cv2 as cv

# Initialize video capture from default webcam (camera index 0)
cap = cv.VideoCapture('street_camera.mp4')

# Create background subtractor using MOG2 algorithm
# MOG2 (Mixture of Gaussians) is effective for dynamic background subtraction
backSub = cv.createBackgroundSubtractorMOG2()


def rescale_frame(frame, percent=20):
    """
    Resize frame to specified percentage of original dimensions.

    Parameters:
    frame (numpy.ndarray): Input video frame
    percent (int): Percentage to scale the frame (default: 60%)

    Returns:
    numpy.ndarray: Resized frame
    """
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


# Main processing loop
while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        print('Video is unavailable!')
        break

    # Resize frame for faster processing
    resized_frame = rescale_frame(frame)

    # Apply background subtraction to get foreground mask
    # The mask will be white where motion is detected, black for background
    fg_mask = backSub.apply(resized_frame)

    # Apply Gaussian blur to reduce noise in the foreground mask
    # Kernel size (9,9) determines the amount of smoothing
    fg_mask = cv.GaussianBlur(fg_mask, (9, 9), 0)

    # Apply binary threshold to create a clear separation between foreground and background
    # Pixels with value > 50 become white (255), others become black (0)
    _, mask = cv.threshold(fg_mask, 50, 255, cv.THRESH_BINARY)

    # Find contours in the binary mask
    # Contours are curves joining continuous points along boundaries
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Process each detected contour
    for contour in contours:
        # Filter contours by area to avoid detecting small noise as motion
        if cv.contourArea(contour) > 3000:  # Minimum area threshold
            # Get bounding rectangle coordinates for the contour
            (x, y, w, h) = cv.boundingRect(contour)

            # Draw a rectangle around the detected motion area
            # The rectangle is drawn with an offset to highlight a specific region
            cv.rectangle(resized_frame,
                         (x + w - 100, y + h - 50),  # Top-left corner (with offset)
                         (x + w, y + h),  # Bottom-right corner
                         (0, 0, 155),  # Color (dark blue in BGR format)
                         2)  # Thickness

    # Display the processed frame with motion detection overlay
    cv.imshow('Motion Detection', resized_frame)

    # Check for key press
    key = cv.waitKey(5)
    if key == 27:  # ESC key (ASCII code 27) to exit
        break

# Release resources
cap.release()
cv.destroyAllWindows()