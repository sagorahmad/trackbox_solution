from app.detector.sam_mock import SamMockDetector
from app.pipeline.processor import VideoProcessor
from app.metrics.calculator import MetricsCalculator
from app.reporting.client import ReportingClient
from app.models import ProgressReport, JobEvent


class PipelineRunner:

    def __init__(self, config):

        self.config = config


    def run(self):

        detector = SamMockDetector(
            min_area=self.config.field_detector.min_area
        )


        processor = VideoProcessor(
            detector,
            frame_interval=self.config.frame_interval
        )


        process_result = processor.process(
            self.config.video_path
        )


        print(
            f"Detected {len(process_result['detections'])} boundaries"
        )


        metrics = MetricsCalculator().calculate(
            process_result["total_frames"],
            process_result["detections"]
        )
        reporter = ReportingClient(
            self.config.reporting_url
        )

        reporter.send_event(
            JobEvent(
                job_id=self.config.job_id,
                event="pipeline_started",
                message="Pipeline execution started"
            )
        )


        reporter.send_progress(
            ProgressReport(
                job_id=self.config.job_id,
                status="completed",
                progress=100
            )
        )


        reporter.send_event(
            JobEvent(
                job_id=self.config.job_id,
                event="pipeline_completed",
                message=f"Processed {metrics['valid_detections']} valid detections"
            )
        )
        

        return {
            "detections": process_result["detections"],
            "metrics": metrics
        }