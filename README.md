# python-anomaly-detection

## Chosen Algorithm: Z-score-based Anomaly Detection

The algorithm used for the Anomaly Detection is based on the Z-score. Also known as the standard score, it tells us the distance of a data point from the mean, measured in standard deviation units. In simple words, Z-Score portrays how far a data point is from the average of a group of values. 

## Algorithm Steps:

1. **Calculate Mean and Standard Deviation:** The algorithm calculates the mean and standard deviation of the data stream. The values represent the "normal" behavior of the data.

2. **Z-Score Calculation:** For each data point, Z-Score is calculated as:
$$
Z = \frac{X - \mu}{\sigma}
$$

where: 
- \( X \) is the data point
- \( \mu \) is the mean of the values
- \( \sigma \) is the standard deviation

3. **Thresholding:** An anomaly is detected if the absolute value of the Z-Score exceeds a defined threshold, by default it is set as 3. This means the data point is more than 3 standard deviations away from the mean, indicating an unusual behavior.

## Effectiveness

Using Z-Score as an anomaly detection is simple yet effective for detecting outliers in normally distributed data. It is particularly suitable for a set  of data that follows a regular pattern but may have occasionally unexpected deviations.

**Advantages:**
- The algorithm is computationally efficient and easy to implement
- It is able to detect both positive and negative anomalies by looking at deviations from the mean
