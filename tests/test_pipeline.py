import pytest

from app.pipeline.processor import VideoProcessor
from app.detector.sam_mock import SamMockDetector


def test_invalid_video_path_fails():

    processor = VideoProcessor(
        SamMockDetector()
    )

    with pytest.raises(RuntimeError):

        processor.process(
            "missing_video.mp4"
        )