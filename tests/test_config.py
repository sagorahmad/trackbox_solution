import pytest

from pydantic import ValidationError
from app.config import PipelineConfig


def test_valid_config_loads():

    config = PipelineConfig()

    assert config.video_path == "synthetic_pitch_feed.mp4"


def test_invalid_confidence_threshold_fails():

    with pytest.raises(ValidationError):
        PipelineConfig(
            confidence_threshold="invalid"
        )