from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV | Anurag Jha"
PAGE_ICON = "random"
NAME = "Anurag Jha"
DESCRIPTION = """
ALL TIME LEARNER, 12TH GRADUATE, PYTHONISTAS, PROGRAMMER, FUTURE BILLIONAIRE.
"""
EMAIL = "anuragpradeepjha@outlook.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/anurag-jha-023584222/",
    "GitHub": "https://github.com/coderthroughout",
    "Instagram": "https://www.instagram.com/apj4356/"
}

PROJECTS = {

}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF AND PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---HERO SECTION---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINK---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years experience of coding.
- ✔️ Strong hands on experience and knowledge in Python and MySQL
- ✔️ Good understanding of Machine Learning from Scikit-Learn it's Models 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Make Multiple Projects.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, datetime, keras(basic), pytorch(learning)), SQL, 
- 📊 Data Visualisation: Matplotlib
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases:MySQL
"""
)


#--- PROJECT'S----


# --- PROJECT_1
st.write("🚧", "**AIRLINES MANAGEMENT SYSTEM**")

st.write(
    """
- ► Used Python, Flask, Pandas, Pickle, seaborn, Scikit-learn and MySQL to make the Project.
- ► Led a team of 3 to complete the project. Done the Backend of the Project.
- ► Has a feature of Data Management as well as prediction of Flight Prices from the data of Airlines Flight price data.
"""
)

#--- Projects links---

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")