## Midjourney Image Splitter ✂️

This Python application with a user-friendly GUI allows you to easily split your Midjourney images into four quadrants, perfect for further editing or experimentation.

### Features:

* Split individual images from a folder.
* Process multiple images at once.
* Fetch an image from a URL and split it into quadrants.
* Save the split quadrants to a designated output folder.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nafi7393/Midjourney-Image-Splitter
   ```

2. **Install dependencies:**

   ```bash
   cd Midjourney-Image-Splitter
   pip install -r requirements.txt
   ```

### Usage

**From GUI:**

The provided GUI application offers a user-friendly interface for splitting images. Simply:

1. **Run the application:**

   ```bash
   python gui.py
   ```

2. **Select input and output folders** for processing local images.
3. **Enter the image URL** and output folder for processing an image from a URL.
4. **Click the corresponding button** to initiate the splitting process.

### Example: Splitting an Image

**Using GUI:**

1. Open the application (`python gui.py`).
2. In the "Input Folder Path" field, enter the path to your folder containing Midjourney images (e.g., "input").
3. In the "Output Folder Path" field, enter the path to the folder where you want to save the split quadrants (e.g., "output").
4. Click the "Process Local Images" button.

**Using Script:**

```bash
python main.py process_folder input_folder output_folder
```

Replace `input_folder` with the actual path to your folder containing Midjourney images and `output_folder` with the desired path to save the split quadrants.

**Visual Example:**

| **Original Image** | **Top-Left Quadrant** | **Top-Right Quadrant** | **Bottom-Left Quadrant** | **Bottom-Right Quadrant** |
|---|---|---|---|---|
| [Image of Full Midjourney Image](path/to/your/logo.png) | [Image of Top-Left Quadrant](path/to/your/gui_image.png) | [Image of Top-Right Quadrant](path/to/your/gui_image.png) | [Image of Bottom-Left Quadrant](path/to/your/gui_image.png) | [Image of Bottom-Right Quadrant](path/to/your/gui_image.png) |

**Note:** Replace the image paths in the table with the actual locations of your logo and an example split image (adjust paths as needed).

### Contributing

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit a pull request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
