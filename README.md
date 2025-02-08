# Hackathon-AIstronautas - Projeto em equipe the goat

![AI](https://github.com/user-attachments/assets/f87343c8-fd78-4e73-96cf-e436665da5e2)

# Space Storytelling and Simulation Project

## Overview

This project is designed to create a cohesive system that integrates multiple agents to fetch space data, generate sci-fi stories, create mission blueprints, and suggest relevant visuals. The system is built using Python and leverages various APIs to fetch real-time space data.

## Project Structure

The project is divided into several key components, each handled by a specific agent:

1. **Space Researcher Agent**: Fetches space-related data from APIs like NASA, ESA, and SpaceX.
2. **Storytelling Agent**: Generates sci-fi stories based on real space data.
3. **Simulation Generator Agent**: Creates mission blueprints based on user inputs.
4. **Visualization Agent**: Suggests relevant space visuals based on the generated stories or missions.

# Space Researcher Project

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### On Windows:
```bash
venv\Scripts\activate
```

### On macOS/Linux:
```bash
source venv/bin/activate
```

## Install Required Packages

```bash
pip install requests json pandas
```

## API Keys

Register for an API key from NASA's API.

Store your API key in a `.env` file:

```bash
NASA_API_KEY=your_api_key_here
```

## Usage

### Space Researcher Agent

#### Fetch Space Data:

Run the script to fetch data from NASA's API:

```bash
python space_researcher.py
```

This script will fetch data such as Mars rover images, descriptions, and facts.

#### Store Data:

The fetched data is stored in a structured format (JSON/CSV/SQLite) for easy access.

### Storytelling Agent

#### Generate Sci-Fi Stories:

Run the script to generate a sci-fi story based on the fetched space data:

```bash
python storytelling_agent.py
```

The story will be printed to the console.

### Simulation Generator Agent

#### Create Mission Blueprints:

Run the script to generate a mission blueprint based on user inputs:

```bash
python simulation_generator.py
```

The blueprint will be printed to the console.

### Visualization Agent

#### Suggest Visuals:

Run the script to suggest relevant visuals based on the generated story or mission:

```bash
python visualization_agent.py
```

The suggested visuals (image URLs) will be printed to the console.

## Integration

To integrate all agents into a cohesive system:

### Run the Main Script:

```bash
python main.py
```

This script will sequentially run the Space Researcher, Storytelling, Simulation Generator, and Visualization Agents.

### Backend Flow:

The output of one agent feeds into the input of the next agent, creating a seamless workflow.

