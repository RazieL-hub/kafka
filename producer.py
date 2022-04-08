from aiokafka import AIOKafkaProducer
import asyncio


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9093')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("test", b"Super message")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


asyncio.run(send_one())


# async def send_one():
#     producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
#     # get cluster layout and initial topic/partition leadership information
#     await producer.start()
#     try:
#         # produce message
#         msg_id = f'{randint(1, 10000)}'
#         value = {'message_id': msg_id, 'text': 'some text', 'state': randint(1, 100)}
#         print(f'Sending message with value: {value}')
#         value_json = json.dumps(value).encode('utf-8')
#         await producer.send_and_wait(KAFKA_TOPIC, value_json)
#     finally:
#         # wait for all pending messages to be delivered or expire.
#         await producer.stop()