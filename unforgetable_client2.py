from __future__ import print_function
import logging

import grpc

import unforgetable_pb2
import unforgetable_pb2_grpc

def runService1():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = unforgetable_pb2_grpc.Service1Stub(channel)
        response = stub.function1(unforgetable_pb2.requestType1(field1=10))
        print("Service1 function1 return : {}".format(response.field1))
        response = stub.function2(unforgetable_pb2.requestType2(field1=0.10, field2=0.20))
        print("Service1 function2 return : {} {}".format(response.field1, response.field2))

def runService2():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = unforgetable_pb2_grpc.Service2Stub(channel)
        response = stub.function1(unforgetable_pb2.requestType1(field1=100))
        print("Service2 function1 return : {} {}".format(response.field1, response.field2))
        response = stub.function2(unforgetable_pb2.requestType2(field1=10.5, field2=20.6))
        print("Service2 function2 return : {}".format(response.field1))

if __name__ == '__main__':
    logging.basicConfig()
    runService1()
    runService2()