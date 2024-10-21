import streamlit as st
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import dotenv

# Load environment variables
ENV = dotenv.dotenv_values(".env")

# Create an Image Analysis client
client = ImageAnalysisClient(
    endpoint=ENV["AZURE_VISION_ENDPOINT"],
    credential=AzureKeyCredential(ENV["AZURE_VISION_KEY"])
)

st.title("👀 Vision")

col1, col2, col3 = st.columns([3,0.5,3])

with col1:
    uploaded_img = st.file_uploader("Upload image(s)")

    if uploaded_img:
        result = client.analyze(
            image_data=uploaded_img,
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
            gender_neutral_caption=True,  # Optional (default is False)
        )
        
        with col3:
            
            # Get a caption for the image. This will be a synchronously (blocking) call.
            st.subheader("Image analysis results:")
            
            # Print caption results to the console
            st.write(" Caption:")
            if result.caption is not None:
                st.write(f"'{result.caption.text}', Confidence {result.caption.confidence:.4f}")

            # Print text (OCR) analysis results to the console
            st.write(" Read:")
            if result.read is not None:
                for line in result.read.blocks[0].lines:
                    st.write(f"Line: '{line.text}', Bounding box {line.bounding_polygon}")
                    for word in line.words:
                        st.write(f"Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")