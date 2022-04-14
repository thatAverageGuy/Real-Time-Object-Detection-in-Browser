import cv2
import numpy as np

def predict(model, frame):
    """Generate predictions and annotate the predicted frame."""
    resx = model(frame, size = 416).crop(save=False)
    for d in resx:
        box = list(map(int, list(map(np.round, d['box']))))
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 3)
        px, py = box[0], box[1]-10
        cv2.putText(frame, "Connector", (px, py), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return frame