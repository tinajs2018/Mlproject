import os
import sys
from src.exception import CustomeExepection
# # # from src.exception import CustomException
# from .src.exception import CustomeExepection

from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class data_ingestion_config:
    train_data_path :str=os.path.join('artifacts',"train.csv")
    test_data_path :str=os.path.join('artifacts',"test.csv")
    raw_data_path :str=os.path.join('artifacts',"raw.csv")

class data_ingestion:
    def __init__(self) :
        self.ingestion_config =data_ingestion_config()
        
    def  initate_data_ingestion(self):
        logging.info("Enter the data ingestion method or components")
        try:
            df=pd.read_csv("/home/hp/Desktop/mlproject/myenv/notebook/stud.csv")
            logging.info("Read the data  as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train_test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("the ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
        except Exception as e:
            raise CustomeExepection(e,sys)
#initaition of the object
if __name__=="__name__":
    obj=data_ingestion()
    obj.initate_data_ingestion()

