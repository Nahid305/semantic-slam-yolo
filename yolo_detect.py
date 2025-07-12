def detect_objects_yolo(frame, model):
    import pandas as pd

    results = model(frame)[0]  # Get first result from list
    detections = []

    if results.boxes is not None:
        boxes = results.boxes
        for box, cls in zip(boxes.xyxy, boxes.cls):
            x1, y1, x2, y2 = map(int, box[:4])
            label = model.names[int(cls)]
            detections.append({
                "xmin": x1,
                "ymin": y1,
                "xmax": x2,
                "ymax": y2,
                "name": label
            })

    return pd.DataFrame(detections)
