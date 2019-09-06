import bottle
import logging

import grpc

from . import helloworld_pb2
from . import helloworld_pb2_grpc


@bottle.route("/")
@bottle.route("/<name>")
def index(name="i.m.g.w"):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    return response.message


def serve():
    bottle.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    serve()
