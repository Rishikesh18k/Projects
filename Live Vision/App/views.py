from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from ultralytics import YOLO
import cv2
import numpy as np
import datetime

def home(request):
    return render(request, 'home.html')

def live_stream(request):
    return render(request, 'livestream.html')

def about(request):
    return render(request, 'about.html')


model = YOLO("yolov8n.pt")
streaming = False
recording = False
out = None

def draw_rounded_box(img, top_left, bottom_right, color, radius=4):
    ...

def generate_frames():
    global streaming, recording, out
    cap = cv2.VideoCapture(0)

    while streaming:   # stream tabhi chale jab flag True ho
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]

                x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                cx = int((x1 + x2) / 2)
                cy = int(y1)

                # 🔹 Bounding Box (Frame)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)  # Green box

                # 🔹 Label Background (Rounded Box)
                font_scale = 0.6
                font_thickness = 1
                (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
                padding_x, padding_y = 20, 15

                rect_x1 = cx - (tw // 2) - padding_x
                rect_y1 = cy - th - 35
                rect_x2 = cx + (tw // 2) + padding_x
                rect_y2 = cy - 10

                draw_rounded_box(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), (0, 200, 0), radius=4)

                # 🔹 Text Centered
                text_x = rect_x1 + (rect_x2 - rect_x1 - tw) // 2
                text_y = rect_y1 + (rect_y2 - rect_y1 + th) // 2
                cv2.putText(frame, label, (text_x, text_y),
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 125, 0), font_thickness, cv2.LINE_AA)

                # 🔹 Arrow pointing to object
                arrow_points = np.array([
                    [cx - 10, rect_y2],
                    [cx + 10, rect_y2],
                    [cx, rect_y2 + 12]
                ], np.int32)
                cv2.fillPoly(frame, [arrow_points], (0, 200, 0))

        # 🔹 Save to file if recording
        if recording and out is not None:
            out.write(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    if out:
        out.release()
        out = None


def video_feed(request):
    global streaming
    streaming = True
    return StreamingHttpResponse(generate_frames(),
                content_type='multipart/x-mixed-replace; boundary=frame')


# 🔹 Start Stream
def start_stream(request):
    global streaming
    streaming = True
    return JsonResponse({"status": "started"})


# 🔹 Stop Stream
def stop_stream(request):
    global streaming
    streaming = False
    return JsonResponse({"status": "stopped"})