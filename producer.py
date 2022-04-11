import json
import os
from asyncio import sleep
import random
from aiokafka import AIOKafkaProducer
import asyncio

from dotenv import load_dotenv

load_dotenv()


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


events = ['once a week', 'once a day', 'once a month', 'once a year']

send_type = ['email', 'telegram', 'viber', 'what\'s app', 'odnoklassniki']


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9093', value_serializer=json_serializer)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        data = {
            'type_event': random.choice(events),
            'send_type': random.choice(send_type),
            'parameters': {
                'email': os.getenv('MY_EMAIL'),
                'CHAT_ID': os.getenv('CHAT_ID'),
                'text': f'This is test text message {random.randrange(1, 100)} '
            }
        }
        await producer.send_and_wait("test", data)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
    await sleep(5)


while True:
    asyncio.run(send_one())
