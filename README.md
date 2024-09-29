# Self-Organizing Maps on Wine Quality Dataset

## Objective
To perform dimensionality reduction and clustering on the Wine Quality dataset using Self-Organizing Maps (SOM), allowing for the visualization of patterns and relationships between wine attributes.

## Introduction
Self-Organizing Maps (SOM) are a type of artificial neural network used for unsupervised learning, particularly in tasks involving dimensionality reduction and clustering. In this project, we apply SOM to the Wine Quality dataset, which contains various attributes of red and white wines. The goal is to identify patterns in the data and visualize how the attributes affect wine quality.

## Dataset
The Wine Quality dataset consists of 1599 red wine samples and 4898 white wine samples. Each wine sample is described by 11 physicochemical properties (such as alcohol, acidity, sugar content) and a quality score ranging from 0 to 10.

### Dataset Link:
You can download the dataset from [Kaggle: Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009).

## Steps of Execution

1. **Download the dataset**: Ensure the dataset (`winequality.csv`) is placed in the `data/` folder.
2. **Install required packages**: Install the dependencies using `pip install -r requirements.txt`.
3. **Run the SOM**: Execute the script with `python src/som_wine_quality.py`.
4. **Visualize results**: The SOM output plots will be generated using `matplotlib` and displayed on the screen.

## Dataset Explanation
The dataset contains the following attributes:

- `fixed acidity`
- `volatile acidity`
- `citric acid`
- `residual sugar`
- `chlorides`
- `free sulfur dioxide`
- `total sulfur dioxide`
- `density`
- `pH`
- `sulphates`
- `alcohol`
- `quality`: Target variable representing the wine quality score (integer between 0 and 10).

## Hardware/Software Requirements
- Python 3.7 or higher
- Libraries: numpy, pandas, matplotlib, minisom
- i3 processor
- 8GB ram
- 500mb hard disk space minimum

To install the required libraries, use the following command:
```bash
pip install numpy pandas matplotlib minisom
