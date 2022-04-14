# Real-Time-Object-Detection-in-Browser
Streamlit app for real-time object detection in browser using OpenCV and yolov5 trained on custom data.

Steps to run locally:
   
   1. Clone the Dev Branch to local.
   >git clone -b Dev https://github.com/mohityogesh44/Real-Time-Object-Detection-in-Browser.git
   
   2. Create a virtual environment.(optional)
   >python -m virtualenv cam
   
   3. Activate virtualenv. (Only if step 2 is done).
   > Linux --> source cam/bin/activate | Windows --> . ./cam/Scripts/activate
   
   4. Install requirements.
   > pip install -r requirements.txt
   
   5. Run server.
   > streamlit run main.py
