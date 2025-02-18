


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit Page Config
st.set_page_config(page_title="Resume Insights App", layout="wide")

# Load Dataset
@st.cache_data
def load_data():
    # Ensure the CSV file is in your project folder
    df = pd.read_csv("Resume_Mortage.csv")
    return df

# Main App
def main():
    st.title("📄 Resume Insights Application")
    st.sidebar.header("⚙️ Settings")
    
    # Load Data
    df = load_data()
    
    # Display Raw Data
    if st.sidebar.checkbox("Show Raw Data", False):
        st.write(df.head(10))  # Display first 10 rows
    
    # Handle Missing Data
    st.subheader("🔍 Data Cleaning")
    missing_values = df.isnull().sum()
    st.write("Missing values in each column:")
    st.write(missing_values)

    # Insights Section
    st.subheader("📊 Key Insights")

    # Insight 1: Top 10 Most Common Job Roles
    st.markdown("### 1️⃣ Top 10 Most Common Job Roles")
    top_roles = df['Job Role'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_roles.index, y=top_roles.values, palette="viridis", ax=ax)
    plt.xticks(rotation=45)
    plt.xlabel("Job Role")
    plt.ylabel("Count")
    plt.title("Top 10 Job Roles")
    st.pyplot(fig)

    # Insight 2: Experience Distribution
    st.markdown("### 2️⃣ Years of Experience Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['Years of Experience'], bins=20, kde=True, color="blue", ax=ax)
    plt.xlabel("Years of Experience")
    plt.ylabel("Count")
    plt.title("Distribution of Experience")
    st.pyplot(fig)

    # Insight 3: Skills Word Cloud
    st.markdown("### 3️⃣ Word Cloud of Most Common Skills")
    from wordcloud import WordCloud
    skill_text = " ".join(df['Skills'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(skill_text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    # Insight 4: Education Level Distribution
    st.markdown("### 4️⃣ Education Level Distribution")
    education_counts = df['Education Level'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=education_counts.index, y=education_counts.values, palette="magma", ax=ax)
    plt.xlabel("Education Level")
    plt.ylabel("Count")
    plt.title("Distribution of Education Levels")
    st.pyplot(fig)

    # Footer
    st.markdown("---")
    st.markdown("📌 *Built with Streamlit & Pandas*")

# Run the App
if __name__ == "__main__":
    main()
