import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai

load_dotenv()

st.title("AI Resume roaster")
st.divider()
st.badge("KAKS PVT LTD, COPYRIGHT 2025")
st.markdown("Upload your resume and get AI powered roasting")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
st.write("✅ API key loaded:", bool(GEMINI_API_KEY))

# import google.generativeai as genai, os
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# for m in genai.list_models():
#     st.write(m.name)


uploaded_file = st.file_uploader("Upload your resume here (PDF and txt only)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role that you are targeting")

analyze = st.button("Analyze resume")
print(analyze)

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_text(uploaded_file):
    """Extracts text from an uploaded pdf of text"""
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        with io.BytesIO(uploaded_file.read()) as file_bytes:
            return extract_text_from_pdf(file_bytes)
    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()

        prompt = f""" 

You are a brutally honest, no non-sense HR expert who's been reviewing resumes for decades
Roast this resume like you are on a comedy stage but still give some useful insights feedback.
Don't hold back - be sarcastic, witty and critical where needed.
Would would make this resume actually land a job in {job_role} for a good company.

here is the resume, go wild:
{file_content}

Make it sting and make sure to keep it in 150 words. Answer everything in Hinglish
 """

        # model = genai.GenerativeModel("gemini-1.5-flash")
        model = genai.GenerativeModel("models/gemini-flash-lite-latest")
        response = model.generate_content(prompt)
        st.markdown("## Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
