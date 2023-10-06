# ETL Pipeline and Dockerization Project

This project involves designing and implementing an ETL (Extract, Transform, Load) pipeline to handle various data-related operations. The pipeline includes importing CSV data into a MySQL database, calculating aggregate data and storing it in a PostgreSQL database, Dockerizing the ETL application, and using Docker Compose to deploy both MySQL and PostgreSQL databases and run the ETL code within containers. Additionally, we will discuss optional components like Grafana for monitoring.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [ETL Pipeline](#etl-pipeline)
- [Dockerization](#dockerization)
- [Grafana Integration (Optional)](#grafana-integration-optional)
- [Challenges and Solutions](#challenges-and-solutions)
- [Alternative Approaches](#alternative-approaches)
- [Conclusion](#conclusion)

## Project Overview

The main objectives of this project are:
1. Import CSV data into a MySQL database.
2. Calculate aggregate data and store it in a PostgreSQL database, including weekly average activity and total activity for each email domain, while filtering out invalid sessions.
3. Containerize the ETL application using Docker.
4. Use Docker Compose to deploy MySQL and PostgreSQL databases and run the ETL code within containers.


## Project Structure

Here's a structured overview of the project directory with descriptions for each file and directory:

- **InSpace**
    - `requirements.txt`: Contains a list of Python packages required for project.
    - `README.md`: Documentation file for project.
    - `InSpace_ Data Engineer Task.pdf`: A PDF document with the data engineer task instructions.
    - `Dockerfile`: Configuration file for building a Docker image for application.
    - `docker-compose.yml`: Configuration for Docker Compose, defining services and containers.
    - `docker_cleanup.sh`: A shell script for cleaning up Docker containers and resources.
    - `DataDescription.md`: Documentation describing the data used in the project.
    - `.gitignore`: A file specifying which files and directories to ignore when using Git.
    - `.env`: Environment file for storing configuration variables.

    - **data**: Directory for storing data files.
        - `user.csv`: CSV file containing user data.
        - `space_session_info.csv`: CSV file containing space session information.
        - `space_attendee.csv`: CSV file containing attendee data.

    - **configs**: Directory for configuration files.
        - **grafana**: Directory for Grafana-related configurations.

    - **app**: Directory containing application's source code.
        - `queries.py`: Python module for defining database queries.
        - `main.py`: Main application file.
        - `connections.py`: Python module for managing database connections.
        - `configs.py`: Configuration file for application.
        - `__init__.py`: Python package initialization file.


## Getting Started
To get started with this project, follow these steps:

Clone the project repository.
```bash
git clone <repository_url>
cd InSpace
```
Set up the necessary dependencies by following the instructions in the etl_pipeline/README.md file.
ETL Pipeline
The ETL pipeline consists of Python code located in the etl_pipeline directory. You can find detailed information on how to run the ETL pipeline in the etl_pipeline/README.md file.

Dockerization
The Dockerization of the ETL application is achieved through the Dockerfile. To build and run the Docker container, follow these steps:

bash
Copy code
# Build the Docker image
docker build -t etl-app .

# Run the Docker container
docker run etl-app


## Grafana Integration (Optional)
To add Grafana to the Docker Compose setup for monitoring purposes, you can create a Grafana service and configure dashboards. Detailed instructions can be found in the grafana/README.md file.

## Challenges and Solutions
During the implementation of this project, some challenges may arise. It's essential to document these challenges and the solutions applied to overcome them.

Example Challenges:

Data Integrity: Ensuring the data is accurate and complete during the ETL process.
Docker Networking: Configuring the network connections between Docker containers.
Example Solutions:

Data Validation: Implement data validation and cleansing steps in the ETL pipeline.
Docker Network: Use Docker Compose to define custom networks for better container communication.
Alternative Approaches
In this section, you can discuss alternative approaches that were considered but not pursued, along with reasons for your choices. For instance, you might consider using a different programming language for the ETL pipeline or alternative containerization tools.

## Conclusion
This project successfully implements an ETL pipeline for data processing, Dockerizes the application, and uses Docker Compose to deploy databases and run the ETL code within containers. Optional components like Grafana integration can be added for monitoring purposes. Challenges and solutions, as well as alternative approaches, have been discussed to provide insights into the project's design and implementation decisions.
