import cv2
import requests

# Load YOLO model and configuration
net = cv2.dnn.readNet("/home/aivid9/Desktop/akash/darknet/yolov3.weights", "/home/aivid9/Desktop/akash/darknet/cfg/yolov3.cfg")

# Define the output layer indices
output_layer_indices = [net.getLayerId("yolo_82"), net.getLayerId("yolo_94"), net.getLayerId("yolo_106")]

# Get the names of the output layers
output_layers = [net.getLayer(output_layer_indices[i]).name for i in range(len(output_layer_indices))]

# Load classes
classes = []
with open("/home/aivid9/Downloads/coco.names", "r") as f:
    classes = f.read().strip().split("\n")

#video_url = "https://aividtechvision.slack.com/files/U0527N5GGBZ/F05NX11T940/vlc-record-2023-08-16-17h42m55s-rtsp___192.168.111.104_554_cam_realmonitor-.mp4?origin_team=T0173SWKNTU&origin_channel=D05K8JKNBP1"
video_path = "/home/aivid9/Desktop.mp4"  # Provide the desired local path

response = requests.get(video_path)
with open(video_path, "wb") as f:
    f.write(response.content)

# Open the locally saved video file
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Rest of your code remains the same

    # Display the frame
    cv2.imshow("Forgotten Object Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()















































# import cv2


# # Load YOLO model and configuration
# net = cv2.dnn.readNet("/home/aivid9/Desktop/akash/darknet/yolov3.weights", "/home/aivid9/Desktop/akash/darknet/cfg/yolov3.cfg")

# # Define the output layer indices
# output_layer_indices = [net.getLayerId("yolo_82"), net.getLayerId("yolo_94"), net.getLayerId("yolo_106")]

# # Get the names of the output layers
# output_layers = [net.getLayer(output_layer_indices[i]).name for i in range(len(output_layer_indices))]

# # Load classes
# classes = []
# with open("/home/aivid9/Downloads/coco.names", "r") as f:
#     classes = f.read().strip().split("\n")

# # Define the class IDs for "forgotten things"
# forgotten_class_ids = [class_id for class_id, class_name in enumerate(classes) if class_name in ["person", "backpack", "umbrella","carrot"]]  # Modify this list as needed

# # RTSP URL for the camera stream
# rtsp_url = "rtsp://aivid:aivid_2022@192.168.111.104:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"
# cap = cv2.VideoCapture(rtsp_url)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     height, width, channels = frame.shape

#     # Perform object detection
#     blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(416, 416), swapRB=True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Process detection results
#     class_ids = []
#     confidences = []
#     boxes = []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = scores.argmax()
#             confidence = scores[class_id]
#             if confidence > 0.5 and class_id in forgotten_class_ids:  # Adjust threshold and class IDs as needed
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 class_ids.append(class_id)
#                 confidences.append(float(confidence))
#                 boxes.append([x, y, w, h])

#     # Apply Non-Maximum Suppression to avoid multiple overlapping detections
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     # Draw detected objects on the frame
#     for i in range(len(boxes)):
#         if i in indexes:
#             label = str(classes[class_ids[i]])
#             confidence = confidences[i]
#             x, y, w, h = boxes[i]
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the frame
#     cv2.imshow("Forgotten Object Detection", frame)

#     # Exit when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# # Release the capture and close the windows
# cap.release()
# cv2.destroyAllWindows()
