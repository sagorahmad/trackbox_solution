class MetricsCalculator:

    def calculate(
        self,
        total_frames: int,
        detections: list
    ):

        valid_detections = len(detections)

        detection_rate = 0

        if total_frames > 0:
            detection_rate = (
                valid_detections / total_frames
            ) * 100


        return {
            "total_frames": total_frames,
            "valid_detections": valid_detections,
            "detection_rate": detection_rate
        }