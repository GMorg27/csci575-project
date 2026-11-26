import matplotlib.pyplot as plt
import sys

from layers.input_layer import InputLayer


def visualize(path: str):
    input_layer = InputLayer()
    processed_image = input_layer.preprocess(path)
    plt.figure("Processed image")
    plt.imshow(processed_image, cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python input_layer_test.py <image_path>")
        sys.exit(1)

    visualize(sys.argv[1])    
