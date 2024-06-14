
from marketing_campaign_responses import logger
from marketing_campaign_responses.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e