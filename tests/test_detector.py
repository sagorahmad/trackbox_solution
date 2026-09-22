import numpy as np

from app.detector.sam_mock import SamMockDetector


def test_blank_frame_returns_none():

    detector = SamMockDetector()

    frame = np.zeros(
        (720,1280,3),
        dtype=np.uint8
    )

    result = detector.detect(frame)

    assert result is None