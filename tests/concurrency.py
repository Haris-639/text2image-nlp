import asyncio
import grpc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.protos import text2image_pb2 as pb2
from app.protos import text2image_pb2_grpc as pb2_grpc

# async def send_request(stub, text, context):
#     request = pb2.ImageRequest(text=text, context=context)
#     response = await stub.GenerateImage(request)
#     print(f"[{text}] Status: {response.status} - {response.message}")

# async def main():
#     async with grpc.aio.insecure_channel('localhost:50051') as channel:
#         stub = pb2_grpc.Text2ImageServiceStub(channel)
#         tasks = [
#             send_request(stub, f"Prompt {i}", f"Context {i}") for i in range(5)
#         ]
#         await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())

# import grpc
# import asyncio
# from app.protos import text2image_pb2 as pb2
# from app.protos import text2image_pb2_grpc as pb2_grpc

# Define the asynchronous client to test concurrency
async def generate_image(client, text, context):
    request = pb2.ImageRequest(text=text, context=context)
    try:
        response = await client.GenerateImage(request)
        if response.status == 200:
            print(f"Image generated successfully: {response.image_base64[:50]}...")  # Print first 50 chars of base64
        else:
            print(f"Error: {response.message}")
    except Exception as e:
        print(f"Request failed: {e}")

async def run_concurrent_requests():
    # Establish the gRPC channel
    channel = grpc.aio.insecure_channel('localhost:50051')  # Assuming server is running locally
    client = pb2_grpc.Text2ImageServiceStub(channel)

    # Create the tasks for concurrent requests with the example inputs
    tasks = []
    inputs = [
        ("A beautiful sunset over the ocean.", "Landscape painting."),
        ("A futuristic city.", "flying cars."),
        ("A cute puppy playing in the grass.", "Realistic photography."),
        ("An astronaut floating in space", "Sci-fi."),
        ("A serene mountain landscape.", "Vibrant autumn colors.")
    ]
    
    for text, context in inputs:
        tasks.append(generate_image(client, text, context))

    # Await all tasks to complete
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run_concurrent_requests())
