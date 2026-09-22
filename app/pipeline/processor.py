import cv2
import logging


logger = logging.getLogger(__name__)


class VideoProcessor:

    def __init__(self, detector, frame_interval=30):

        self.detector = detector
        self.frame_interval = frame_interval


    def process(self, video_path):

        logger.info(
            f"Processing video: {video_path}"
        )

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():

            raise RuntimeError(
                "Could not open video"
            )


        frame_number = 0
        detections = []


        while True:

            ret, frame = cap.read()


            if not ret:
                break


            if frame_number % self.frame_interval == 0:

                polygon = self.detector.detect(frame)


                if polygon is not None:

                    detections.append(
                        polygon
                    )


            frame_number += 1


        cap.release()


        logger.info(
            f"Processed {frame_number} frames"
        )


        return {
            "total_frames": frame_number,
            "detections": detections
        }