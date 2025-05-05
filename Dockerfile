# # Use NVIDIA CUDA 11.6 base image with cuDNN
# FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04

# # Set working directory
# WORKDIR /app

# # Environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     DEBIAN_FRONTEND=noninteractive

# # Install Python 3.10 and system dependencies
# # RUN apt-get update && apt-get install -y --no-install-recommends \
# #     software-properties-common \
# #     git \
# #     curl \
# #     wget \
# #     build-essential \
# #     python3.10 \
# #     python3.10-dev \
# #     python3-pip \
# #     && rm -rf /var/lib/apt/lists/*
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     git \
#     curl \
#     wget \
#     build-essential \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update && apt-get install -y --no-install-recommends \
#     python3.10 \
#     python3.10-dev \
#     python3-pip \
#     && rm -rf /var/lib/apt/lists/*


# # Make python3.10 the default
# RUN ln -sf /usr/bin/python3.10 /usr/bin/python && ln -sf /usr/bin/pip3 /usr/bin/pip

# # Upgrade pip
# RUN pip install --no-cache-dir --upgrade pip

# # Install specific Torch + CUDA 11.6 packages
# # RUN pip install --no-cache-dir \
# #     torch==1.12.0+cu116 \
# #     torchvision==0.13.0+cu116 \
# #     torchaudio==0.12.1+cu116 \
# #     --extra-index-url https://download.pytorch.org/whl/cu116
# # RUN pip install --no-cache-dir \
# #     torch==1.12.0+cu116 \
# #     torchvision==0.13.0+cu116 \
# #     torchaudio==0.12.1 \
# #     -f https://download.pytorch.org/whl/torch_stable.html
# RUN pip install --no-cache-dir \
#     torch==1.12.1+cu116 \
#     torchvision==0.13.1+cu116 \
#     torchaudio==0.12.1 \
#     -f https://download.pytorch.org/whl/torch_stable.html



# # Copy requirements first (for caching)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Additional dependencies
# RUN pip install --no-cache-dir \
#     grpcio \
#     grpcio-tools \
#     protobuf \
#     diffusers \
#     transformers

# # Copy project files
# COPY . .

# # Create required folders
# RUN mkdir -p /app/models /app/generated_images

# # Default server run command
# CMD ["python", "-m", "app.server"]

# # Expose gRPC port
# EXPOSE 50051

# Use NVIDIA CUDA 11.6 base image with cuDNN
# FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04

# # Set working directory
# WORKDIR /app

# # Environment variables
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     DEBIAN_FRONTEND=noninteractive

# # Install Python 3.10 and system dependencies in a single layer
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     git \
#     curl \
#     wget \
#     build-essential \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update && apt-get install -y --no-install-recommends \
#     python3.10 \
#     python3.10-dev \
#     python3-pip \
#     && ln -sf /usr/bin/python3.10 /usr/bin/python \
#     && ln -sf /usr/bin/pip3 /usr/bin/pip \
#     && pip install --no-cache-dir --upgrade pip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Create a .dockerignore file to exclude unnecessary files
# # Copy requirements first and install all Python packages in one layer
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt \
#     torch==1.12.1+cu116 \
#     torchvision==0.13.1+cu116 \
#     torchaudio==0.12.1 \
#     -f https://download.pytorch.org/whl/torch_stable.html \
#     grpcio \
#     grpcio-tools \
#     protobuf \
#     diffusers \
#     transformers

# # Create required folders
# RUN mkdir -p /app/models /app/generated_images

# # Copy only necessary project files
# # Consider using .dockerignore to exclude models, images, etc.
# COPY app/ ./app/

# # Expose gRPC port
# EXPOSE 50051

# # Default server run command
# CMD ["python", "-m", "app.server"]

