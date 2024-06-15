# app.py

import streamlit as st
from data_handling import load_projects_dataset

# Load dataset
dataset_path = 'ceqr-projects.csv'
df = load_projects_dataset(dataset_path)


# Function to retrieve projects based on query
def retrieve_projects(query):
    # Filter dataset based on query in project name or project description
    filtered_data = df[(df['Project Name'].str.contains(query, case=False)) |
                       (df['Project Description'].str.contains(query, case=False))]

    # Extract relevant information
    projects = filtered_data[['CEQR', 'Project Name', 'Project Description', 'Borough', 'Lead Agency', 'URL']].to_dict(
        'records')

    return projects


# Title of the app
st.title("Project Search and Details Application")

# Sidebar for user input
query = st.text_input("Enter your query:", "Kingsbridge")

# Main logic to handle user input and display results
if st.button("Search"):
    # Retrieve projects based on user query
    retrieved_projects = retrieve_projects(query)

    # Display retrieved projects
    st.subheader("Retrieved Projects:")
    for project in retrieved_projects:
        st.write(f"**Project Name:** {project['Project Name']}")
        st.write(f"**Project Description:** {project['Project Description']}")
        st.write(f"**Borough:** {project['Borough']}")
        st.write(f"**Lead Agency:** {project['Lead Agency']}")
        st.write(f"**URL:** {project['URL']}")
        st.write("---")
