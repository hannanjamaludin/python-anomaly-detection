# NUR HANNAN BINTI JAMALUDIN
# COBBLESTONE ENERGY RECRUITMENT 
# EFFICIENT DATA STREAM ANOMALY DETECTION
# START DATE: 12/9/2024
# UPDATE DATE: 12/9/2024

import numpy as np

def generate_data_stream(n_points=1000):
    # Create a regular pattern with noise and anomalies
    time = np.arange(n_points)
    data = 10 + np.sin(time / 10) * 5 + np.random.normal(0, 1, size=n_points)

    # Introduce some anomalies
    data[100:110] = 30 # Simulate some large anomalies
    data[300:305] = -20 # Simulate some negative anomalies

    return data
    
def detect_anomalies(data, threshold=3):
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = [(x - mean) / std_dev for x in data]
    anomalies = np.where(np.abs(z_scores) > threshold)[0]
    return anomalies

import matplotlib.pyplot as plt

def visualize_data(data, anomalies):
    plt.figure(figsize=(10,6))
    plt.plot(data, label="Data Stream")
    plt.scatter(anomalies, data[anomalies], color='red', label="Anomalies")
    plt.legend()
    plt.show()

# Running the data stream simulation and anomaly detection
data = generate_data_stream()
anomalies = detect_anomalies(data)
visualize_data(data, anomalies)