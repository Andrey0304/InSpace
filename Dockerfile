FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the local codebase to the container
COPY . /app

# Install any dependencies
RUN pip install -r requirements.txt --no-cachdir

# Define the command to run ETL script
CMD ["python", "-m", "etl"]
