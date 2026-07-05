import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


model = tf.keras.models.load_model("rock_type_classifier.keras")

class_names = [
    "Limestone",
    "Sandstone",
    "Shale"
]
rock_info = {

        "Limestone":
        """
        Limestone is a sedimentary rock composed mainly of calcium carbonate.

        • Reservoir rock for hydrocarbons
        • Used in cement production
        • Important in petroleum exploration
        """,

        "Sandstone":
        """
        Sandstone is a porous sedimentary rock.

        • Excellent petroleum reservoir
        • High porosity and permeability
        • Stores oil and natural gas
        """,

        "Shale":
        """
        Shale is a fine-grained sedimentary rock.

        • Source rock for hydrocarbons
        • Rich in organic matter
        • Produces shale oil and shale gas
        """
    }
st.set_page_config(
    page_title='Rock Type Classifier',
    page_icon="🪨",
    layout = "centered"
)
st.sidebar.title("About")

st.sidebar.write("""
    ### Rock Type Classification

    Model:
    - MobileNetV2 (Transfer Learning)

    Dataset:
    - Limestone
    - Sandstone
    - Shale

    Framework:
    - TensorFlow
    - Streamlit
    """)



st.title("Rock Type Classification")
st.info("""
**Model Disclaimer**

This classifier was developed as an educational Purposes**.

Current validation accuracy is approximately **74%**.

Prediction performance may vary because of:
- Limited dataset size
- Similar visual characteristics among rock types
- Differences in lighting, camera angle, and image quality

This application should not be used as a substitute for professional geological or laboratory analysis.
""")
st.write("Upload a rock image to classify it")

uploaded_file = st.file_uploader(
    "choose a rock image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((224,224))
    img_array = np.array(image)
    img_array = img_array.astype("float32")/255.0
    img_array = np.expand_dims(img_array,axis=0)

    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)

    st.subheader("Prediction")

    st.success(f"🪨 {class_names[predicted_class]}")

    st.subheader("Prediction Confidence")

    for i, rock in enumerate(class_names):
        st.write(f"**{rock}**")
        st.progress(float(prediction[0][i]))
        st.write(f"{prediction[0][i]*100:.2f}%")


    
    


    st.subheader('Rock Information')
    st.info(rock_info[class_names[predicted_class]])


st.markdown('---')

st.caption(
        "Developed by : Sayan Das"
    )
    

