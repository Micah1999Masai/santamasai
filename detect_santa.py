from PIL import Image
import tensorflow.keras as keras
import numpy as np
import sys

def main() :
    file_uploaded = st.file_uploader('Choose an image...', type = 'jpg')
    if file_uploaded is not None :
        image = Image.open(file_uploaded)
        st.write("Uploaded Image.")
        figure = plt.figure()
        plt.imshow(image)
        plt.axis('off')
        st.pyplot(figure)
def predict_class(image) :
    with st.spinner('Loading Model...'):
        classifier_model = keras.models.load_model(r'mynetwork.h5', compile = False)
model = keras.Sequential([hub.KerasLayer(classifier_model, input_shape = shape)])
pred = model.predict(image_np)
print(pred)
