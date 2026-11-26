from pathlib import Path
import json


CONFIG_PATH = Path(__file__).parent / "config.json"


class Config:
    def __init__(self):
        self.input: dict = {}

    def load_config(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as file:
                config = json.load(file)
                if config["input"]:
                    self.input = config["input"]
        except Exception as e:
            print(f"Error: Cannot open file {path}; exception is {e}")

    def get_input_config(self) -> dict:
        return self.input


layer_config: Config = Config()
layer_config.load_config(CONFIG_PATH)
