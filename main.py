
from marketing_campaign_responses import logger
from marketing_campaign_responses.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from marketing_campaign_responses.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from marketing_campaign_responses.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from marketing_campaign_responses.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from marketing_campaign_responses.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e