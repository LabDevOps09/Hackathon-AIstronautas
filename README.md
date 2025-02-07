# Hackathon-AIstronautas - Projeto em equipe the goat

![AI](https://github.com/user-attachments/assets/f87343c8-fd78-4e73-96cf-e436665da5e2)

# Day 1: Define the Core Features and Set Up the Environment:

Objective: Prepare the development environment and start with backend logic.

Pick Your First Agent: Space Researcher:

Start with the Space Researcher Agent for fetching space facts from NASA, ESA, SpaceX, etc.

## Set Up the Environment:

Install Python and create a virtual environment (venv).
Install necessary Python libraries like requests, json, pandas for handling data.

## API Exploration:

Register and get an API key for NASA’s API (or other space-related APIs).
Explore endpoints that give data on space missions, planets, Mars rover, or images.

## Basic Data Fetching:

Write a Python script that connects to the chosen APIs and fetches basic space data (like Mars data or current space missions).
For example, fetch the latest Mars rover data from NASA’s API.

# Day 2: Build the Space Researcher Agent:

Objective: Implement the Space Researcher Agent to fetch and store space facts.

## Data Fetching:

Create a Python function that fetches space facts using the APIs.
Example: Fetch Mars rover images, descriptions, and facts using the NASA API.

Store Data:

Store the fetched data in a structured format (like JSON, CSV, or a simple database like SQLite) for easy access later.

## Data Parsing:

Parse the fetched data to extract useful facts and convert it into readable text.

## Testing:

Test the agent by running the Python script and printing out the space facts.

# Day 3: Build the Storytelling Agent

Objective: Create the Storytelling Agent that generates sci-fi stories based on real space data.

## Basic Story Template:

Design a template where real space facts (like planet names, missions, or astronauts) can be inserted into a story format.

Example story template: “Astronaut [Name] discovered [Event] on [Planet] during a [Mission].”

## Space Facts Integration:

Link the Space Researcher Agent’s data to the Storytelling Agent.
Use the data to fill the gaps in your story template.

Generate Sci-Fi Story:

Develop a Python function to generate sci-fi stories by selecting random space facts (like planets, missions, or discoveries) and inserting them into the template.

## Testing:

Test the storytelling generation by running a few sample outputs and verifying they make sense.

# Day 4: Build the Simulation Generator Agent

Objective: Develop the Simulation Generator Agent to create mission blueprints.

## Mission Template Creation:

Create a simple structure for a mission blueprint, e.g., mission stages like "Launch", "Orbit", "Landing".
Define basic mission variables such as crew size, mission duration, and destination.

Data Integration:

Allow users to input parameters (e.g., crew size, destination, mission duration) to generate a personalized mission blueprint.

Generate Mission Blueprint:

Write a function that uses the input data to generate a mission blueprint in text format. For example, "The mission to Mars will take 9 months, with a crew of 3 astronauts."

Testing:

Test the simulation generator with various input combinations to ensure the output is accurate and logical.

# Day 5: Build the Visualization Agent

## Objective: Create the Visualization Agent to suggest space visuals.
Create a Database of Images/Models:

Collect publicly available space images or 3D models (e.g., from NASA or open-source libraries).
Store these assets in a simple structure, like a list of URLs pointing to the images or models.

## Visualization Logic:

Based on the current mission or story (generated by the Storytelling or Simulation Agent), suggest a relevant image or model.
For example, if the mission is about Mars, the agent should suggest an image of Mars or a rover.

Return Relevant Visuals:

Write Python functions that select and return relevant images based on the current context (mission or story).
Testing:

Test the visualization logic by generating missions and stories and verifying that the agent returns appropriate visuals.

# Day 6: Integrate All Agents and Polish the Backend Logic:

Objective: Combine all the agents and finalize the backend logic.
Integrate Agents:

Link the Space Researcher, Storytelling, Simulation Generator, and Visualization Agents so they work in a cohesive flow.
Example: Once the Storytelling Agent generates a sci-fi story, the Visualization Agent should suggest an image related to the story.

Backend Flow:

Set up a clear workflow where one agent’s output feeds into the next agent's input.
For example, the Space Researcher Agent provides data for the Storytelling Agent, which then sends output to the Simulation Generator, and finally, the Visualization Agent suggests related visuals.’

Final Testing:

Run through a complete use case (e.g., generate a space mission, create a story, and display visuals) and ensure everything works together smoothly.
Prepare for Presentation:

Prepare the backend to handle any API calls and processes that might be used in the frontend (since someone else is handling it).
Ensure your backend logic is well-documented and ready for integration.

