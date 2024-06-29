# YouTube Tools

This repository contains a Python script that provides various tools for working with YouTube data. Follow the steps below to get started.

## Prerequisites

- Python: Make sure you have Python installed on your system. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

## Installation

1. Clone this repository to your local machine using the following command:

    ```shell
    git clone https://github.com/your-username/youtube-tools.git
    ```

2. Navigate to the project directory:

    ```shell
    cd youtube-tools
    ```

3. Create a virtual environment to isolate the project dependencies:

    ```shell
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```shell
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```shell
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

5. Install pytorch (https://pytorch.org/), if you don't have GPU, check the website for the correct command:

    ```shell
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
    ```

## Usage

Please modify the file path variable video_path in the script before running.

To specify a file path in Windows, use backslashes (\) to separate directories. For example:

```shell
video_path = 'C:\\Users\\Richard\\Videos\\my_video.mp4'
```
or

```shell
video_path = r"C:\Users\Richard\Videos\my_video.mp4"
```

In macOS and Linux, use forward slashes (/) to separate directories. For example:

```shell
video_path = '/Users/Richard/Videos/my_video.mp4'
```

Make sure to replace `'my_video.mp4'` with the actual name of your video file.

To run the Python script, use the following command:

```shell
python auto_cap_whipser.py
```

Make sure you are in the project directory and the virtual environment is activated.
