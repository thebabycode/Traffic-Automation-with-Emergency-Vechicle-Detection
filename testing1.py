import serial
import torch
import cv2


class MugDetection:

    def __init__(self, capture_index, capture_index2, capture_index3, model_name):

        self.capture_index = capture_index
        self.capture_index2 = capture_index2
        self.capture_index3 = capture_index3

        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        self.classes = self.model.names
        print("classes = ", self.classes)
        self.device = 'cpu'
        # self.arduino = serial.Serial(port="COM23", baudrate="115200", timeout=.1)
        # self.arduino.write(bytes("hello arduino inside innit", 'utf-8'))

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        print("classes[int(x)] = ", self.classes[int(x)])
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.6:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap2 = cv2.VideoCapture(self.capture_index2)
        assert cap2.isOpened()
        cap3 = cv2.VideoCapture(self.capture_index3)
        assert cap3.isOpened()
        #self.arduino.write(bytes("hello", 'utf-8'))
        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, (500, 500))  # resize the output window
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            cv2.imshow('ROAD 1 Detection', frame)

            ret, frame2 = cap2.read()
            frame2 = cv2.resize(frame2, (500, 500))  # resize the output window
            results2 = self.score_frame(frame2)
            frame2 = self.plot_boxes(results2, frame2)
            cv2.imshow('ROAD 2 Detection', frame2)

            ret, frame3 = cap3.read()
            frame3 = cv2.resize(frame3, (500, 500))  # resize the output window
            results3 = self.score_frame(frame3)
            frame3 = self.plot_boxes(results3, frame3)
            cv2.imshow('ROAD 3 Detection', frame3)

            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()


# Create a new object and execute.
detector = MugDetection(capture_index='video2.mp4', capture_index2="video3.mp4", capture_index3="video4.mp4", model_name='best.pt')
detector()