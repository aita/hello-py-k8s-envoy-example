import concurrent.futures
import logging
import time
import grpc

from . import helloworld_pb2
from . import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name.title())


def serve():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
        server = grpc.server(executer)
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        server.add_insecure_port("[::]:50051")
        server.start()

        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
