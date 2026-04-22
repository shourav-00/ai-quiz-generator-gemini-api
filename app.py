import streamlit as st
st.title("Note Summary and Quiz Genarator")
st.markdown("Upload below or equal to 3 images to genarate Note summary and Quizes")
st.divider()

from api import note_gen,audio_gen,quiz_gen
from PIL import Image


with st.sidebar:
    st.header("Controls")
    st.markdown("Upload your photos")
    img=st.file_uploader(
        "Select Images",
        type=["img","png","avif"],
        accept_multiple_files=True
    )
    
    if img:
        if len(img)>3:
            st.error("You uploaded more than 3 images")
        else:
            col=st.columns(len(img))
            for i,each_img in enumerate(img):
                with col[i]:
                    st.image(each_img)
    st.markdown("Enter the difficulty of the quiz")
    select=st.selectbox(
        "Choose an option:",
        ("Easy","Medium","Hard"),
        index=None
    )
    if select:
        st.markdown(f"You seleceted :green[{select}] option")
    
         
    btn=st.button("Click the button to initiate AI",type="primary")



if btn:
    pil_img_list=[]
    for x in img:
        pil_img=Image.open(x)
        pil_img_list.append(pil_img)
    if not img:
        st.error("You have to select at least one image")
    if not select:
        st.error("You have to select the difficulty level")
    if img and select:
        with st.container(border=True):
            st.header("Your note")
            response_one=note_gen(pil_img_list)
            st.write(response_one)
        with st.container(border=True):
            st.subheader("Audio Helpline")
            response_one= response_one.replace("-","")
            response_one= response_one.replace("_","")
            response_one= response_one.replace("/","")
            response_one= response_one.replace("*","")
            response_one= response_one.replace("*","")
            response_two=audio_gen(response_one)
            st.audio(response_two)
        with st.container(border=True):
            st.subheader("Try on :green[Your own]")
            response_three=quiz_gen(pil_img_list,select)
            st.write(response_three)

