import requests  # For making API calls
import nltk
nltk.download('punkt')
nltk.download('stopwords')

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize the PorterStemmer
ps = PorterStemmer()

# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the vectorizer and model
tk = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Function to fetch location from phone number
def get_location(phone_number):
    try:
        # Placeholder for actual API call (replace with your API)
        response = requests.get(f"https://api.example.com/phone_location?number={phone_number}")
        if response.status_code == 200:
            data = response.json()
            return data.get("location", "Location not found")
        else:
            return "Unable to fetch location. Check the phone number or try again later."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit interface
st.set_page_config(page_title="SMS Spam Detection", page_icon="📱")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f3e6f7, #d9ecf2);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        max-width: 800px;
        margin: auto;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: violet;
        text-align: center;
        font-size: 40px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .subtitle {
        color: blue;
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .input {
        color: #333;
        font-size: 18px;
    }
    .button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .result {
        color: #27ae60;
        text-align: center;
        font-size: 28px;
        margin-top: 20px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #888;
    }
    .footer a {
        color: GREEN;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .phone-box {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<div class="title">SMS Spam Detection Model</div>', unsafe_allow_html=True)
    # st.markdown('<div class="subtitle">Created by Abhishek</div>', unsafe_allow_html=True)

    input_sms = st.text_area("Enter the SMS", key="sms_input", help="Type the SMS message you want to check for spam.")
    sender_name = st.text_input("Sender's Name (Optional)", key="sender_name", help="Enter the name of the sender, if known.")
    phone_number = st.text_input("Enter Phone Number", key="phone_number", help="Enter the phone number to check location.", max_chars=15)

    if st.button('Predict', key="predict_button"):
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tk.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.markdown('<div class="result">Spam</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result">Not Spam</div>', unsafe_allow_html=True)

        if sender_name:
            st.write(f"Message sent by: {sender_name}")

        if phone_number:
            st.write(f"Fetching location for phone number: {https://api.example.com/phone_location?number=9341380920}...")
            location = get_location(phone_number)
            st.write(f"Location: {location}")

    # st.markdown('<div class="footer">Made with ❤️ by <a href="https://github.com/Abhishek72-avail">Abhishek</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        margin-top: 60px;
        color: White;
        font-size: 14px;
        line-height: 1.6;
    }
    .footer a {
        color:Green;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ by <a href="https://github.com/Abhishek72-avail">Abhishek</a></p>
        <hr style="border: 0; height: 1px; background: #ddd;">
        <h4>What is SMS Spam Detection?</h4>
        <p>
            SMS Spam Detection is a process of identifying unwanted, unsolicited, and potentially harmful messages
            using machine learning algorithms. These messages are often sent in bulk to advertise products, promote
            scams, or spread malware.
        </p>
        <h4>How to Use This Tool?</h4>
        <ol>
            <li>Enter the SMS message you want to analyze in the text area provided.</li>
            <li>If you know the sender's name, you can enter it in the "Sender's Name" field (optional).</li>
            <li>To find the location of the sender's phone number, enter the number in the "Phone Number" field (optional).</li>
            <li>Click the "Predict" button to classify the SMS as "Spam" or "Not Spam."</li>
        </ol>
        <p>
            This tool uses Natural Language Processing (NLP) and machine learning to analyze SMS content and identify
            patterns commonly associated with spam messages.
        </p>
        <p>For more information, check out the <a href="https://github.com/Abhishek72-avail">GitHub Repository</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)

















# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# # Initialize the PorterStemmer
# ps = PorterStemmer()

# # Function to preprocess text
# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)

#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         y.append(ps.stem(i))

#     return " ".join(y)

# # Load the vectorizer and model
# tk = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open("model.pkl", 'rb'))

# # Streamlit interface
# st.set_page_config(page_title="SMS Spam Detection", page_icon="📲", layout="centered")

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     body {
#         font-family: 'Roboto', sans-serif;
#         background: linear-gradient(135deg, #74ebd5, #9face6);
#         margin: 0;
#         padding: 0;
#     }
#     .main-container {
#         background-color: #ffffff;
#         padding: 30px;
#         border-radius: 15px;
#         box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
#         max-width: 600px;
#         margin: 50px auto;
#     }
#     .title {
#         color: #2d2e82;
#         text-align: center;
#         font-size: 36px;
#         font-weight: bold;
#         margin-bottom: 10px;
#     }
#     .subtitle {
#         color: #5253a1;
#         text-align: center;
#         font-size: 18px;
#         margin-bottom: 30px;
#     }
#     .text-area {
#         font-size: 16px;
#         border: 1px solid #cccccc;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     .predict-button {
#         background-color: #2d2e82;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-size: 18px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#     }
#     .predict-button:hover {
#         background-color: #4345b8;
#         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
#     }
#     .result {
#         color: #2d2e82;
#         text-align: center;
#         font-size: 24px;
#         font-weight: bold;
#         margin-top: 20px;
#     }
#     .footer {
#         text-align: center;
#         margin-top: 50px;
#         color: #888;
#         font-size: 14px;
#     }
#     .footer a {
#         color: #2d2e82;
#         text-decoration: none;
#     }
#     .footer a:hover {
#         text-decoration: underline;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Main container
# st.markdown('<div class="main-container">', unsafe_allow_html=True)

# st.markdown('<div class="title">SMS Spam Detection</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Predict if your SMS is Spam or Not Spam</div>', unsafe_allow_html=True)

# input_sms = st.text_area(
#     "Enter your SMS here:", key="sms_input", help="Type the SMS message you want to analyze.",
#     placeholder="e.g., Win a free iPhone by clicking this link!",
#     height=100
# )

# if st.button('Predict', key="predict_button", use_container_width=True):
#     # 1. preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. vectorize
#     vector_input = tk.transform([transformed_sms])
#     # 3. predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result == 1:
#         st.markdown('<div class="result">This SMS is classified as: <span style="color: #e63946;">Spam</span></div>', unsafe_allow_html=True)
#     else:
#         st.markdown('<div class="result">This SMS is classified as: <span style="color: #2a9d8f;">Not Spam</span></div>', unsafe_allow_html=True)

# st.markdown('<div class="footer">Made with ❤️ by <a href="https://github.com/Abhishek72-avail" target="_blank">Abhishek</a></div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# # End of Streamlit interface



# -------------------------------------------------------------------------------------------------------------------





# import nltk
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# import streamlit as st
# import pickle 
# import string
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# ps = PorterStemmer()


# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)

#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         y.append(ps.stem(i))

#     return " ".join(y)


# tk = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open("model.pkl", 'rb'))

# st.title("SMS Spam Detection Model")
# st.write("*Created by Abhishek*")
    

# input_sms = st.text_input("Enter the SMS")

# if st.button('Predict'):

#     # 1. preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. vectorize
#     vector_input = tk.transform([transformed_sms])
#     # 3. predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")


# ------------------------------------------------------------------------------------------------

# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# # Initialize the PorterStemmer
# ps = PorterStemmer()

# # Function to preprocess text
# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)

#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)

#     text = y[:]
#     y.clear()

#     for i in text:
#         y.append(ps.stem(i))

#     return " ".join(y)

# # Load the vectorizer and model
# tk = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open("model.pkl", 'rb'))

# # Streamlit interface
# st.set_page_config(page_title="SMS Spam Detection", page_icon="📱")

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #f0f2f6;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         max-width: 700px;
#         margin: auto;
#         font-family: 'Arial', sans-serif;
#     }
#     .title {
#         color: #2e3a87;
#         text-align: center;
#         font-size: 36px;
#         margin-bottom: 10px;
#     }
#     .subtitle {
#         color: #2e3a87;
#         text-align: center;
#         font-size: 18px;
#         margin-bottom: 30px;
#     }
#     .input {
#         color: #333;
#         font-size: 18px;
#     }
#     .button {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }
#     .result {
#         color: #2e3a87;
#         text-align: center;
#         font-size: 24px;
#         margin-top: 20px;
#     }
#     .footer {
#         text-align: center;
#         margin-top: 60px;
#         color: #888;
#     }
#     .footer a {
#         color: #2e3a87;
#         text-decoration: none;
#     }
#     .footer a:hover {
#         text-decoration: underline;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Main container
# with st.container():
#     st.markdown('<div class="main">', unsafe_allow_html=True)
    
#     st.markdown('<div class="title">SMS Spam Detection Model</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtitle">*Created by Abhishek*</div>', unsafe_allow_html=True)
    
#     input_sms = st.text_area("Enter the SMS", key="sms_input", help="Type the SMS message you want to check for spam.")
    
#     if st.button('Predict', key="predict_button"):
#         # 1. preprocess
#         transformed_sms = transform_text(input_sms)
#         # 2. vectorize
#         vector_input = tk.transform([transformed_sms])
#         # 3. predict
#         result = model.predict(vector_input)[0]
#         # 4. Display
#         if result == 1:
#             st.markdown('<div class="result">Spam</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="result">Not Spam</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="footer">Made with ❤️ by <a href="https://github.com/Abhishek72-avail">Abhishek</a></div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------------------------------------------

