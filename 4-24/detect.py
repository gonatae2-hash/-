import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("best.pt")
image_path = "test_images/나사사진.jpg"

def analyze_screw(roi):
    defects = []

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        
        # 1. 휘어짐 검출
        if len(largest) >= 5:
            ellipse = cv2.fitEllipse(largest)
            angle_diff = abs(ellipse[2] - 90)
            if angle_diff > 30:
                defects.append(f"Bent({angle_diff:.1f}deg)")

        # 2. 부러짐 검출
        hull = cv2.convexHull(largest)
        solidity = cv2.contourArea(largest) / cv2.contourArea(hull) if cv2.contourArea(hull) > 0 else 1
        if solidity < 0.5:
            defects.append(f"Broken({solidity:.2f})")

    return defects

img = cv2.imread(image_path)
results = model.predict(image_path, conf=0.2, iou=0.3, verbose=False)

for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        roi = img[y1:y2, x1:x2]
        defects = analyze_screw(roi)

        if defects:
            label = "DEFECT: " + ", ".join(defects)
            color = (0, 0, 255)
        else:
            label = "OK"
            color = (0, 255, 0)

        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        print(f"신뢰도: {conf:.2f} | {label}")

cv2.imshow("Screw Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()