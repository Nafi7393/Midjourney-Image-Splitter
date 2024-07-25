import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,\
    QMessageBox, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from main import process_images_in_folder, fetch_and_split_image


class ImageProcessorGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Configuration of the application
        self.pos_x = 100
        self.pos_y = 100
        self.width = 525
        self.height = 605
        self.setWindowTitle("Midjourney Image Processor")
        self.setGeometry(self.pos_x, self.pos_y, 0, 0)
        self.setFixedSize(self.width, self.height)

        # Create Widgets (1st half)
        self.input_folder_label = QLabel("Input Folder Path:")
        self.input_folder_edit = QLineEdit()

        self.output_folder_label = QLabel("Output Folder Path:")
        self.output_folder_edit = QLineEdit()

        self.process_local_button = QPushButton("Process Local Images")

        # Logo
        self.logo_pix = QPixmap("ASSETS & DEMO/logo.png")
        self.logo_label = QLabel()  # Replace with your logo
        self.logo_label.setPixmap(self.logo_pix)

        # Create Widgets (2nd half)
        self.url_label = QLabel("Image URL:")
        self.url_edit = QLineEdit()

        self.output_folder_label2 = QLabel("Output Folder:")
        self.output_folder_edit2 = QLineEdit()

        self.process_url_button = QPushButton("Process Image from URL")

        self.initUI()

        # Set the styles to the buttons
        self.styles()

    def initUI(self):
        self.input_folder_edit.setText("input")
        self.output_folder_edit.setText("output")

        self.output_folder_edit2.setText("output")

        # Create layouts
        main_layout = QVBoxLayout()
        local_layout = QVBoxLayout()
        url_layout = QVBoxLayout()

        # Add widgets to local layout
        local_layout.addWidget(self.input_folder_label)
        local_layout.addWidget(self.input_folder_edit)
        local_layout.addWidget(self.output_folder_label)
        local_layout.addWidget(self.output_folder_edit)
        local_layout.addWidget(self.process_local_button)

        # Add widgets to url layout
        url_layout.addWidget(self.url_label)
        url_layout.addWidget(self.url_edit)
        url_layout.addWidget(self.output_folder_label2)
        url_layout.addWidget(self.output_folder_edit2)
        url_layout.addWidget(self.process_url_button)

        # Add spacer for logo
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add layouts to main layout
        main_layout.addLayout(local_layout)
        main_layout.addWidget(self.logo_label)
        main_layout.addItem(spacer)
        main_layout.addLayout(url_layout)

        # Set layout for the main window
        self.setLayout(main_layout)

        # Connect buttons to functions
        self.process_local_button.clicked.connect(self.process_local_images)
        self.process_url_button.clicked.connect(self.process_image_from_url)

        self.show()

    def process_local_images(self):
        input_folder = self.input_folder_edit.text()
        output_folder = self.output_folder_edit.text()
        confirmation = process_images_in_folder(input_folder, output_folder)

        if confirmation:
            QMessageBox.information(self, 'Success', 'Successfully splitted all the images.')
        else:
            QMessageBox.warning(self, 'Failed', 'Error processing images in the folder.')

    def process_image_from_url(self):
        url = self.url_edit.text()
        output_folder = self.output_folder_edit2.text()
        confirmation = fetch_and_split_image(url, output_folder)

        if confirmation:

            QMessageBox.information(self, 'Success', 'Successfully split the image.')
        else:
            QMessageBox.warning(self, 'Failed', 'Error processing image, Check link or give valid output folder path.')

    def styles(self):
        style = """
            QPushButton {
                background-color: #D9D9D9;
                border-radius: 8px;
                padding: 12px 25px;
                font-family: sans-serif;
                font-weight: bold;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #4CAF50;
                border-color: #f0f8f0;
                color: #FFFFFF;
                transition: all 0.3s ease-in-out;
            }
        """

        self.process_local_button.setStyleSheet(style)
        self.process_url_button.setStyleSheet(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessorGUI()
    sys.exit(app.exec_())
