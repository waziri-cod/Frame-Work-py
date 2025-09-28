# Part 4: Streamlit Application

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# Title
st.title("CORD-19 Metadata Explorer")
st.markdown("Explore publications related to COVID-19 from the CORD-19 dataset.")

# Show sample of data
st.subheader("Sample Data")
st.dataframe(df.sample(5))

# Publications by Year
st.subheader("Publications by Year")
year_counts = df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_n = st.slider("Select number of top journals", 5, 20, 10)
top_journals = df['journal'].value_counts().head(top_n)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
ax.set_title("Top Journals Publishing COVID-19 Research")
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
titles_text = " ".join(df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)
fig, ax = plt.subplots(figsize=(12,6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Sources
st.subheader("Top Sources")
source_counts = df['source_x'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, ax=ax)
ax.set_title("Top Sources of Papers")
st.pyplot(fig)
