Min-max normalization, also known as feature scaling or min-max scaling, is a data normalization technique used in machine learning and statistics to rescale a feature's values within a certain range, typically between 0 and 1.

The formula for min-max normalization is:

\[ X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}} \]

Where:
- \( X \) is the original value of the feature.
- \( X_{\text{min}} \) is the minimum value of the feature in the dataset.
- \( X_{\text{max}} \) is the maximum value of the feature in the dataset.
- \( X_{\text{norm}} \) is the normalized value of the feature.

This normalization method is useful when the input features have different scales and units. By scaling all features to the same range, min-max normalization ensures that each feature contributes equally to the analysis and prevents features with large scales from dominating those with smaller scales.

However, min-max normalization may not be suitable if the dataset contains outliers, as they can heavily influence the calculation of the minimum and maximum values. In such cases, robust normalization techniques like z-score normalization (standardization) may be more appropriate.


Z-score normalization, also known as standardization, is a data normalization technique used in statistics and machine learning to rescale features with a Gaussian distribution (normal distribution) to a standard normal distribution with a mean of 0 and a standard deviation of 1.

The formula for z-score normalization is:

\[ Z = \frac{X - \mu}{\sigma} \]

Where:
- \( X \) is the original value of the feature.
- \( \mu \) is the mean of the feature in the dataset.
- \( \sigma \) is the standard deviation of the feature in the dataset.
- \( Z \) is the standardized value of the feature.

Standardizing the data in this way centers the distribution around 0 and expresses each data point's distance from the mean in terms of the number of standard deviations. Features with different scales and units can be effectively compared after standardization. It also makes it easier to interpret the data, especially in the context of statistical analyses.

Z-score normalization is robust to outliers compared to min-max normalization since it is based on the mean and standard deviation rather than the range of the data. However, it may not be suitable for data that do not follow a Gaussian distribution. In such cases, alternative normalization methods may be more appropriate.
