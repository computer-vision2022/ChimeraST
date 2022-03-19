#Build Stramlit App
import streamlit as st
from PIL import Image
import os

st.title("Progressive Attentional Manifoid Alignment for Arbitrary Style Transfer")

content = st.file_uploader("Upload the content image here (jpg)", type=['jpg'])
style = st.file_uploader("Upload the style image here (jpg)", type=['jpg'])

if (content is not None) and (style is not None):
    content_image = Image.open(content)
    content_image.save("images/content-images/user-content.jpg")
    st.image(content_image, caption='Your Content Image', use_column_width=True)
    style_image = Image.open(style)
    style_image.save("images/style-images/user-style.jpg")
    st.image(style_image, caption='Your Style Image', use_column_width=True)

    os_cmd = "python3 main.py eval --content images/content-images/user-content.jpg --style images/style-images/user-style.jpg"

    if st.button('Create Style Transfer Image'):
        os.system(os_cmd)
        st.image("ics.jpg", caption='Stylized', use_column_width=True)
    else:
        st.write('click button to run model')
