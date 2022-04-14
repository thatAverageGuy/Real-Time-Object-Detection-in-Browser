import cv2
from torch import hub
import numpy as np
import streamlit as st
from PIL import Image
from inference import predict
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

@st.cache(allow_output_mutation=True)
def load_model():
    """Load model from hub with custom weights."""
    model = hub.load("ultralytics/yolov5", 'custom', "connector.pt")
    return model

if __name__=="__main__":

    with st.spinner('Model is being loaded..'):
            model=load_model()

    st.title("Object Detector")
    run = st.checkbox('Camera')

    class VideoTransformer(VideoTransformerBase):
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            img = predict(model, img)

            return img
    if run:
        webrtc_streamer(key="objectDetector", video_transformer_factory=VideoTransformer)
