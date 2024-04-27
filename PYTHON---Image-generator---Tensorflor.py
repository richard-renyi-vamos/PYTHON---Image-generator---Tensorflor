import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Load your pretrained model
# For example, if using TensorFlow:
# model = tf.keras.models.load_model('your_model.h5')

class ImageGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Image Generator")

        # Create GUI elements
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        self.generate_button = tk.Button(master, text="Generate Image", command=self.generate_image)
        self.generate_button.pack()

        # Placeholder for generated image
        self.generated_image = None

    def generate_image(self):
        # Generate random noise or any input for the model
        input_data = np.random.rand(1, 100)  # Example: random noise of size (1, 100)

        # Use your model to generate an image
        # For example, if using TensorFlow:
        # generated_image = model.predict(input_data)
        
        # Placeholder for generated image (replace this with actual generation)
        generated_image = np.random.rand(64, 64, 3)  # Example: random image of size (64, 64, 3)

        # Convert the generated image array to a PIL Image
        pil_image = Image.fromarray((generated_image * 255).astype(np.uint8))

        # Convert PIL Image to Tkinter-compatible format
        self.generated_image = ImageTk.PhotoImage(pil_image)

        # Update the canvas with the new image
        self.canvas.create_image(150, 150, image=self.generated_image)

def main():
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
