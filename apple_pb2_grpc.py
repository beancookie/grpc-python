# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import apple_pb2 as apple__pb2


class FarmerStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetApple = channel.unary_unary(
                '/apple.Farmer/GetApple',
                request_serializer=apple__pb2.AppleRequest.SerializeToString,
                response_deserializer=apple__pb2.AppleReply.FromString,
                )


class FarmerServicer(object):
    """The greeting service definition.
    """

    def GetApple(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FarmerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetApple': grpc.unary_unary_rpc_method_handler(
                    servicer.GetApple,
                    request_deserializer=apple__pb2.AppleRequest.FromString,
                    response_serializer=apple__pb2.AppleReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'apple.Farmer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Farmer(object):
    """The greeting service definition.
    """

    @staticmethod
    def GetApple(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apple.Farmer/GetApple',
            apple__pb2.AppleRequest.SerializeToString,
            apple__pb2.AppleReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
