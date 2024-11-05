import cv2
import numpy as np
import os
from hand_detector import HandDetector
from gesture_analyzer import GestureAnalyzer

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Get camera dimensions
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Initialize detectors
    hand_detector = HandDetector(detection_confidence=0.8)
    gesture_analyzer = GestureAnalyzer()
    
    # Writing mode and drawing settings
    drawing = False
    draw_color = (255, 0, 0)  # Drawing color (blue)
    thickness = 5
    
    # Create a separate canvas for drawing
    canvas = np.zeros((height, width, 3), np.uint8)
    
    # Previous point for smooth line drawing
    prev_point = None
    
    # Mode switch cooldown
    mode_switch_cooldown = 0
    COOLDOWN_FRAMES = 15  # Frames to wait before allowing another mode switch
    
    # Store finger count history
    finger_history = []
    max_history_length = 50  # Maximum number of frames to display in the graph
    
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to read from camera")
            break
        
        # Flip frame horizontally for more intuitive interaction
        frame = cv2.flip(frame, 1)
        
        # Detect hands and draw landmarks
        frame = hand_detector.find_hands(frame)
        
        # Get landmark positions
        landmark_list = hand_detector.find_positions(frame)
        
        # Initialize finger_count to handle cases where no landmarks are detected
        finger_count = 0
        
        if landmark_list:
            # Count fingers
            finger_count = gesture_analyzer.count_fingers(landmark_list)
            
            # Get index finger tip position
            index_finger_tip = (landmark_list[8][1], landmark_list[8][2])
            
            # Mode switching logic with cooldown
            if mode_switch_cooldown == 0:
                if finger_count == 1 and not drawing:  # One finger to start drawing
                    drawing = True
                    mode_switch_cooldown = COOLDOWN_FRAMES
                elif finger_count == 2 and drawing:  # Two fingers to stop drawing
                    drawing = False
                    prev_point = None
                    mode_switch_cooldown = COOLDOWN_FRAMES
            else:
                mode_switch_cooldown = max(0, mode_switch_cooldown - 1)
            
            # Drawing logic
            if drawing and finger_count == 1:
                # Draw circle at current position
                cv2.circle(frame, index_finger_tip, 10, draw_color, -1)
                
                # Draw line for smooth connection
                if prev_point:
                    cv2.line(canvas, prev_point, index_finger_tip, draw_color, thickness)
                prev_point = index_finger_tip
            else:
                prev_point = None
        
        # Blend the canvas with the frame using a valid mask
        mask = np.any(canvas > 0, axis=-1)  # Check if any channel has non-zero values
        if np.any(mask):  # Ensure there is something to blend
            frame[mask] = cv2.addWeighted(frame[mask], 0.5, canvas[mask], 0.5, 0)
        
        # Update finger count history
        finger_history.append(finger_count)
        if len(finger_history) > max_history_length:
            finger_history.pop(0)  # Keep only the latest 'max_history_length' entries
        
        # Draw the graph
        graph_height = 100
        graph_y_start = height - graph_height - 10
        graph_x_scale = width / max_history_length
        
        # Draw the graph background
        cv2.rectangle(frame, (0, graph_y_start), (width, height - 10), (0, 0, 0), -1)
        
        # Draw the finger count graph
        for i in range(1, len(finger_history)):
            cv2.line(frame, 
                      (int((i - 1) * graph_x_scale), graph_y_start + graph_height - finger_history[i - 1] * 10), 
                      (int(i * graph_x_scale), graph_y_start + graph_height - finger_history[i] * 10), 
                      (0, 255, 0), 2)  # Green color for the graph
        
        # Display status and instructions
        status_color = (0, 255, 0) if drawing else (0, 0, 255)
        status_text = 'Drawing Mode: ON' if drawing else 'Drawing Mode: OFF'
        
        # Create a semi-transparent overlay for text background
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 120), (0, 0, 0), -1)
        frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)
        
        # Add text with instructions
        cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
        cv2.putText(frame, '1 Finger: Start Drawing', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, '2 Fingers: Stop Drawing', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, 'Press "q" to quit', (width - 200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Display the finger count
        cv2.putText(frame, f'Fingers: {finger_count}', (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('Hand Writing Recognition', frame)
        
        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            canvas = np.zeros_like(canvas)  # Clear the canvas
        
    # Save the drawing canvas as an image
    output_folder = 'output_images'
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
    output_file_path = os.path.join(output_folder, 'drawing_progress.png')
    cv2.imwrite(output_file_path, canvas)
    print(f"Drawing progress saved as: {output_file_path}")
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
