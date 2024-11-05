# === src/gesture_analyzer.py ===
import math
import cv2
import numpy as np

class GestureAnalyzer:
    def __init__(self):
        self.finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
        self.finger_bases = [2, 6, 10, 14, 18]  # Base points for each finger

    def count_fingers(self, landmark_list):
        """
        Count extended fingers based on landmark positions
        """
        if not landmark_list:
            return 0

        fingers = []
        
        # Thumb (special case)
        if landmark_list[self.finger_tips[0]][1] < landmark_list[self.finger_tips[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            
        # Other fingers
        for id in range(1, 5):
            if landmark_list[self.finger_tips[id]][2] < landmark_list[self.finger_bases[id]][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        return sum(fingers)

    def draw_finger_count(self, frame, count):
        """
        Display finger count on frame
        """
        cv2.putText(
            frame,
            f'Fingers: {count}',
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (255, 0, 0),
            2
        )
        return frame

