import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# تحميل النموذج
model = tf.keras.models.load_model("D:\studying\CV internship\second task\model.keras")  
class_names = ['CaS', 'CoS', 'Gum', 'MC' , 'OC' , 'OLP' , 'OT']  

st.title("Teeth Classification 🦷")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).resize((256, 256))
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)  # غيرها حسب الموديل

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    confidence = prediction[0][class_idx]

    st.write(f"### Prediction: `{class_names[class_idx]}` ({confidence*100:.2f}%)")