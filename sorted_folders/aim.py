import cv2
import numpy as np

class ObjectDetector:
    def __init__(self, reference_frame_path, video_path, output_path, min_static_frames=20):
        self.reference_frame = cv2.imread(reference_frame_path, cv2.IMREAD_GRAYSCALE)
        self.reference_frame = cv2.resize(self.reference_frame, (self.reference_frame.shape[1], self.reference_frame.shape[0]))  # Resize the reference frame
        
        self.cap = cv2.VideoCapture(video_path)
        self.frame_width = int(self.cap.get(3))
        self.frame_height = int(self.cap.get(4))
        self.fps = int(self.cap.get(5))
        self.output_path = output_path
        self.min_static_frames = min_static_frames
        self.static_objects = {}
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(output_path, self.fourcc, self.fps, (self.frame_width, self.frame_height), isColor=True)
   
    def process_frames(self):  #process frame   
        while True:    
            ret, frame = self.cap.read()
            if not ret:
                break
           
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert frame to grayframe 
            diff_frame = cv2.absdiff(gray_frame, self.reference_frame)
            
            _, threshold_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            criteria = [
                # {"name": "person", "min_width": 20, "min_height": 80, "color": (0, 255, 0)},
                {"name": "bag", "min_width": 40, "min_height": 40, "color": (0, 0, 255)}
            ]
            
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                for crit in criteria:
                    if crit["min_width"] < w and crit["min_height"] < h:
                        obj_id = (x, y, w, h)#crit["name"] 
                        if obj_id in self.static_objects:
                            self.static_objects[obj_id] += 1
                        else:
                            self.static_objects[obj_id] = 1
                        if self.static_objects[obj_id] >= self.min_static_frames:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), crit["color"], 2)
                            cv2.putText(frame,crit["name"], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, crit["color"], 2)
            
            self.out.write(frame)
            cv2.imshow('Processed Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
          
    def release(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
       
        
if __name__ == "__main__":
    reference_frame_path = '/home/aivid9/Downloads/test2.png'
    video_path = '/home/aivid9/Downloads/test2 (1).avi'
    output_path = '/home/aivid9/Downloads.mp4'
    
    detector = ObjectDetector(reference_frame_path, video_path, output_path)
    detector.process_frames()
    detector.release()
  


#/home/aivid9/Downloads/test2 (1).avi
#/home/aivid9/Desktop_output.mp4

#'/home/aivid9/Downloads/test2.png'