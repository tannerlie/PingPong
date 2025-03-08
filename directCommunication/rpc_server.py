import pika

def on_request(ch, method, properties, body):
    response = f"Processed: {body.decode()}"
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=properties.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

