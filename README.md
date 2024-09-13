# Real-time Anomaly Detection System

## Overview

This project implements a real-time anomaly detection system using a sliding window of data points. The system monitors a simulated data stream and identifies anomalous values based on a Z-score threshold. If an anomaly is detected, it is highlighted on a real-time plot.

## Features

- Real-time data stream generation with a 5% chance of anomalies.
- Sliding window-based anomaly detection using Z-score.
- Dynamic plotting of the data stream, highlighting detected anomalies.
- Configurable parameters for detection sensitivity (window size and threshold).

## Requirements

- Python 3.x
- `matplotlib` for plotting
- `deque` from the `collections` module for managing the sliding window of data

You can install the required dependencies using the following command:

```bash
pip install matplotlib
```

## Usage

### Running the Script

To run the script, use the following command:

```bash
python anomaly_detection.py
```

The system will generate a simulated data stream, detect anomalies in real-time, and visualize the results.

### Key Components

1. **AnomalyDetector**:
   - **`__init__(self, window_size=100, threshold=3)`**: Initializes the detector with a sliding window size and Z-score threshold for anomaly detection.
   - **`update(self, value)`**: Adds a new data point to the sliding window and updates the mean and standard deviation.
   - **`is_anomaly(self, value)`**: Checks if the new data point is an anomaly based on the Z-score compared to the window’s mean and standard deviation.

2. **Data Stream Generation**:
   - **`generate_data_stream()`**: Generates a synthetic data stream with a small chance of introducing anomalies.

3. **Visualization**:
   - **`visualize_stream(data, anomalies)`**: Plots the data stream with anomalies highlighted in red.

4. **Main Loop**:
   - The script runs an infinite loop to simulate real-time data collection, updating the anomaly detector, and dynamically visualizing the data and detected anomalies.

## Parameters

- **`window_size`**: The number of recent data points used to calculate the mean and standard deviation for anomaly detection. Default is 100.
- **`threshold`**: The Z-score threshold beyond which a data point is considered an anomaly. Default is 3.

## Example Output

During execution, the script outputs the following in real-time:

- Detected anomalies (e.g., "Anomaly detected: 175.32").
- A real-time plot with anomalies highlighted in red.

To stop the program, press `Ctrl+C`.

## Customization

- **Window Size and Threshold**: You can change the sensitivity of the anomaly detection by adjusting `window_size` and `threshold` when creating the `AnomalyDetector` instance.
  
Example:
```python
detector = AnomalyDetector(window_size=200, threshold=2.5)
```

- **Sleep Time**: Modify the `time.sleep(0.1)` in the main loop to adjust the speed of data stream simulation.

## License

This project is open source and available under the MIT License.