import cv2
from torch import hub
import numpy as np
import streamlit as st
from PIL import Image
from inference import predict

@st.cache(allow_output_mutation=True)
def load_model():
    """Load model from hub with custom weights."""
    model = hub.load("ultralytics/yolov5", 'custom', "connector.pt")
    return model

if __name__=="__main__":

    #Load Model
    with st.spinner('Model is being loaded..'):
        model=load_model()

    st.title("Object Detector")
    run = st.checkbox('Camera')
    image = st.checkbox("Image File Upload")
    
    #webcam feed
    if run:
        st.title("Webcam Feed")
        FRAME_WINDOW = st.image([])
        cam = cv2.VideoCapture(0)
        while run:
            ret, frame = cam.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = predict(model, frame)
            FRAME_WINDOW.image(frame)
        else:
            cam.release()
            st.write('Stopped')

    #Image file upload
    elif image:
        st.title("Upload Image File")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = np.array(Image.open(uploaded_file))
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("")
            st.write("Classifying...")
            im = predict(model, image)
            st.image(im)