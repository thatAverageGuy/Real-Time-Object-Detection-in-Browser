import cv2
import torch
from torch import hub
import numpy as np
import streamlit as st
from PIL import Image
import av
from inference import predict
from streamlit_webrtc import webrtc_streamer

@st.cache(allow_output_mutation=True)
def load_model():
    """Load model from hub with custom weights."""
    model = hub.load("ultralytics/yolov5", 'custom', "connector.pt")
    model.conf = 0.8
    return model
with st.spinner('Model is being loaded..'):
        model=load_model()

st.title("Object Detector")
run = st.checkbox('Camera')

class VideoProcessor:
    def recv(self, frame):
    # def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = predict(model, img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

if run:
    webrtc_streamer(key="objectDetector", video_transformer_factory=VideoProcessor, rtc_configuration={ # Add this line
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })
