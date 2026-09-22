import logging
import requests

from app.models import ProgressReport, JobEvent


logger = logging.getLogger(__name__)


class ReportingClient:


    def __init__(self, base_url: str):

        self.base_url = base_url.rstrip("/")


    def send_progress(
        self,
        report: ProgressReport
    ):

        try:

            response = requests.post(
                f"{self.base_url}/api/v1/jobs/progress",
                json=report.model_dump(),
                timeout=5
            )

            response.raise_for_status()


        except Exception:

            logger.error(
                "Failed to send progress report",
                exc_info=True
            )


    def send_event(
        self,
        event: JobEvent
    ):

        try:

            response = requests.post(
                f"{self.base_url}/api/v1/jobs/events",
                json=event.model_dump(),
                timeout=5
            )

            response.raise_for_status()


        except Exception:

            logger.error(
                "Failed to send job event",
                exc_info=True
            )