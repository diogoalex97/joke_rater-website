import streamlit as st
from PIL import Image

# Check the website: make streamlit



# Images
mascot = Image.open("objects/mascot.png")

# Text Justified
def text_justify(text):
    return f"<div style='text-align: justify;'>{text}</div>"

# Text Centered
def text_center(text):
    return f"<div style='text-align: center;'>{text}</div>"

# Color green
def color_text(text):
    return f"<span style='color: green;'>{text}</span>"
u_funny = color_text("U Funny's")
hijinks = color_text("Hijinks")
the_team = color_text("The team:")

# Remove the space above the text box
# "<h1 style='padding: 0'>TEXT</h1>"





# # # WEBPAGE
# # Sidebar
st.sidebar.write(text_center("<h1>#1242 Data Science Bootcamp Project</h1>"), unsafe_allow_html=True)

st.sidebar.write(text_justify(f"Hey there, from {u_funny} team. The presented product is the final version of our bootcamp's project. We choose to create a dynamic and entertaining <b>joke classifier</b>, where you can input a joke and the model will rate it for its predicted engagement level. I'll give you an idea of what's going on, behind this (<b>beautifully designed</b>) Website:"), unsafe_allow_html=True)


st.sidebar.markdown(
    """
    <ul>
        <li>You start by inputting your joke into the pipeline</li>
        <li>Inside, we have two models working:</li>
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="list-style-type: none; margin-left: 0;">‣ Model 1) Your joke will be rated into a score of engagement</li>
            <li style="list-style-type: none; margin-left: 0;">‣ Model 2) Your joke will be classified into a type and topic of humor</li>
        </ul>
        <li>Now that we have your joke's type and topic of humor rated, we will compare them with the average of our database</li>
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="list-style-type: none; margin-left: 0;">‣ Depending if it's higher, around the same value, or worst, we will give you, as an output, that information (we might do it in our special way, since, you know, humor!)</li>
        </ul>
        <li>Finally, we want to point out that our base data was obtained from (sub)Reddit, meaning it's the backbone of all our predictions</li>
    </ul>
    """,
    unsafe_allow_html=True
)
st.sidebar.write(text_justify("We hope you can enjoy and have fun with the interactions."), unsafe_allow_html=True)
st.sidebar.write("")
st.sidebar.write(f"<div>{the_team}</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Diogo Oliveira</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Jorge Silva</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Liam McHugh</div>", unsafe_allow_html=True)





# # Main Page
st.write(text_center("<h1>U Funny's</h1>"), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.header(" ")
with col2:
    st.image(mascot, width=200)
with col3:
    st.header(" ")

st.write(text_justify(f"<h5>Hey, I'm {hijinks}, the brilliant result product of three dudes' work (acknowledge my 'stache, it's glorious).</h5>"), unsafe_allow_html=True)
st.write(text_justify("<h5>I'm a two-week product of Natural Language Processing (NLP) from subreddits datasets. Expect <u>mediocracy</u>, like the jokes I'm assuming you're inputting. Think that not even Chat GPD can generate more than 25 jokes (or variants), so I'm saying I'm awsome, in a 'what your parents expect of you' way.</h5>"), unsafe_allow_html=True)

# Text Input Box
st.write("<h5>In case you want to give it a go, type a joke on the space bellow</h5>", unsafe_allow_html=True)
joke_input = st.text_input("who would have guessed that's what the bar was for... shocking, I know", label_visibility='collapsed')
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = joke_input.title()
    st.success(f"Processing {result}, good luck")
