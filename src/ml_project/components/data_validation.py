import os
import pandas as pd
from ml_project import logger
from ml_project.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema_key = self.config.all_schema.keys()
            all_schema = self.config.all_schema
            value  = self.config.all_schema.values()
            
            for col in all_cols:
                
                if col not in all_schema_key:
                    for i in all_schema:
                        print(data[col].dtypes ,'::',all_schema[i])
                        if all_schema[i] != data[col].dtypes:
                            validation_status = False
                            with open(self.config.STATUS_FILE, 'w') as f:
                                f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e