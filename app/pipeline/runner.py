from app.detector.sam_mock import SamMockDetector
from app.pipeline.processor import VideoProcessor


class PipelineRunner:


    def __init__(self, config):

        self.config = config


    def run(self):

        detector = SamMockDetector(
            min_area=
            self.config.field_detector.min_area
        )


        processor = VideoProcessor(
            detector,
            frame_interval=
            self.config.frame_interval
        )


        results = processor.process(
            self.config.video_path
        )


        print(
            f"Detected {len(results)} boundaries"
        )


        return results