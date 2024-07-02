# cv-bounding-box

This Python script creates an adjustable, always-on-top window using Tkinter that captures the screen area directly below it and performs Optical Character Recognition (OCR) using Tesseract. The recognized text is printed to the console every 3 seconds. The script is also DPI aware to handle different screen scaling settings.

## Features
- Always-on-top, adjustable Tkinter window
- Captures the screen area directly below the window
- Performs OCR using Tesseract and prints the recognized text
- Dynamic resizing and dragging of the window
- Handles DPI scaling

## Prerequisites
- Python 3.x
- Tesseract OCR installed and added to the system path

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/zacharylyj/cv-bounding-box.git
cd cv-bounding-box
```

2. **Install required Python packages:**

```bash
pip install pytesseract pillow opencv-python numpy
```

3. **Install Tesseract OCR:**
Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki). Ensure it is added to your system's PATH.

## Usage
1. **Set the path to the Tesseract executable:**
In the script, update the path to the Tesseract executable if it's installed in a different location:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

2. **Run the script:**

```bash
python main.py
```

3. **Adjust the window size and position:**

- Drag the window by clicking and holding the left mouse button.
- Resize the window by adjusting its geometry in the script (root.geometry("100x50")).