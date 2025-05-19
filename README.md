# Text-to-Image AI Agent

A microservice-based text-to-image generation system using Stable Diffusion 1.4, implementing a gRPC API with concurrent request handling.

## Project Overview

This project implements a text-to-image AI agent as a microservice. It uses Stable Diffusion 1.4 to generate images from text prompts. The system is containerized using Docker and exposes a gRPC API for interaction. It also includes a simple Gradio frontend for demonstration purposes.

### Key Features

- **gRPC API** for text-to-image generation
- **Concurrency support** using Python's asyncio
- **Error handling** for invalid inputs and server errors
- **JSON responses** with appropriate status codes
- **Comprehensive test suite**
- **Containerized deployment** with Docker
- **Streamlit+HTML+CSS frontend** for easy demonstration

## Technical Requirements

- Python 3.10.11
- PyTorch 1.12
- CUDA 11.6
- Docker and Docker Compose

## Project Structure

```
text2image-agent/
├── app/
│   ├
│   │  
│   │            
│   ├── proto/
│   │   ├── text2image.proto   # gRPC protocol definition
│   │   └── text2image_pb2_grpc.py
│   │   └── text2image_pb2.py
│   ├── text2image.py    # Stable Diffusion model handling
│   └── utils.py        # Utility functions
│   └── server.py       # gRPC server
│              
├── tests/
│   ├── concurrency.py
│   └── test_service.py
├── frontend/
│   ├── front.py
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── client.py
└── README.md
```

## API Endpoints

The service implements two gRPC endpoints:

1. **GenerateImage** - Generates an image from a text prompt
   - Parameters:
     - `prompt` (string): Text prompt for image generation
     - `height` (int, optional): Image height (default: 512)
     - `width` (int, optional): Image width (default: 512)
     - `guidance_scale` (float, optional): How closely to follow the prompt (default: 7.5)
     - `num_inference_steps` (int, optional): Number of denoising steps (default: 50)
     - `negative_prompt` (string, optional): Things to avoid in the image
     - `seed` (int, optional): Random seed for reproducibility (-1 for random)

2. **GetStatus** - Get the status of the service
   - Returns information about the service's status, model version, and resource usage

## Installation and Setup

### Building with Docker Compose

```bash
# Clone the repository
git clone <repository-url>
cd text2image-agent

# Build and start the services
docker-compose up --build
```

### Manual Setup

```bash
# Clone the repository
git clone <repository-url>
cd text2image-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate gRPC code
python -m grpc_tools.protoc -I./app/proto --python_out=./app/proto/generated --grpc_python_out=./app/proto/generated ./app/proto/text2image.proto
touch ./app/proto/generated/__init__.py

# Run the server
python -m app.service.server
```

## Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run all tests
pytest

# Run specific test file
pytest tests/test_model.py
pytest tests/test_service.py
```

### Manual Testing with the Client Script

```bash
# Check service status
python client.py status

# Generate an image
python client.py generate "a beautiful landscape with mountains" --output landscape.png

# Generate with custom parameters
python client.py generate "a cyberpunk city at night" --width 640 --height 384 --steps 30 --guidance-scale 8.5 --output cyberpunk.png --save-metadata
```

### Testing with Postman

1. Install the Postman gRPC plugin
2. Import the proto file
3. Create a new request:
   - Server URL: `localhost:50051`
   - Service: `text2image.Text2ImageService`
   - Method: `GenerateImage` or `GetStatus`
   - Fill in the request message fields
   - Send the request

## Frontend

The frontend is available at `http://localhost:8501/` when the services are running. It provides a user-friendly interface for interacting with the text-to-image service.

## Performance Considerations

- The service uses asyncio for concurrent request handling
- Image generation is computationally intensive and requires a GPU for reasonable performance
- The model is loaded into memory once and reused for all requests
- Large images or high step counts will increase generation time
