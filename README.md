# PingPong
# RabbitMQ Messaging System

## 1. Introduction
This document provides a step-by-step guide on how to set up, run, and manage a RabbitMQ-based messaging system implemented in Python. The program supports three communication models:
- **Direct Communication (Client-Server RPC)**
- **Message-Oriented Middleware (MOM) using Queues**
- **Publish-Subscribe Model**

---

## 2. Running the RabbitMQ Program

### 2.1 Direct Communication (Client-Server RPC)
1. **Start the Server:**
```bash
python3 rpc_server.py
```
2. **Run the Client:**
```bash
python3 rpc_client.py
```
The client sends a request, and the server processes it and returns a response.

### 2.2 Two Entities Communicating Through a Queue (MOM)
1. **Start the Consumer (Receiver):**
```bash
python3 consumer.py
```
2. **Send Messages Using the Producer:**
```bash
python3 producer.py
```
The producer sends messages to a queue, and the consumer retrieves them asynchronously.

### 2.3 Publish-Subscribe Model
1. **Start Multiple Consumers:**
```bash
python3 consumer.py
```
Run this in **2 separate instances**.

2. **Run the Publisher:**
```bash
python3 publisher.py
```
The publisher sends messages to an exchange, and all bound consumers receive the message.

---

## 3. Running the Ping-Pong Program

### 3.1 Start Two Instances of the Node Script
Open **two separate terminals** and run the following commands:

- **For Node 1:**
```bash
python node.py 1
```
- **For Node 2:**
```bash
python node.py 2
```

### 3.2 Simulate Pressing the PUSH Button
- **For Node 1:**
```bash
python send_push.py 1
```
- **For Node 2:**
```bash
python send_push.py 2
```

The nodes will start exchanging **PING** and **PONG** messages automatically.

---

## 4. Additional Information
Ensure RabbitMQ is running locally before starting the scripts:
```bash
brew services start rabbitmq
```
To stop the RabbitMQ service:
```bash
brew services stop rabbitmq
```

