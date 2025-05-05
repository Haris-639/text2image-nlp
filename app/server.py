# app/server.py

import grpc
from concurrent import futures
import asyncio
import base64
from app.protos import text2image_pb2 as pb2
from app.protos import text2image_pb2_grpc as pb2_grpc
from app.text2image import generate_image_from_text  


class Text2ImageService(pb2_grpc.Text2ImageServiceServicer):
    async def GenerateImage(self, request, context):
        try:
            text = request.text
            ctx = request.context

            # Generate image bytes asynchronously
            image_bytes = await generate_image_from_text(text, ctx)

            if image_bytes is None:
                return pb2.ImageResponse(
                    status=500,
                    message="Image generation failed.",
                    image_base64=""
                )

            # Encode image bytes to base64
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')

            return pb2.ImageResponse(
                status=200,
                message="Image generated successfully.",
                image_base64=image_base64
            )
        except Exception as e:
            return pb2.ImageResponse(
                status=500,
                message=f"Server Error: {str(e)}",
                image_base64=""
            )


async def serve():
    server = grpc.aio.server()
    pb2_grpc.add_Text2ImageServiceServicer_to_server(Text2ImageService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("✅ gRPC Server is running on port 50051...")
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
