from app.PoloniexWrapper import *
import pika
import settings

# DECLARE QUEUE PROCESS
connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBIT_HOST))
channel = connection.channel()
channel.queue_declare(queue=settings.QUEUE)

# DECLARE PROCESS
wrapper = PoloniexWrapper()


def main_context():

    ticker = wrapper.get_ticker()

    channel.basic_publish(exchange='',
                          routing_key=settings.QUEUE,
                          body=str(ticker),
                          properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          ))
