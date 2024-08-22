[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://queryhunt-game.streamlit.app/)

# 🕵️‍♂️ QueryHunt - SQL Murder Mystery Game

**QueryHunt** is an interactive SQL game that combines the excitement of a murder mystery with the power of AI. Inspired by the original SQL Murder Mystery, this project challenges players to solve a unique case by running SQL queries against AI-generated data. Built as a hackathon project for TiDB, QueryHunt showcases the capabilities of TiDB Serverless, GPT-4, and other modern technologies.

## Architecture

<img src="https://i.postimg.cc/G34Zdz22/Architecture.png"/>

## Features

- **Engaging Gameplay:** Players use SQL queries to explore data and identify the murderer in a dynamically generated story.
- **AI-Powered Hints:** An AI assistant provides hints based on previous queries to guide players toward the correct solution.
- **Cutting-Edge Tech Stack:** The game leverages TiDB Serverless, GPT-4, and open-source libraries to deliver a smooth and modern experience.
- **Scalable and Unique:** Each game session is unique, with new stories and data generated every time, ensuring a fresh challenge for every player.

## Tech Stack

- **TiDB Serverless:** Stores AI-generated temporary game data, including tables for Victim, Suspects, Evidence, Alibis, and more.
- **TiDB VectorSearch:** Ensures the AI generates valid SQL queries by referencing schema embeddings stored in the vs_game_schema table.
- **Llama-Index:** Manages the workflow for generating and validating game data, including self-healing processes.
- **Streamlit:** Provides the user interface, including a custom SQL editor for running queries.

## How It Works

1. **Story Generation:** The AI generates a unique murder mystery story and populates the database with relevant data.
2. **Data Exploration:** Players explore the data by running SQL queries to piece together the clues and identify the murderer.
3. **Hints System:** The AI can offer hints based on the player’s query history, helping them narrow down the suspects.
4. **Victory:** The game ends when the player correctly identifies the murderer.

## Getting Started

To set up and run QueryHunt locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/QueryHunt.git
   cd QueryHunt

