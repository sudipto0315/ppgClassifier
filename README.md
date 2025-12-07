# PPG Signal Quality Classifier

## Project Description

This project implements a machine learning-based classifier for photoplethysmography (PPG) signal quality assessment. It processes PPG signals, extracts relevant features, and uses a Random Forest classifier to distinguish between clean and noisy signals. The system includes signal preprocessing with bandpass filtering, feature extraction, and an interactive Gradio-based demo interface for real-time signal quality evaluation.

## How to Run the Notebook in the Cloud

### Google Colab

1. Upload the project files to your Google Drive or directly to Colab
2. Open `notebook/main.ipynb` in Google Colab
3. Upload the required files when prompted:
   - `data/mock_ppg_dataset.csv`
   - `src/preprocessing.py`
   - `src/visualization.py`
4. Install dependencies by running the first cell:
   ```python
   !pip install gradio -q
   ```
5. Run all cells sequentially (Runtime → Run all)

### Jupyter Notebook (Cloud Platforms)

For other cloud platforms (AWS SageMaker, Azure Notebooks, etc.):

1. Clone or upload the repository to your cloud environment
2. Ensure the following directory structure is maintained:
   ```
   ppgClassifier/
   ├── data/
   │   └── mock_ppg_dataset.csv
   ├── notebook/
   │   └── main.ipynb
   └── src/
       ├── preprocessing.py
       └── visualization.py
   ```
3. Install required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the `notebook/` directory and open `main.ipynb`
5. Run all cells in order

## How to Use the Demo

The Gradio demo interface launches at the end of the notebook execution:

1. **Run the notebook** - Execute all cells in `main.ipynb` sequentially
2. **Wait for Gradio launch** - The last cell will launch an interactive web interface
3. **Access the interface** - Click on the provided URL (local or public link)
4. **Select a signal** - Use the dropdown menu to select a Segment ID from the dataset
5. **View results** - The interface displays:
   - A visualization showing both raw and filtered PPG signals
   - Predicted label (Clean/Noisy)
   - Actual label from the dataset
6. **Test different signals** - Select different IDs to evaluate various signals

### Demo Features

- **Signal Visualization**: Plots both raw (light gray) and filtered (blue) signals
- **Real-time Prediction**: Instant classification using the trained Random Forest model
- **Comparison**: Shows predicted vs. actual labels for validation

## Assumptions and Limitations

### Assumptions

- **Sampling Frequency**: All PPG signals are assumed to be sampled at 100 Hz
- **Signal Format**: Input signals are expected to be in a parseable string format that can be converted to numerical arrays
- **Dataset Structure**: The CSV dataset must contain columns: `id`, `signal`, and `label`
- **Binary Classification**: Signals are classified into two categories (Clean/Noisy)
- **Feature Space**: The current feature extraction assumes typical PPG signal characteristics

### Limitations

- **Mock Dataset**: The classifier is trained on a mock/synthetic dataset, which may not generalize well to real-world PPG signals
- **Fixed Sampling Rate**: The system is optimized for 100 Hz signals; different sampling rates require preprocessing adjustments
- **Limited Feature Set**: Feature extraction may not capture all relevant signal quality indicators
- **Model Complexity**: Uses Random Forest with fixed hyperparameters (n_estimators=100, max_depth=8) which may not be optimal for all datasets
- **No Real-time Acquisition**: The demo works only with pre-recorded signals from the dataset
- **Memory Constraints**: All signals are loaded into memory, which may be problematic for very large datasets
- **No Cross-validation**: Model validation uses a single train-test split, not k-fold cross-validation
- **Visualization Dependency**: The `viz.visualize()` function requires the parsed signals dictionary to be in scope

## Requirements

See `requirements.txt` for complete dependency list. Key packages:
- pandas
- numpy
- matplotlib
- scipy
- scikit-learn
- gradio
