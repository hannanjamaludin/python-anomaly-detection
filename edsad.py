# NUR HANNAN BINTI JAMALUDIN
# COBBLESTONE ENERGY RECRUITMENT 
# EFFICIENT DATA STREAM ANOMALY DETECTION
# START DATE: 12/9/2024
# UPDATE DATE: 14/9/2024

import numpy as np
import matplotlib.pyplot as plt

def generate_data_stream(n_points=1000):
    # Validate input
    if not isinstance(n_points, int) or n_points <= 0:
        raise ValueError("n_points must be a positive integer.")

    try:
        # Create a regular pattern with noise and anomalies
        time = np.arange(n_points)
        data = 10 + np.sin(time / 10) * 5 + np.random.normal(0, 1, size=n_points)
        
        # Introduce some anomalies
        data[100:110] = 30      # Simulate some large anomalies
        data[300:305] = -20     # Simulate some negative anomalies

        return data
    
    except Exception as e:
        print(f"Error generating data stream: {e}")
        return None

    
def detect_anomalies(data, threshold=3):
    # Validate input
    if data is None or not isinstance(data, (np.ndarray, list)):
        raise ValueError("Invalid data input: data must be a list or numpy array.")
    
    if not isinstance(threshold, (int, float)) or threshold <= 0:
        raise ValueError("Threshold must be a positive number.")
    
    try:
        mean = np.mean(data)                                    # calculate average of entire data
        std_dev = np.std(data)                                  # to identify what count as normal variation
        z_scores = [(x - mean) / std_dev for x in data]         # to identify how many standart dev away from the mean a data point is
        anomalies = np.where(np.abs(z_scores) > threshold)[0]   # identify indices where anomalies occur
        
        return anomalies
    
    except Exception as e:
        print(f"Error detecting anomalies: {e}")
        return []

# plots the data stream and highlights anomalies
def visualize_data(data, anomalies):
    if data is None or anomalies is None:
        print("Invalid data or anomalies to visualize.")
        return
    
    try:
        plt.figure(figsize=(10,6))
        plt.plot(data, label="Data Stream")
        plt.scatter(anomalies, data[anomalies], color='red', label="Anomalies")
        plt.legend()
        plt.title("Data Stream with Detected Anomalies")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.show()

    except Exception as e:
        print(f"Error visualizing data: {e}")

# Running the data stream simulation and anomaly detection
try:
    data = generate_data_stream()
    if data is not None:
        anomalies = detect_anomalies(data)
        visualize_data(data, anomalies)

except Exception as e:
    print(f"Unexpected error: {e}")