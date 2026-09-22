from abc import ABC, abstractmethod

import numpy as np
from shapely.geometry import Polygon


class FieldDetector(ABC):

    @abstractmethod
    def detect(self, frame: np.ndarray) -> Polygon | None:
        pass