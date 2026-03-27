import os
import yaml
from dotenv import load_dotenv
from src.utils.logger import setup_logger
from src.pipeline.base_pipeline import BasePipeline
from src.utils.env import get_env

def load_config():
    load_dotenv() 

    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    # Replace env variables
    config["telegram"]["token"] = get_env("TELEGRAM_TOKEN")
    config["telegram"]["chat_id"] = get_env("TELEGRAM_CHAT_ID")

    return config

def main():
    config = load_config()
    logger = setup_logger(config["paths"]["log_dir"])
    logger.info("Environment variables loaded successfully")

    pipeline = BasePipeline(config, logger)

    input_dir = config["paths"]["input_dir"]

    for file in os.listdir(input_dir):
        image_path = os.path.join(input_dir, file)
        print(f"Processing {image_path}...")

        result = pipeline.process_image(image_path)
        pipeline.save_output(result)

        logger.info(f"Saved output for {file}")

if __name__ == "__main__":
    main()