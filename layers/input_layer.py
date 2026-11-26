import cv2
import numbers
import numpy as np

from .config import layer_config


class InputLayer:
    def __init__(self, width=None, height=None):
        self.config: dict = layer_config.get_input_config()
        self.width: int = 0
        self.height: int = 0

        if isinstance(width, numbers.Real) and int(width) >= 0:
            self.width = int(width)
        elif self.config["width"]:
            self.width = self.config["width"]
        else:
            print("Error: Input layer width config not found")

        if isinstance(height, numbers.Real) and int(height) >= 0:
            self.height = int(height)
        elif self.config["height"]:
            self.height = self.config["height"]
        else:
            print("Error: Input layer height config not found")

    def preprocess(self, path: str) -> np.ndarray:
        # Load image
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"Could not load image {path}")

        # Resize image
        h, w = image.shape
        scale = min(self.width / w, self.height / h)
        new_w = max(1, round(w * scale))
        new_h = max(1, round(h * scale))
        resized = cv2.resize(
            image,
            (new_w, new_h),
            interpolation=cv2.INTER_AREA if scale > 1 else cv2.INTER_LINEAR
        )

        # Center resized image within dimensions
        canvas = np.zeros((self.height, self.width), dtype=np.uint8)
        x = (self.width - new_w) // 2
        y = (self.height - new_h) // 2
        canvas[y:y+new_h, x:x+new_w] = resized

        # Normalize pixel intensities
        canvas = canvas.astype(np.float32) / 255.0

        return canvas
