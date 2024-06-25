# LMS NoisePurify

LMS NoisePurify is an audio noise reduction application that utilizes the LMS (Least Mean Squares) adaptive filtering technique to remove noise from audio signals. This application provides a simple and intuitive user interface, allowing you to easily load, process, and play audio files.

# Video Link

### **[Watch the video](https://youtu.be/MEQV0mZmJ1o?si=2qiZMI3gFMwOLywW)** 




##**如果執行程式有問題，可以去雲端硬碟下載整個檔案，網址如下：** [https://drive.google.com/drive/folders/1EfXj1RgwpP4WTPcVhc0gqGm9GCp3DlHO?usp=sharing](https://drive.google.com/drive/folders/1EfXj1RgwpP4WTPcVhc0gqGm9GCp3DlHO?usp=sharing)


## Features

- **Load Audio Files**: Load audio files with noise and pure noise files.
- **Audio Processing**: Use the LMS algorithm to perform noise reduction on the audio signal and generate a cleaned audio file.
- **Play Audio**: Play both the original and noise-reduced audio, and visualize the waveform.

## Technology Used

- **LMS Algorithm**: Adjusts filter parameters by calculating the error between the desired signal and the actual filtered signal to achieve noise reduction.
- **Partial Differential Equations**: Utilizes gradient descent to minimize error and adjust filter weights.


## Installation and Usage

### Requirements

- Python 3.x
- `tkinter`
- `numpy`
- `soundfile`
- `matplotlib`
- `winsound` (Windows only)

### Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/yourusername/LMS-NoisePurify.git
    cd LMS-NoisePurify
    ```

2. Set up a virtual environment and install the required Python libraries:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Usage

1. Navigate to the project directory and run the main application:

    ```sh
    python main.py
    ```

2. In the application interface:
   - Load the noisy audio file and the pure noise file.
   - Click the "Process" button to perform noise reduction.
   - Click the "Play Input Signal" button to play the original noisy audio.
   - Click the "Play and Show Waveforms" button to play the noise-reduced audio and visualize the waveforms.

## Code Overview

### Main Application

The `main.py` contains the primary logic for the application, handling the user interface and interactions.

### LMS Filter

The `filters/lms_filter.py` file implements the LMS filter, which processes the audio signals.

```python
class LMSFilter:
    def __init__(self, filter_order, step_size):
        self.filter_order = filter_order
        self.step_size = step_size
        self.weights = np.zeros(filter_order)

    def adapt(self, desired, input_signal):
        n = len(input_signal)
        output = np.zeros(n)
        error = np.zeros(n)

        for i in range(self.filter_order, n):
            x = input_signal[i:i-self.filter_order:-1]
            output[i] = np.dot(self.weights, x)
            error[i] = desired[i] - output[i]
            self.weights += 2 * self.step_size * error[i] * x

        return output, error

### `requirements.txt`





