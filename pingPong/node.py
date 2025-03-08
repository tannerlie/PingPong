import pika
import sys
import config

# Get node ID from command line argument
NODE_ID = int(sys.argv[1])  # Pass 1 or 2 when running the script
OTHER_NODE_ID = 2 if NODE_ID == 1 else 1

# Set queue names
MY_QUEUE = config.QUEUE_1 if NODE_ID == 1 else config.QUEUE_2
OTHER_QUEUE = config.QUEUE_2 if NODE_ID == 1 else config.QUEUE_1

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST))
channel = connection.channel()

# Declare queues
channel.queue_declare(queue=MY_QUEUE)
channel.queue_declare(queue=OTHER_QUEUE)

# Flag to track if the node has started
started = False

def send_message(message):
    print(f"Sending {message} to Node {OTHER_NODE_ID}")
    channel.basic_publish(exchange='', routing_key=OTHER_QUEUE, body=message)

def on_message_received(ch, method, properties, body):
    global started
    message = body.decode()

    if message == 'PUSH' and not started:
        print("PUSH button pressed, sending PING")
        send_message('PING')

    elif message == 'PING':
        print(f"Received PING from Node {OTHER_NODE_ID}, sending PONG")
        send_message('PONG')

    elif message == 'PONG':
        print(f"Received PONG from Node {OTHER_NODE_ID}, sending PING")
        send_message('PING')

    started = True

# Start consuming messages
channel.basic_consume(queue=MY_QUEUE, on_message_callback=on_message_received, auto_ack=True)

print(f"Node {NODE_ID} is waiting for messages...")
channel.start_consuming()