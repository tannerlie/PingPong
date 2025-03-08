import pika
import sys
import config

# Get node ID from command line argument
NODE_ID = int(sys.argv[1])  # Pass 1 or 2 when running the script
MY_QUEUE = config.QUEUE_1 if NODE_ID == 1 else config.QUEUE_2

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
channel = connection.channel()

# Send PUSH to the node
channel.basic_publish(exchange='', routing_key=MY_QUEUE, body='PUSH')
print(f"Sent PUSH to Node {NODE_ID}")

connection.close()