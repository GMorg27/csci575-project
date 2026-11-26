from pathlib import Path
import json


CONFIG_PATH = Path(__file__).parent / "config.json"


class Config:
    def __init__(self):
        self.dataset_path: str = ""
        self.test_split: float = 0.0
        self.val_split: float = 0.0

    def load_config(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as file:
                config = json.load(file)
                if config["dataset_path"]:
                    self.test_split = config["dataset_path"]
                if config["test_split"]:
                    self.test_split = config["test_split"]
                if config["val_split"]:
                    self.val_split = config["val_split"]
        except Exception as e:
            print(f"Error: Cannot open file {path}; exception is {e}")

    def get_dataset_path(self) -> str:
        return self.dataset_path

    def get_test_split(self) -> float:
        return self.test_split

    def get_val_split(self) -> float:
        return self.val_split


training_config: Config = Config()
training_config.load_config(CONFIG_PATH)
