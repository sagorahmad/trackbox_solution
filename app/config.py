from pydantic import BaseModel, Field


class FieldDetectorConfig(BaseModel):
    type: str = "sam_mask_v1"
    sport: str = "football"
    min_area: int = Field(default=1000, gt=0)


class CropSearchConfig(BaseModel):
    aspect_ratio: str = "16:9"
    padding_px: int = Field(default=20, ge=0)


class PipelineConfig(BaseModel):

    video_path: str = "synthetic_pitch_feed.mp4"

    target_fps: int = Field(default=30, gt=0)

    confidence_threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0
    )

    job_id: str = "job-synthetic-001"

    frame_interval: int = Field(
        default=30,
        gt=0
    )

    field_detector: FieldDetectorConfig = Field(
        default_factory=FieldDetectorConfig
    )

    crop_search: CropSearchConfig = Field(
        default_factory=CropSearchConfig
    )

    debug_mode: bool = True