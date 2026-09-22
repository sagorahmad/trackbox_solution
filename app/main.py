from app.config import PipelineConfig
from app.pipeline.runner import PipelineRunner


def main():

    config = PipelineConfig()

    runner = PipelineRunner(config)

    results = runner.run()

    print(
        f"Pipeline completed. Results: {len(results)}"
    )


if __name__ == "__main__":
    main()