# ---------- Stage 1: Builder ----------
    # FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04 as builder

    # # Set environment variables
    # ENV PYTHONUNBUFFERED=1 \
    #     PYTHONDONTWRITEBYTECODE=1 \
    #     DEBIAN_FRONTEND=noninteractive
    
    # # Install Python 3.10 and dependencies
    # RUN apt-get update && apt-get install -y --no-install-recommends \
    #     software-properties-common \
    #     git \
    #     curl \
    #     wget \
    #     build-essential \
    #     && add-apt-repository ppa:deadsnakes/ppa \
    #     && apt-get update && apt-get install -y --no-install-recommends \
    #     python3.10 \
    #     python3.10-dev \
    #     python3-pip \
    #     && ln -sf /usr/bin/python3.10 /usr/bin/python \
    #     && ln -sf /usr/bin/pip3 /usr/bin/pip \
    #     && pip install --no-cache-dir --upgrade pip \
    #     && apt-get clean \
    #     && rm -rf /var/lib/apt/lists/*
    
    # # Set workdir
    # WORKDIR /app
    
    # # Copy and install Python dependencies
    # # COPY requirements.txt .
    # # RUN pip install --no-cache-dir -r requirements.txt \
    # #     torch==1.12.1  \
    # #     torchvision==0.13.1\
    # #     torchaudio==0.12.1 \
    # #     -f https://download.pytorch.org/whl/torch_stable.html \
    # #     grpcio \
    # #     grpcio-tools \
    # #     protobuf \
    # #     diffusers \
    # #     transformers

    # # Download and install PyTorch + CUDA 11.6 compatible wheels for Python 3.10
    # # RUN wget https://download.pytorch.org/whl/cu116/torch-1.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl -O torch.whl && \
    # # wget https://download.pytorch.org/whl/cu116/torchvision-0.13.1%2Bcu116-cp310-cp310-linux_x86_64.whl -O torchvision.whl && \
    # # wget https://download.pytorch.org/whl/cu116/torchaudio-0.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl -O torchaudio.whl && \
    # # pip install torch.whl torchvision.whl torchaudio.whl && \
    # # rm torch.whl torchvision.whl torchaudio.whl
    # RUN wget https://download.pytorch.org/whl/cu116/torch-1.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl  \
    # && wget https://download.pytorch.org/whl/cu116/torchvision-0.13.1%2Bcu116-cp310-cp310-linux_x86_64.whl  \
    # && wget https://download.pytorch.org/whl/cu116/torchaudio-0.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl  \
    # && pip install torch-1.12.1+cu116-cp310-cp310-linux_x86_64.whl torchvision-0.13.1+cu116-cp310-cp310-linux_x86_64.whl torchaudio-0.12.1+cu116-cp310-cp310-linux_x86_64.whl  \
    # && rm *.whl


    # # Copy requirements and install remaining packages
    # COPY requirements.txt .
    # RUN pip install --no-cache-dir -r requirements.txt \
    # grpcio \
    # grpcio-tools \
    # protobuf \
    # diffusers \
    # transformers
    
    # # ---------- Stage 2: Runtime ----------
    # FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04
    
    # # Set environment variables again in final image
    # ENV PYTHONUNBUFFERED=1 \
    #     PYTHONDONTWRITEBYTECODE=1 \
    #     DEBIAN_FRONTEND=noninteractive
    
    # # Install Python runtime only
    # RUN apt-get update && apt-get install -y --no-install-recommends \
    #     python3.10 \
    #     python3-pip \
    #     && ln -sf /usr/bin/python3.10 /usr/bin/python \
    #     && ln -sf /usr/bin/pip3 /usr/bin/pip \
    #     && apt-get clean \
    #     && rm -rf /var/lib/apt/lists/*
    
    # # Set workdir
    # WORKDIR /app
    
    # # Copy installed Python packages from builder stage
    # COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
    # COPY --from=builder /usr/local/bin /usr/local/bin
    
    # # Copy your code and required directories
    # COPY app/ ./app/
    # COPY models/ ./models/
    # COPY model_cache/ ./model_cache/
    # # COPY generated_images/ ./generated_images/
    
    # # Expose gRPC port
    # EXPOSE 50051
    
    # # Default run command
    # CMD ["python", "-m", "app.server"]
    
    # ---------- Stage 1: Builder ----------
FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04 as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Install Python 3.10 and development tools
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     git \
#     curl \
#     wget \
#     build-essential \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update && apt-get install -y --no-install-recommends \
#     python3.10 \
#     python3.10-dev \
#     python3.10-distutils \
#     python3-pip \
#     && python3.10 -m ensurepip --upgrade \
#     && ln -sf /usr/bin/python3.10 /usr/bin/python \
#     && ln -sf /usr/bin/pip3 /usr/bin/pip \
#     && python --version && pip --version \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    git \
    curl \
    wget \
    build-essential \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-dev \
    python3.10-distutils \
    && curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3.10 get-pip.py \
    && ln -sf /usr/bin/python3.10 /usr/bin/python \
    && ln -sf /usr/local/bin/pip /usr/bin/pip \
    && python --version && pip --version \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* get-pip.py


# Set workdir
WORKDIR /app

# Download and install PyTorch + CUDA 11.6 compatible wheels for Python 3.10
RUN wget https://download.pytorch.org/whl/cu116/torch-1.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl \
 && wget https://download.pytorch.org/whl/cu116/torchvision-0.13.1%2Bcu116-cp310-cp310-linux_x86_64.whl \
 && wget https://download.pytorch.org/whl/cu116/torchaudio-0.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl \
 && python3.10 -m pip install torch-1.12.1+cu116-cp310-cp310-linux_x86_64.whl \
                              torchvision-0.13.1+cu116-cp310-cp310-linux_x86_64.whl \
                              torchaudio-0.12.1+cu116-cp310-cp310-linux_x86_64.whl \
 && rm *.whl

# Copy requirements and install remaining packages
COPY requirements.txt .
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt \
    grpcio \
    grpcio-tools \
    protobuf \
    diffusers \
    transformers

# ---------- Stage 2: Runtime ----------
FROM nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04

# Set environment variables again in final image
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Install Python runtime
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     python3.10 \
#     python3.10-distutils \
#     python3-pip \
#     && python3.10 -m ensurepip --upgrade \
#     && ln -sf /usr/bin/python3.10 /usr/bin/python \
#     && ln -sf /usr/bin/pip3 /usr/bin/pip \
#     && python --version && pip --version \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
# Add deadsnakes PPA to get Python 3.10 and required modules
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-distutils \
    python3.10-venv \
    curl \
    wget \
    git \
    build-essential \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 \
    && ln -sf /usr/bin/python3.10 /usr/bin/python \
    && ln -sf /usr/local/bin/pip /usr/bin/pip \
    && python --version && pip --version \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Set workdir
WORKDIR /app
ENV PYTHONPATH=/app

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application files
COPY app/ ./app/
COPY models/ ./models/
COPY model_cache/ ./model_cache/
# COPY generated_images/ ./generated_images/  # Uncomment if needed

# Expose gRPC port
EXPOSE 50051

# Default run command
CMD ["python","-m", "app.server","--server.port=8501", "--server.address=0.0.0.0"]
