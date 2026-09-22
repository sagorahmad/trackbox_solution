from app.detector.sam_mock import SamMockDetector


def test_detector_creation():

    detector = SamMockDetector()

    assert detector.min_area == 1000