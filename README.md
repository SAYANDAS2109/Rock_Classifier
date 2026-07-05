# 🪨 Rock Type Classification using Deep Learning

An end-to-end Deep Learning project that classifies sedimentary rock images into **Limestone, Sandstone, and Shale**. The project explores both a **Custom Convolutional Neural Network (CNN)** and **Transfer Learning with MobileNetV2**, followed by deployment as an interactive **Streamlit web application**.

---

## 📌 Project Overview

This project focuses on automated rock type classification for geological and petroleum-related applications. A custom CNN was initially developed as a baseline model, followed by a Transfer Learning approach using MobileNetV2 to improve classification performance.

The web application allows users to upload a rock image and receive:

- Predicted rock type
- Prediction confidence
- Geological information about the predicted rock

---

## Live Demo
-link

## Linkedin
-link

## 🚀 Features

- Custom CNN implementation
- Transfer Learning using MobileNetV2
- Image classification into:
  - Limestone
  - Sandstone
  - Shale
- Streamlit web application
- Confidence visualization
- Geological information display

---

## 🧠 Models Implemented

### 1. Custom CNN
A Convolutional Neural Network was built from scratch using:

- Convolution Layers
- MaxPooling Layers
- Batch Normalization
- Dropout
- Dense Layers

This model served as the baseline for comparison.

### 2. Transfer Learning (Final Model)

To improve performance, **MobileNetV2** pretrained on ImageNet was used.

Architecture:

- MobileNetV2 (Frozen Base)
- Global Average Pooling
- Dense (256, ReLU)
- Dropout (0.3)
- Dense (Softmax)

The upper layers were later fine-tuned for improved performance.

---

## 📊 Dataset

The dataset consists of images belonging to three sedimentary rock classes:

- Limestone
- Sandstone
- Shale

Dataset Split:

- 80% Training
- 20% Validation

---

## ⚙️ Training

### Data Augmentation

- Random Flip
- Random Rotation
- Random Zoom

### Optimization

- Adam Optimizer
- Sparse Categorical Crossentropy
- Early Stopping
- ReduceLROnPlateau

---

## 📈 Results

### Final Model

**MobileNetV2 Transfer Learning**

Validation Accuracy:

**74%**

### Classification Report

| Class | Precision | Recall | F1-score |
|--------|----------:|--------:|---------:|
| Limestone | 0.66 | 0.86 | 0.75 |
| Sandstone | 0.76 | 0.82 | 0.79 |
| Shale | 0.93 | 0.49 | 0.64 |

Overall Accuracy:

**74%**

---

## 💻 Streamlit Application

The application provides:

- Image Upload
- Rock Prediction
- Prediction Confidence
- Geological Information

---

## 📂 Project Structure

```
Rock_Classifier/
│
├── app.py
├── rock_type_classifier.keras
├── requirements.txt
├── README.md

```

---

## 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Rock_Classifier.git
```

Navigate to the project

```bash
cd Rock_Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- MobileNetV2
- Convolutional Neural Networks (CNN)
- NumPy
- Streamlit
- Pillow
- Scikit-learn

---

## ⚠️ Limitations

The model achieves approximately **74% validation accuracy**, but performance is limited by:

- Relatively small dataset
- Only three rock classes
- Visual similarity between sedimentary rocks
- Sensitivity to image quality, lighting, and viewing angle

This application is intended for educational and demonstration purposes and should not replace professional geological analysis.

---

## 🔮 Future Improvements

- Expand the dataset
- Add additional rock classes
- Experiment with ConvNeXt
- Hyperparameter optimization

---

## 👨‍💻 Author

**Sayan Das**

