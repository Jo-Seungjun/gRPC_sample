from concurrent import futures
import logging

import grpc

import unforgetable_pb2
import unforgetable_pb2_grpc

class Service1(unforgetable_pb2_grpc.Service1Servicer):
    def function1(self, request, context):
        field1 = request.field1
        return unforgetable_pb2.returnType1(field1=field1)

    def function2(self, request, context):
        field1 = request.field1
        field2 = request.field2
        return unforgetable_pb2.returnType2(field1=field2, field2=field1)

class Service2(unforgetable_pb2_grpc.Service2Servicer):
    def function1(self, request, context):
        field1 = request.field1
        return unforgetable_pb2.returnType2(field1=field1, field2=field1)
    
    def function2(self, request, context):
        field1 = request.field1
        field2 = request.field2
        return unforgetable_pb2.returnType1(field1=int(field1+field2))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    unforgetable_pb2_grpc.add_Service1Servicer_to_server(Service1(), server)
    unforgetable_pb2_grpc.add_Service2Servicer_to_server(Service2(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
