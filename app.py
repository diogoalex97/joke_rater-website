from PIL import Image
import streamlit as st
from analyzetext import analyze_text, classify_text, remove_word_from_string
from frame import load_jokes_data, top3_jokes, filter_jokes
import matplotlib.pyplot as plt

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

jokes_data = load_jokes_data()



# # # WEBPAGE
# # Sidebar
st.sidebar.write(text_center("<h1>#1242 Data Science Bootcamp Project</h1>"), unsafe_allow_html=True)

st.sidebar.write(text_justify(f"   Hey there, from {u_funny} team. The presented product is the final version of our bootcamp's project. We choose to create a dynamic and entertaining <b>joke classifier</b>, where you can input a joke and the model will classify its theme, as in the type (knock-knock, dad, dark,...) and topic (politics, animal, technology) of the joke; it will then predicted its engagement level. I'll give you an idea of what's going on, behind this (<b>beautifully designed</b>) Website:"), unsafe_allow_html=True)


st.sidebar.markdown(
    """
    <ul>
        <li>You start by inputting your joke into the pipeline</li>
        <li>Inside, we have two models working:</li>
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="list-style-type: none; margin-left: 0;">‣ Model 1) Will predict your joke's engagement level</li>
            <li style="list-style-type: none; margin-left: 0;">‣ Model 2) Will predict your joke's class (type and topic of humor)</li>
            </ul>
        <li>The output will be the classification and the engagement score. It will also allow you to see, related to your joke class, some statistics and three more jokes of the same theme of humor</li>
        <li>Finally, we want to point out that our base data was obtained from (sub)Reddit, meaning it's the backbone of all our predictions.</li>
    </ul>
    """,
    unsafe_allow_html=True
)
st.sidebar.write(text_justify("   We hope you can enjoy and have fun with the interactions."), unsafe_allow_html=True)
st.sidebar.write("")
st.sidebar.write(f"<div>{the_team}</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Diogo Oliveira</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Jorge Silva</div>", unsafe_allow_html=True)
st.sidebar.write("<div style='padding: 0'>Liam McHugh</div>", unsafe_allow_html=True)





# # Main Page
st.write(text_center("<h1>U Funny</h1>"), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.header(" ")
with col2:
    st.image(mascot, width=200)
with col3:
    st.header(" ")

st.write(text_justify(f"<h5>Hey, I'm {hijinks}, the brilliant product that is going to predict what theme of jokes can you come up with, make me proud! (acknowledge my 'stache, it's glorious).</h5>"), unsafe_allow_html=True)
st.write(text_justify("<h5>I'm a two-week product of three handsome guys. Expect <u>mediocracy</u>, like the jokes I'm assuming you're inputting.</h5>"), unsafe_allow_html=True)
st.write(text_justify("<h5>Since Chat GPT can't generate more than 25 jokes (or variants), the fact I can classify your jokes means I'm pretty awesome. You know, in a 'what your parents expect of you' kind of way.</h5>"), unsafe_allow_html=True)


# Text Input Box
st.write("<h5>In case you want to give it a go, type a joke below</h5>", unsafe_allow_html=True)
joke_input = st.text_area("")

# Perform analysis when the button is clicked

if st.button('LETS GOOO!') :
    st.session_state.submit = True

if  st.session_state.get("LETS GOOO!", False):
    if joke_input:
        # reaction to joke
        st.success(f"Processing your joke, give me a sec...")

        # print type and topic
        type_, topic = analyze_text(joke_input)

        modified_type= remove_word_from_string(type_, 'Humor')
        modified_topic = remove_word_from_string(topic, 'Jokes')
        st.write("<b>Type of humor :</b>", modified_type, unsafe_allow_html=True)
        st.write("<b>Topic of the Joke :</b>", modified_topic, unsafe_allow_html=True)
        # statistics on type and topic
        # st.write(f"<b> Average number of comments for {modified_type} {modified_topic} jokes:</b>",str(round(calculate_average(jokes_data,"ncom_raw","type humor",type_,"topic joke",topic),2)),unsafe_allow_html=True)
        # st.write("<b> Average number of interaction with these types:</b>",str(round(calculate_average(jokes_data,"score_raw","type humor",type_,"topic joke",topic),2)),unsafe_allow_html=True)
        # st.write("<b> Average of upvote ratio for these types:</b>",str(round(calculate_average(jokes_data, "ratio_0_to_10", "type humor", type_, "topic joke", topic),2) * 100) + "%",unsafe_allow_html=True)
        st.write("<b> Engagement percentage:</b>",str(round(classify_text(joke_input),2)),unsafe_allow_html=True)
        st.write("(Note that this rate is definitely not reliable!! I'll fixe it one day)",unsafe_allow_html=True)
        filtered_jokes = filter_jokes(jokes_data, "type humor",type_,"topic joke",topic)
        fig, axes = plt.subplots(1, 3, figsize=(10, 3))

        filtered_jokes["ncom_raw"].plot.hist(bins=40, color='blue', ax=axes[0])
        filtered_jokes["score_raw"].plot.hist(bins=40, color='orange', ax=axes[1])
        filtered_jokes["ratio_0_to_10"].plot.hist(bins=20, color='pink', ax=axes[2])

        axes[1].set_ylabel("")
        axes[2].set_ylabel("")
        axes[0].set_title('Number of comments')
        axes[1].set_title('Number of interactions')
        axes[2].set_title('Upvote ratio')
        with st.expander(f"See metrics for {modified_type}/{modified_topic}"):
            st.pyplot(fig)


        if (st.button('Wanna see what I can do? Ask for more jokes of the same theme of yours.')):
        # more jokes
            filtered_jokes = top3_jokes(jokes_data, "type humor", type_,"topic joke", topic)
            for joke in filtered_jokes:
                st.write(joke)
    else:
        st.write("You can type your joke, I won't bite.")



# display the name when the submit button is clicked
# .title() is used to get the input text string
