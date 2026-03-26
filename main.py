import os
import yaml
from src.utils.logger import setup_logger
from src.pipeline.base_pipeline import BasePipeline

def load_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    logger = setup_logger(config["paths"]["log_dir"])

    pipeline = BasePipeline(config, logger)

    input_dir = config["paths"]["input_dir"]

    for file in os.listdir(input_dir):
        image_path = os.path.join(input_dir, file)

        result = pipeline.process_image(image_path)
        pipeline.save_output(result)

        logger.info(f"Saved output for {file}")

if __name__ == "__main__":
    main()