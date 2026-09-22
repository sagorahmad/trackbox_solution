import cv2
import numpy as np
import logging

from shapely.geometry import Polygon
from app.detector.base import FieldDetector

logger = logging.getLogger(__name__)


class SamMockDetector(FieldDetector):

    def __init__(self, min_area: int = 1000):

        self.min_area = min_area


    def detect(self, frame: np.ndarray) -> Polygon | None:

        mask = self._extract_mask(frame)

        return self._derive_polygon_from_mask(mask)


    def _extract_mask(self, frame: np.ndarray) -> np.ndarray:

        hsv = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2HSV
        )

        lower_green = np.array(
            [35, 40, 40]
        )

        upper_green = np.array(
            [85, 255, 255]
        )

        return cv2.inRange(
            hsv,
            lower_green,
            upper_green
        )


    def _derive_polygon_from_mask(
        self,
        mask: np.ndarray
    ) -> Polygon | None:

        try:

            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            if not contours:
                return None


            largest = max(
                contours,
                key=cv2.contourArea
            )


            if cv2.contourArea(largest) <= self.min_area:
                return None


            points = largest.reshape(-1, 2)


            if len(points) < 3:
                return None


            return Polygon(points)


        except Exception as error:
            logger.error(
                "Polygon extraction failed",
                exc_info=True
            )

            return None