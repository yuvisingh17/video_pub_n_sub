import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.cameraDeviceNumber=0
        self.publisher_ = self.create_publisher(Image, 'video_stream', 10)
        self.timer = self.create_timer(1.0 / 30, self.publish_frame)  # 30 FPS
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(self.cameraDeviceNumber)  # Open the webcam

    def publish_frame(self):
        ret, frame = self.cap.read()  # Read a frame from the webcam
        if ret:
            img_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")  # Convert frame to ROS Image message
            self.publisher_.publish(img_msg)  # Publish the image

def main(args=None):
    rclpy.init(args=args)
    video_publisher = VideoPublisher()
    rclpy.spin(video_publisher)
    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
