# 🦷 Teeth Image Classification Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Deployed%20With-Streamlit-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview

This is a complete end-to-end **Image Classification** project built for classifying dental diseases images into their respective categories.  
The project showcases:

✅ Model from scratch using CNN  
✅ Transfer Learning using multiple pre-trained models  
✅ Evaluation and comparison  
✅ Deployment with **Streamlit UI** (demo ready!)

---

## 🧠 Problem Statement

The goal was to train a model that can **automatically classify images of teeth** into predefined classes (e.g. molar, canine, incisor...).  
This has potential use cases in **dental diagnostics** and educational tools.

---

## 🏗️ Project Structure

📦teeth-classification
┣ 📂data/ ← original images (not uploaded)
┣ 📂models/ ← saved Keras models (.keras)
┣ 📂notebooks/ ← EDA & experiments
┣ 📜app.py ← Streamlit deployment script
┗ 📜README.md

---

## ⚙️ Models Used

| Model             | Feature Extraction | Fine-Tuning | Accuracy (%) |
|------------------|--------------------|-------------|---------------|
| Custom CNN       | ✅                 | ❌          | ~57%          |
| MobileNetV2       | ✅                 | ✅          | ~91%          |
| ResNet50          | ✅                 | ✅          | ~96%          |
| EfficientNetB4    | ✅                 | ✅          | ~93%        |

> ✅ Final model selected: **ResNet50**

---

## 🔬 Data Preprocessing

- Images resized to `256x256`
- Normalization applied (`[0,1]` or `[-1,1]` based on model)
- Augmentation only on training data:
  - `RandomFlip`
  - `RandomRotation`
  - `RandomZoom`
  - `RandomContrast`

---

## 🚀 Deployment

The best model was deployed using **Streamlit** on Google Colab.  
It allows users to upload a photo and get the predicted class instantly.

---
