from app.config import PipelineConfig
from app.pipeline.runner import PipelineRunner
from app.logging_config import setup_logging

def main():
    
    setup_logging()
    config = PipelineConfig()

    runner = PipelineRunner(config)

    results = runner.run()

    print(
        f"Pipeline completed. Valid detections: {results['metrics']['valid_detections']}"
    )

if __name__ == "__main__":
    main()