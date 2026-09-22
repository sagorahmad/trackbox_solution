from app.metrics.calculator import MetricsCalculator


def test_detection_rate_calculation():

    metrics = MetricsCalculator().calculate(
        total_frames=100,
        detections=[1, 2, 3, 4, 5]
    )

    assert metrics["valid_detections"] == 5
    assert metrics["detection_rate"] == 5