import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='task_queue', body=message)

print(f" [x] Sent {message}")

connection.close()

