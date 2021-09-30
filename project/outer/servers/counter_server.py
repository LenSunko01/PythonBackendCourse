from concurrent import futures
import logging
import math
import time

import grpc
import counter_pb2
import counter_pb2_grpc


class CounterServicer(counter_pb2_grpc.CounterServicer):
    def Count(self, request, context):
        text = request.text
        word = request.word
        number_of_occurrences = text.count(word)
        return counter_pb2.NumberOfOccurrences(number=number_of_occurrences)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    counter_pb2_grpc.add_CounterServicer_to_server(
        CounterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()