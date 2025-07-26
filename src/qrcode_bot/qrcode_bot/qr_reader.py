#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class QRCodeReader(Node):
    def __init__(self):
        super().__init__('qr_code_reader')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',  # ✅ corrected topic name
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.qr_detector = cv2.QRCodeDetector()
        self.get_logger().info("📷 QR Code Reader Node Started")

    def image_callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV image
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"❌ CV Bridge error: {e}")
            return

        # Detect and decode QR code
        data, bbox, _ = self.qr_detector.detectAndDecode(frame)

        if bbox is not None and data:
            # Draw bounding box
            bbox = bbox.astype(int)
            for i in range(len(bbox[0])):
                pt1 = tuple(bbox[0][i])
                pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            # Put text on image
            cv2.putText(frame, data, (bbox[0][0][0], bbox[0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            self.get_logger().info(f"🔍 QR Code Detected: {data}")

        # Show the video frame
        cv2.imshow("QR Code Reader", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = QRCodeReader()
    rclpy.spin(node)
    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

