# Hand Writing Recognition

## Overview

The Hand Writing Recognition project utilizes computer vision and gesture detection to create an interactive drawing application. This application leverages a webcam to detect hand movements and allows users to draw on the screen using their hands. The project is built using Python and employs OpenCV, Mediapipe, and NumPy libraries for real-time hand tracking and gesture analysis.

## Features

- **Real-time Hand Detection**: Utilizes Mediapipe to accurately detect hands and track finger movements.
- **Gesture-Based Drawing**: Users can start and stop drawing with simple hand gestures (1 finger to start, 2 fingers to stop).
- **Canvas Drawing**: A drawing canvas that captures the user's strokes and displays them in real-time.
- **Finger Count Visualization**: A graph that shows the history of detected finger counts, providing visual feedback on hand gestures.
- **Image Saving**: Option to save the drawing progress as an image file.

## Technologies Used

- Python
- OpenCV
- Mediapipe
- NumPy

## Installation

1. **Clone the Repository**

   To get a copy of this project up and running on your local machine, clone the repository using:

   ```bash
   git clone https://github.com/engrmumtazali0112/hand-gestures-recognition.git
   cd hand-gestures-recognition
Set Up a Virtual Environment (Optional but Recommended)

You can create a virtual environment to manage dependencies:


python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies

Install the required libraries using pip:


pip install -r requirements.txt
Usage
Run the Application

Start the application by executing the following command:


python src/main.py
Controls

1 Finger: Start Drawing
2 Fingers: Stop Drawing
Press "q": Quit the application
Press "c": Clear the canvas
Output

The application saves the drawing progress as an image file in the output_images folder when the drawing session is complete.

Project Structure


.
├── env_src/              # Virtual environment directory (if created)
├── src/                  # Source code
│   ├── gesture_analyzer.py  # Contains logic for gesture analysis
│   ├── hand_detector.py      # Contains logic for hand detection
│   └── main.py               # Main application file
├── requirements.txt       # Python package dependencies
└── output_images/         # Directory for saving drawing 

Contribution
Contributions are welcome! If you have suggestions for improvements or would like to contribute, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
OpenCV for computer vision functionalities.
Mediapipe for hand tracking capabilities.
NumPy for numerical operations.
Contact
For any inquiries or feedback, feel free to reach out to me:

Email: engrmumtazali01@gmail.com
GitHub: [engrmumtazali0112](https://github.com/engrmumtazali0112)


### Instructions

1. **Replace** `yourusername` and `your.email@example.com` with your actual GitHub username and email address.
2. **Ensure** that your directory structure and files match the structure described in the README.
3. **Save** this content in a file named `README.md` in the root of your project directory.

This README provides comprehensive information about your project, including features, installation steps, usage instructions, and contribution guidelines.





