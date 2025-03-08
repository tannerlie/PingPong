import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print(f" [x] Consumer 1 received {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(" [x] Waiting for messages")
channel.start_consuming()

