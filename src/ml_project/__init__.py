import os 
import sys
import logging

log_format= '[%(asctime)s : %(levelname)s : %(module)s : %(message)s]'

log_dir= 'Logs'
os.makedirs(log_dir,exist_ok=True)
log_filepath=os.path.join(log_dir,'running_logs.log')

logging.basicConfig(
    level=logging.INFO,
    format=log_format,

    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
    ]

    )
logger= logging.getLogger("mlProjectLogger")

