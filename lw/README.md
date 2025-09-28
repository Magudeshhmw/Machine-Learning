# Machine Learning & Data Science Showcase

Welcome to this collection of machine learning and data science projects. This repository is designed for beginners and enthusiasts to explore various algorithms and concepts in a practical way. Each Jupyter Notebook is a self-contained example with clear explanations.

**Author:** Magudeshwaran and Senthilkumaran

---

## Table of Contents

1.  [Getting Started](#getting-started)
2.  [Notebook Descriptions](#notebook-descriptions)
    *   [Regression](#regression)
    *   [Classification](#classification)
    *   [Clustering](#clustering)
    *   [Neural Networks](#neural-networks)
    *   [Time Series](#time-series)
    *   [Association Rule Mining](#association-rule-mining)
    *   [Python Libraries & Concepts](#python-libraries--concepts)
    *   [Statistics & Data Preprocessing](#statistics--data-preprocessing)

---

## Getting Started

To run these notebooks on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd <repository-name>
    ```
3.  **Install the required libraries.** You will need libraries such as `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, and `tensorflow`. You can install them using pip:
    ```bash
    pip install numpy pandas scikit-learn matplotlib seaborn tensorflow
    ```
4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
5.  Open any of the `.ipynb` files to explore the code.

---

## Notebook Descriptions

Here is a detailed breakdown of each notebook in this repository.

### Regression

*   **`linear_regression.ipynb`**: A fundamental example of simple linear regression, predicting a continuous value based on a single input feature.
*   **`multi_linear_regression.ipynb`**: An extension of linear regression that uses multiple input features to predict a continuous value.
*   **`multi_linear_regression_3d_v2.ipynb`**: A visually engaging example of multiple linear regression with two features, including a 3D plot to visualize the regression plane.

### Classification

*   **`logistic_regression.ipynb`**: A classic example of logistic regression for binary classification problems.
*   **`knn_classifier.ipynb`**: Implements the K-Nearest Neighbors algorithm, a simple yet powerful classification method based on feature similarity.
*   **`decision_tree_classifier.ipynb`**: Demonstrates how to use a decision tree for classification tasks, showing how the algorithm splits the data based on features.
*   **`random_forest_classifier.ipynb`**: An example of the Random Forest algorithm, which is an ensemble of decision trees, used here for digit recognition.
*   **`naive_bayes_classifier.ipynb`**: Implements the Naive Bayes classifier, a probabilistic algorithm based on Bayes' theorem, for a simple classification task.
*   **`mnist_digit_recognition.ipynb`**: A more advanced digit recognition example using a Random Forest classifier on the famous MNIST dataset.

### Clustering

*   **`kmeans_clustering.ipynb`**: Implements the K-Means clustering algorithm, which groups data points into a predefined number of clusters.
*   **`dbscan_clustering.ipynb`**: An example of DBSCAN (Density-Based Spatial Clustering of Applications with Noise), an algorithm that groups together points that are closely packed together.
*   **`dbscan_weather.py`**: A Python script applying the DBSCAN algorithm to weather data.

### Neural Networks

*   **`ann_insurance.ipynb`**: A basic example of an Artificial Neural Network (ANN) for an insurance-related prediction task.

### Time Series

*   **`arima_model.ipynb`**: Implements the ARIMA (AutoRegressive Integrated Moving Average) model, a popular model for time series forecasting.

### Association Rule Mining

*   **`apriori_association.ipynb`**: An example of the Apriori algorithm, which is used to find frequent itemsets in a dataset and generate association rules.

### Python Libraries & Concepts

*   **`numpy_examples.ipynb`**: A guide to fundamental operations in the NumPy library, including array creation, indexing, and mathematical operations.
*   **`pandas_examples.ipynb`**: Demonstrates basic Pandas operations, focusing on DataFrame creation and manipulation from dictionaries.
*   **`matplotlib_examples.ipynb`**: A showcase of various 2D and 3D plotting techniques using Matplotlib and Seaborn, including bar, line, scatter, joint, and 3D scatter plots.
*   **`regex_examples.ipynb`**: A handy guide with examples of how to use regular expressions in Python for pattern matching.

### Statistics & Data Preprocessing

*   **`binomial_distribution_part2.ipynb`**: A notebook that explains and visualizes the binomial distribution, a fundamental concept in statistics.
*   **`statistics_examples.ipynb`**: A tutorial on how to calculate basic statistical measures like mean, median, mode, and variance in Python.
*   **`standard_scaler_example.ipynb`**: Demonstrates how to use `StandardScaler` from scikit-learn to standardize features, a common preprocessing step.
