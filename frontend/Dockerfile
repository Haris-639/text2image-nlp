# # Use Python 3.10 as the base image
# FROM python:3.10-slim

# # Set the working directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     python3-dev \
#     libjpeg-dev \
#     libpng-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first for better caching
# COPY frontend/requirements1.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements1.txt

# # Create the directory structure
# RUN mkdir -p /app/frontend /app/app/protos

# # Copy the frontend code
# COPY frontend/ /app/frontend/

# # Copy just the proto files to the protos directory
# COPY app/protos/text2image_pb2.py /app/app/protos/
# #COPY app/protos/text2image_pb2_grpc.py /app/app/protos/
# COPY app/protos/text2image_pb2_grpc.py /app/app/protos/

# # Expose the Streamlit port
# EXPOSE 8501 

# # Set environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     STREAMLIT_SERVER_PORT=8501 \
#     STREAMLIT_SERVER_HEADLESS=true \
#     STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# # Set the working directory to the frontend folder
# WORKDIR /app/frontend

# # Command to run the Streamlit application
# CMD ["streamlit", "run", "paste.txt", "--server.port=8501", "--server.address=0.0.0.0"]


FROM python:3.10.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the frontend code
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Command to run the application
CMD ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0"]