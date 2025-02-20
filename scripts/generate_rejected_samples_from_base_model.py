import logging
import os
import sys
import yaml
import pandas as pd

from ollama import chat
from ollama import ChatResponse

logger = logging.getLogger(__name__)
logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
logger.setLevel(logging.INFO)


# Load YAML file
file_path = os.path.abspath(sys.argv[1])
with open(file_path, "r") as file:
    args = yaml.safe_load(file)  # Use safe_load to avoid security risks

df = pd.read_parquet(args.dataset.data_input_path)

for i in range(len(df)):
    message_system_user = df.iloc[i]["prompt"]
    try:
        response: ChatResponse = chat(model=args.model.model_ollama, messages=message_system_user)
        message_rejected = {}
        message_rejected["content"] = response['message']['content']
        message_rejected["role"] = "assistant"
        df.loc[i]["rejected"] = [message_rejected]
    except:
        logger.info(f"LLM reply failed for sample: {i}")
        df.loc[i]["rejected"] = None

df.to_parquet(args.dataset.data_output_path)