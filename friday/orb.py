import cv2, numpy as np, math
from datetime import datetime

def draw_orb(state="idle", angle=0, size=150):
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    center = (250, 250)
    radius = size // 2
    orb_color = (255, 0, 0)

    if state == "speaking":
        pulse = int(10 + 8 * math.sin(math.radians(angle)))
    else:
        pulse = int(6 + 4 * math.sin(math.radians(angle)))

    cv2.circle(img, center, radius + pulse, orb_color, -1)
    img = cv2.GaussianBlur(img, (0, 0), 25)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %b %Y")

    cv2.putText(img, current_date, (100, 120), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (180, 180, 180), 2, cv2.LINE_AA)
    cv2.putText(img, current_time, (180, 430), cv2.FONT_HERSHEY_DUPLEX,
                1.2, (255, 255, 255), 2, cv2.LINE_AA)

    return img
