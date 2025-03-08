import pika
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

callback_queue = channel.queue_declare(queue='', exclusive=True).method.queue
correlation_id = str(uuid.uuid4())

channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      properties=pika.BasicProperties(
                          reply_to=callback_queue,
                          correlation_id=correlation_id),
                      body="Hello, process this!")

def on_response(ch, method, properties, body):
    if properties.correlation_id == correlation_id:
        print(f" [.] Got response: {body.decode()}")

channel.basic_consume(queue=callback_queue, on_message_callback=on_response, auto_ack=True)

print(" [x] Waiting for response")
channel.start_consuming()

