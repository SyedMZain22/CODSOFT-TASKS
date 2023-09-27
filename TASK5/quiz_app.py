import streamlit as st
from streamlit_lottie import st_lottie
import requests
#task05
#syed muhamamd zain bin faisal

st.set_page_config(page_title="QUIZ", page_icon=":maple_leaf:", layout="wide")


def load_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


animation_url = "https://lottie.host/6abc3b57-340b-4abe-b8db-360262d3c9a6/aOOznDAYyB.json"
animation_json = load_url(animation_url)
st_lottie(animation_json, height=550, key="coding1")
ani_url="https://lottie.host/c28c3b38-398b-4fde-856c-08ffbaf56d82/cA0oxXLHJG.json"
ani_j=load_url(ani_url)


with st.container():
    st.write("--------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('RULES AND INSTRUCTIONS')
        everthing='''
**Introduction:**
Hi :wave:, My Name is Zain and
i have design this quiz and i am also a Gen Z.

**Quiz Overview:**
Test your knowledge about the Gen Z generation
Multiple-choice questions
Select the correct answer for each question
Final score calculated at the end

**Quiz Format:**
Questions about Gen Z
Three options per question
Choose the correct answer

**Answering Questions:**
Select one option per question: Type (a,b or c)

**Submitting Answers:**
Click/tap "calculate score"

**Scoring System:**
One point per correct answer.
No negative marking

**Enjoy and Learn:**
Expand understanding of Gen Z,
Have fun and embrace learning
'''
        st.write(everthing)
    with right_column:

        st_lottie(ani_j, height=450, key="coding2")


st.write("-------")
st.title("LET THE QUIZ BEGIN, BEST OF LUCK!")
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define the questions
questions = [
    Question("**What years define the Gen Z generation?**"
             "\n(a) 1980s-1990s\n(b) 1990s-2000s\n(c) 2000s-2010s\n\n", "b"),
    Question("**Which social media platform is most popular among Gen Z?** "
             "\n(a) Facebook\n(b)  Instagram\n(c) LinkedIn\n\n", "b"),
    Question("**Which popular app allows users to create and share short videos?**"
             "\n(a) Snapchat\n(b) TikTok\n(c) WhatsApp\n\n", "b"),
    Question("**What is the term used to describe the fear of missing out, often associated with Gen Z?**"
             "\n(a) LOL\n(b) YOLO\n(c) FOMO\n\n", "c"),
    Question("**Which environmental issue is of great concern to Gen Z?**"
             "\n(a) Climate Change\n(b) Deforestation\n(c) Water pollution\n\n", "a"),
    Question("**Which Gen Z activist gained worldwide attention for her work on gun control in the United States?**"
             "\n(a) Malala Yousafzai\n(b) Emma Gonzalez\n(c) Greta Thunberg\n\n", "b"),
    Question("**Which streaming platform became popular among Gen Z for gaming content?**"
             "\n(a) Twitch\n(b) Netflix\n(c) Hulu\n\n", "a"),
    Question("**What is the term used to describe the generation that comes after Gen Z?**"
             "\n(a) Generation Alpha\n(b) Generation Y\n(c) Generation X\n\n", "a"),
    Question("**Which popular Gen Z slang term means 'cool' or 'awesome'?** "
             "\n(a) Lit\n(b) Salty\n(c) Yeet\n\n", "a"),
    Question("**Which music genre is most popular among Gen Z?**"
             "\n(a) Hip Hop\n(b) Rock\n(c) Country\n\n", "a"),
    Question("**Who design this Quiz??**"
             "\n(a) Xen\n(b) Zayn\n(c) Zain\n\n", "c")
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    correct_count = 0
    incorrect_count = 0
    user_answers = []

    for question in questions:
        answer = st.text_input(question.prompt)
        user_answers.append(answer.lower())

    if st.button("Calculate Score"):
        for i in range(len(questions)):
            if user_answers[i] == questions[i].answer:
                score += 1
                correct_count += 1
            else:
                incorrect_count += 1
        st.subheader("You got " + str(score) + "/" + str(len(questions)) + " correct!")
        st.write("Correct answers: " + str(correct_count))
        st.write("Incorrect answers: " + str(incorrect_count))

# Run the quiz
run_quiz(questions)
