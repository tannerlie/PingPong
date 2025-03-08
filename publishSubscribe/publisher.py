import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = "Broadcast message to all!"
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(f" [x] Sent {message}")

connection.close()

