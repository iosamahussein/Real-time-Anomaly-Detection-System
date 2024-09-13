import random
import time
import matplotlib.pyplot as plt
from collections import deque

class AnomalyDetector:
    """
    A class used to detect anomalies in a continuous data stream using a sliding window approach.
    """

    def __init__(self, window_size=100, threshold=3):
        """
        Initializes the AnomalyDetector with the specified window size and threshold.

        Parameters:
        ----------
        window_size : int, optional
            The number of data points to consider in the sliding window (default is 100).
        threshold : float, optional
            The Z-score threshold for anomaly detection (default is 3).
        """
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
        self.mean = 0
        self.std_dev = 0

    def update(self, value):
        """
        Updates the sliding window with a new data point and recalculates the mean and standard deviation.

        Parameters:
        ----------
        value : float
            The new data point to add to the window.
        """
        self.data_window.append(value)

        if len(self.data_window) == self.window_size:
            self.mean = sum(self.data_window) / self.window_size
            self.std_dev = (sum((x - self.mean) ** 2 for x in self.data_window) / self.window_size) ** 0.5

    def is_anomaly(self, value):
        """
        Determines if the given value is an anomaly based on its Z-score compared to the window's mean and standard deviation.

        Parameters:
        ----------
        value : float
            The value to check for anomaly.

        Returns:
        -------
        bool
            True if the value is considered an anomaly, False otherwise.
        """
        if len(self.data_window) < self.window_size:
            return False
        
        z_score = abs(value - self.mean) / self.std_dev
        return z_score > self.threshold


def generate_data_stream():
    """
    Generates a synthetic data point for a simulated data stream, with a 5% chance of being an anomaly.

    Returns:
    -------
    float
        The generated data point.
    """
    base = 100
    noise = random.gauss(0, 10)
    anomaly = random.random() < 0.05  # 5% chance of anomaly

    if anomaly:
        value = base + noise + random.uniform(50, 100)
    else:
        value = base + noise

    return value


def visualize_stream(data, anomalies):
    """
    Plots the data stream in real-time, highlighting any detected anomalies in red.

    Parameters:
    ----------
    data : deque
        The current sliding window of the data stream.
    anomalies : deque
        A deque of boolean values indicating whether each corresponding data point is an anomaly.
    """
    plt.clf()
    plt.plot(data, label='Data Stream')
    plt.scatter([i for i, a in enumerate(anomalies) if a], 
                [d for d, a in zip(data, anomalies) if a],
                color='red', label='Anomalies')
    plt.legend()
    plt.title('Data Stream Anomaly Detection')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.pause(0.01)


def main():
    """
    Main function to run the real-time anomaly detection system. It generates data, updates the anomaly detector,
    and visualizes the results in real-time.
    """
    window_size = 100
    detector = AnomalyDetector(window_size=window_size) 
    data = deque(maxlen=window_size)
    anomalies = deque(maxlen=window_size)
    plt.ion()

    try:
        while True:
            value = generate_data_stream()
            data.append(value)

            detector.update(value)
            is_anomaly = detector.is_anomaly(value)
            anomalies.append(is_anomaly)

            if is_anomaly:
                print(f"Anomaly detected: {value}")

            visualize_stream(data, anomalies)
            time.sleep(0.1)  # Simulate real-time data stream

    except KeyboardInterrupt:
        print("Stream stopped by user.")


if __name__ == "__main__":
    main()
