import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬")

st.title("🎬 Movie Info Extractor")
st.caption("Enter a movie name OR paste a paragraph describing a movie")

@st.cache_resource
def get_llm():
    return ChatMistralAI(model="mistral-small-latest")

llm = get_llm()

class MovieInfo(BaseModel):
    movie_name: str = Field(description="Name of the movie")
    release_year: int = Field(description="Year the movie was released")
    director: str = Field(description="Director of the movie")
    genre: str = Field(description="Genre of the movie")
    main_cast: List[str] = Field(description="Top 3 main actors in the movie")
    plot_summary: str = Field(description="Short 2-3 line plot summary")

plain_template = ChatPromptTemplate([
    ("system", "You are a movie information extraction assistant. The user will give you either a movie name or a paragraph describing a movie. You extract structured details about that movie. If any information is not known or not mentioned, clearly write 'Not mentioned' instead of guessing."),
    ("human", """Here is the input:

"{user_input}"

Extract the following information about the movie:
1. Movie Name
2. Release Year
3. Director
4. Genre
5. Main Cast (top 3, if known)
6. Short Plot Summary (2-3 lines)

Format the answer clearly with headings.""")
])

user_input = st.text_area(
    "Enter movie name or paragraph:",
    placeholder="e.g., Inception  —  OR  —  Inception is a 2010 science fiction film directed by Christopher Nolan...",
    height=150
)

want_json = st.toggle("Show as JSON format", value=False)

if st.button("🔍 Extract Info"):
    if user_input.strip() == "":
        st.warning("Please enter a movie name or paragraph first.")
    elif want_json:
        with st.spinner("Extracting structured data..."):
            structured_llm = llm.with_structured_output(MovieInfo)
            result = structured_llm.invoke(user_input)

        st.divider()
        st.subheader("📋 Extracted Structured Data")
        st.write(f"**Movie Name:** {result.movie_name}")
        st.write(f"**Release Year:** {result.release_year}")
        st.write(f"**Director:** {result.director}")
        st.write(f"**Genre:** {result.genre}")
        st.write(f"**Main Cast:** {', '.join(result.main_cast)}")
        st.write(f"**Plot Summary:** {result.plot_summary}")

        st.divider()
        st.subheader("🔧 Raw JSON")
        st.json(result.model_dump())
    else:
        with st.spinner("Extracting movie information..."):
            final_prompt = plain_template.invoke({"user_input": user_input})
            response = llm.invoke(final_prompt)

        st.divider()
        st.subheader("📋 Extracted Information")
        st.write(response.content)