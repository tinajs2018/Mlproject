#to tract the errors
import logging
import os 
from src.logger import logging
from datetime import  datetime
#creating the log file
LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M%_%S')}.log"
#add the path of the log file
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_PATH_FILE=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)


