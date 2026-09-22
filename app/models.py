from pydantic import BaseModel, Field


class ProgressReport(BaseModel):

    job_id: str

    status: str

    progress: float = Field(
        ge=0.0,
        le=100.0
    )


class JobEvent(BaseModel):

    job_id: str

    event: str

    message: str