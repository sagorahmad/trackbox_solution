from app.config import PipelineConfig


def main():

    config = PipelineConfig()

    print("TrackBox pipeline configuration loaded successfully.")

    print(
        f"Video path: {config.video_path}, "
        f"Target FPS: {config.target_fps}, "
        f"Job ID: {config.job_id}"
    )


if __name__ == "__main__":
    main()