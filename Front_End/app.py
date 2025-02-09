import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

# Custom Styling
st.markdown(
    """
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #ff4b4b;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="main-title">🚀 Space Mission Assistant</p>', unsafe_allow_html=True)

class SpaceMissionAssistant:
    def __init__(self, nasa_api_key, llm_api_key):
        self.nasa_api_key = nasa_api_key
        self.llm_api_key = llm_api_key
        self.hf_model = "mistralai/Mistral-7B-Instruct-v0.3"

    def chat_with_ai(self, user_input):
        api_url = f"https://api-inference.huggingface.co/models/{self.hf_model}"
        headers = {"Authorization": f"Bearer {self.llm_api_key}"}
        payload = {"inputs": user_input}

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            return response.json()[0]['generated_text']
        except:
            return "⚠️ AI Response Failed. Please try again later."

    def generate_mission_report(self, destination, payload_weight):
        fuel_required = payload_weight * 50  
        mission_cost = payload_weight * 100  
        travel_time = np.random.randint(6, 24)  
        success_probability = np.random.uniform(70, 98)  
        weather_condition = np.random.choice(["Clear", "Stormy", "Windy", "Extreme Cold", "High Radiation"])

        return {
            "Destination": destination,
            "Payload Weight": f"{payload_weight} tons",
            "Estimated Fuel": f"{fuel_required} tons",
            "Mission Cost": f"${mission_cost}M",
            "Travel Time": f"{travel_time} months",
            "Weather": weather_condition,
            "Success Probability": f"{success_probability:.2f}%"
        }

# Initialize the assistant
nasa_api_key = "8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv"
llm_api_key = "************************************"
assistant = SpaceMissionAssistant(nasa_api_key, llm_api_key)

st.sidebar.markdown(
    """
    <style>
        .sidebar-icons {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding-bottom: 10px;
        }
        .sidebar-icons img {
            width: 60px;  /* Adjust size */
            margin-bottom: 10px; /* Space between icons */
        }
    </style>
    <div class="sidebar-icons">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712134.png" alt="AI Chat">
        <img src="https://cdn-icons-png.flaticon.com/512/2725/2725306.png" alt="Space Mission">
    </div>
    """,
    unsafe_allow_html=True
)

menu = st.sidebar.radio("📌 Select Option:", 
                       ["💬 Chat with AI", 
                        "🛰️ Plan a Space Mission",
                        "🛠️ Mission Analytics",
                        "🌍 Space News"])

if menu == "💬 Chat with AI":
    st.subheader("🤖 Space Chatbot")
    user_input = st.text_input("💬 Ask anything about space missions:")
    
    if st.button("🚀 Get AI Response"):
        if user_input:
            response = assistant.chat_with_ai(user_input)  # Assuming assistant is defined
            st.write("🤖 **AI Response:**")
            st.write(response)
        else:
            st.warning("⚠️ Please enter a question.")

elif menu == "🛰️ Plan a Space Mission":
    st.subheader("🌌 Plan Your Space Mission")
    destination = st.text_input("🌍 Enter mission destination:")
    payload_weight = st.number_input("📦 Enter payload weight (tons):", min_value=1.0, step=0.1)

    if st.button("🚀 Generate Mission Report"):
        if destination and payload_weight > 0:
            report = assistant.generate_mission_report(destination, payload_weight)  # Assuming assistant is defined
            for key, value in report.items():
                st.write(f"**{key}:** {value}")

            # Generate Graph Data
            x_payload = np.linspace(1, 100, 10)
            fuel_values = x_payload * 50
            cost_values = x_payload * 100
            probability_values = np.random.uniform(70, 98, 10)
            travel_time_values = np.random.randint(6, 24, 10)

            # Store data in session state
            st.session_state["graph_data"] = {
                "x_payload": x_payload,
                "fuel_values": fuel_values,
                "cost_values": cost_values,
                "probability_values": probability_values,
                "travel_time_values": travel_time_values
            }
        else:
            st.warning("⚠️ Please enter valid details.")

    # Graph Display Logic
    if "graph_data" in st.session_state:
        graph_data = st.session_state["graph_data"]

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📈 Payload vs. Fuel Requirement"):
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(graph_data["x_payload"], graph_data["fuel_values"], marker="o", linestyle="-", color="blue")
                ax.set_title("Payload vs. Fuel Requirement", fontsize=14, fontweight="bold")
                ax.set_xlabel("Payload (tons)")
                ax.set_ylabel("Fuel (tons)")
                ax.grid(True)
                st.pyplot(fig)

            if st.button("🎯 Payload vs. Success Probability"):
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(graph_data["x_payload"], graph_data["probability_values"], marker="^", linestyle="-", color="green")
                ax.set_title("Payload vs. Success Probability", fontsize=14, fontweight="bold")
                ax.set_xlabel("Payload (tons)")
                ax.set_ylabel("Success Probability (%)")
                ax.grid(True)
                st.pyplot(fig)

        with col2:
            if st.button("💰 Payload vs. Mission Cost"):
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(graph_data["x_payload"], graph_data["cost_values"], marker="s", linestyle="-", color="red")
                ax.set_title("Payload vs. Mission Cost", fontsize=14, fontweight="bold")
                ax.set_xlabel("Payload (tons)")
                ax.set_ylabel("Cost ($M)")
                ax.grid(True)
                st.pyplot(fig)

            if st.button("⏳ Payload vs. Travel Time"):
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(graph_data["x_payload"], graph_data["travel_time_values"], marker="D", linestyle="-", color="purple")
                ax.set_title("Payload vs. Travel Time", fontsize=14, fontweight="bold")
                ax.set_xlabel("Payload (tons)")
                ax.set_ylabel("Travel Time (months)")
                ax.grid(True)
                st.pyplot(fig)

elif menu == "🛠️ Mission Analytics":
    st.subheader("🔧 Mission Analytics")
    
    # Assuming we are analyzing payload-to-cost relationship or other mission data
    st.write("🔍 This section provides in-depth analytics for your space missions.")
    
    # Sample data for analysis
    payload_data = np.linspace(1, 100, 10)
    fuel_data = payload_data * 50
    mission_cost_data = payload_data * 100
    success_rate_data = np.random.uniform(70, 100, 10)

    # Analytics: Plot payload vs mission cost
    st.write("📊 **Payload vs Mission Cost**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(payload_data, mission_cost_data, marker='o', linestyle='-', color='red')
    ax.set_title("Payload vs Mission Cost", fontsize=14, fontweight="bold")
    ax.set_xlabel("Payload (tons)")
    ax.set_ylabel("Mission Cost ($M)")
    ax.grid(True)
    st.pyplot(fig)

    # Success Rate vs Payload Analysis
    st.write("📈 **Payload vs Success Rate**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(payload_data, success_rate_data, marker='^', linestyle='-', color='green')
    ax.set_title("Payload vs Success Rate", fontsize=14, fontweight="bold")
    ax.set_xlabel("Payload (tons)")
    ax.set_ylabel("Success Rate (%)")
    ax.grid(True)
    st.pyplot(fig)
    
   # Function to fetch space news
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_space_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "space exploration",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": "39ba6a7cc657450dbeeb36e8b82a8bd3"  # Replace with a valid API key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

# Display space news
st.subheader("📰 Latest Space News")
articles = get_space_news()

if articles:
    for article in articles[:5]:  # Show top 5 articles
        st.write(f"**[{article['title']}]({article['url']})**")
        st.write(f"📅 {article['publishedAt']}")
        st.write(f"📰 {article['source']['name']}")
        st.write("---")
else:
    st.warning("⚠️ Unable to fetch space news at the moment. Try again later.")
