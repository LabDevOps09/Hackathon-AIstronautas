import streamlit as st
import requests
import os

def get_nasa_apod():
    """
    Fetches the Astronomy Picture of the Day (APOD) from NASA's API.
    """
    nasa_api_key = os.getenv("NASA_API_KEY")  # Secure API key retrieval
    if not nasa_api_key:
        return {"error": "⚠️ Error: NASA API key not configured."}
    
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error fetching NASA APOD: {response.status_code}"}

def get_space_news():
    """
    Retrieves the latest space-related news articles.
    """
    url = "https://api.spaceflightnewsapi.net/v3/articles"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"⚠️ Error fetching space news: {response.status_code}")
        return []

def query_ai_model(user_input):
    """
    Queries an AI model to answer user questions about space.
    """
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}  # Secure API key retrieval
    
    payload = {
        "inputs": f"Provide an objective, science-based response: {user_input}",
        "parameters": {"temperature": 0.2}  # Low temperature to reduce hallucinations
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "⚠️ Unexpected AI response. Please try again later."
    except Exception as e:
        return f"⚠️ AI error: {str(e)}"

def main():
    """
    Streamlit application main function.
    """
    st.title("Space Exploration 🚀")
    
    # NASA APOD Section
    st.header("NASA's Astronomy Picture of the Day")
    apod_data = get_nasa_apod()
    if "error" in apod_data:
        st.error(apod_data["error"])
    else:
        st.image(apod_data.get("url", ""), caption=apod_data.get("title", "Image of the Day"))
        st.write(apod_data.get("explanation", "No description available."))
    
    # Space News Section
    st.header("Latest Space News")
    news = get_space_news()
    for article in news[:5]:  # Display only the top 5 articles
        st.subheader(article["title"])
        st.write(article["summary"])
        st.write(f"[Read more]({article['url']})")
    
    # AI Space Q&A Section
    st.header("Ask AI About Space")
    user_question = st.text_input("Enter your question about the universe:")
    if user_question:
        answer = query_ai_model(user_question)
        st.write(answer)
    
if __name__ == "__main__":
    main()


