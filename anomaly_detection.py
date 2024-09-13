import random
import time
import matplotlib.pyplot as plt
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
        self.mean = 0
        self.std_dev = 0

    def update(self, value):
        self.data_window.append(value)
        
        if len(self.data_window) == self.window_size:
            self.mean = sum(self.data_window) / self.window_size
            self.std_dev = (sum((x - self.mean) ** 2 for x in self.data_window) / self.window_size) ** 0.5

    def is_anomaly(self, value):
        if len(self.data_window) < self.window_size:
            return False
        z_score = abs(value - self.mean) / self.std_dev
        return z_score > self.threshold

def generate_data_stream():
    base = 100
    trend = 0
    season = 0
    noise = random.gauss(0, 10)
    anomaly = random.random() < 0.05  # 5% chance of anomaly

    if anomaly:
        value = base + trend + season + noise + random.uniform(50, 100)
    else:
        value = base + trend + season + noise

    return value

def visualize_stream(data, anomalies):
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
    window_size = 100
    detector = AnomalyDetector( window_size=window_size) 
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