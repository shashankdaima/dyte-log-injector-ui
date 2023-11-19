import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Shashank's Log Ingestor! 👋")

# st.sidebar.success("Select a demo above.")
image_path = "./images/home_page.png"

# Display the image
st.image(image_path, caption="Your Image Caption", use_column_width=True)

st.markdown(
    f"""
    ## Overview

Welcome to the Log Ingestor project! This project is designed to efficiently handle the ingestion of logs and provide scalable solutions for processing and analyzing log data.

## Table of Contents

- [Data Flow for Individual Logs](#data-flow-for-individual-logs)
- [Ideal System Design](#ideal-system-design)
- [System Design for Hiring Assignment](#system-design-for-hiring-assignment)
- [Getting Started](#getting-started)
- [Contrainst to this assignment](#contrainst-to-this-assignment)

"""
)
import streamlit as st

def data_flow_section():
    st.header("Data Flow for Individual Logs")
    st.markdown(
        """
        Describe the data flow for individual logs. 
        Explain how logs are ingested, processed, and stored in the system. 
        Include any relevant components and their interactions.
        """
    )

   # st.sidebar.success("Select a demo above.")
    image_path = "./images/basic_data_flow.png"

    # Display the image
    st.image(image_path, caption="This shows how individual log data goes into different component.", use_column_width=True)

def ideal_system_design_section():
    st.header("Ideal System Design")
    st.markdown(
        """
        Provide an ideal system design that outlines the architecture for a scalable log processing system. 
        Discuss key components, data storage, and strategies for handling increased load and scalability challenges.
        """
    )
    # st.sidebar.success("Select a demo above.")
    image_path = "./images/proposal.png"

    # Display the image
    st.image(image_path, caption="This shows the actually system deign that needs to be build.", use_column_width=True)

    

def hiring_assignment_section():
    st.header("System Design for Hiring Assignment")
    st.markdown(
        """
        Detail the specific system design implemented for the hiring assignment. 
        Discuss any modifications or optimizations made based on the requirements of the assignment.
        """
    )
    # st.sidebar.success("Select a demo above.")
    image_path = "./images/actual_flow.png"

    # Display the image
    st.image(image_path, caption="This shows the actually system deign that needs to be build.", use_column_width=True)

    

def getting_started_section():
    st.header("Getting Started")
    st.markdown(
        """
        Instructions on how to get started with the Log Ingestor project. 
        Include any prerequisites, installation steps, and dependencies.
        """
    )

def usage_section():
    st.header("Contrainst to this assignment")
    st.markdown(
        """
        1. Lack of time, this assignment feels like a week of work.
        2. Constraints of using free resources like rabbitmq shared queue blocks some traffic and supabase will pause the db if it not being used for over a week something. 
        3. I messed very very much :(, i started with rust apis, because I thought it would be more efficient on runtime. Plus, I could not able to do use rabbitmq for 7-8 hours. It was a exploration of redis, rabbitmq, streamlit(frontend is built with streamlit). Resulting in only online mode.
        """
    )

# Main Streamlit app
def main():
    # Add sections
    data_flow_section()
    ideal_system_design_section()
    hiring_assignment_section()
    getting_started_section()
    usage_section()

if __name__ == "__main__":
    main()

