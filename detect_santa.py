from PIL import Image
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
model = load_model('mynetwork.h5')
pred = model.predict(image_np)
print(pred)
