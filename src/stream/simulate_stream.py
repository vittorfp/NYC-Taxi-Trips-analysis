import boto3
from multiprocess.pool import ThreadPool


AWS_REGION = "sa-east-1"
STREAM_NAME = "taxi-trips-stream"
max_bytes = 215000  # 215 kb | ~500 lines
total_sent = 0

client = boto3.client(
    'kinesis',
    region_name=AWS_REGION
)

files = [
    './data/raw/data-sample_data-nyctaxi-trips-2009-json_corrigido.json',
    './data/raw/data-sample_data-nyctaxi-trips-2010-json_corrigido.json',
    './data/raw/data-sample_data-nyctaxi-trips-2011-json_corrigido.json',
    './data/raw/data-sample_data-nyctaxi-trips-2012-json_corrigido.json'
]


def send_register(registers):
    global total_sent

    length = len(registers)
    total_sent += length
    records = [
        {
            'Data': data.encode(),
            'PartitionKey': '1'
        }
        for data in registers
    ]
    print(f"Total: {total_sent}/4MI")
    client.put_records(
        Records=records,
        StreamName=STREAM_NAME,
    )


def process_file(file):
    with open(file, 'r') as buffer:
        registers = buffer.readlines(max_bytes)
        while len(registers):
            send_register(registers)
            registers = buffer.readlines(max_bytes)


pool = ThreadPool(4)
pool.map(process_file, files)
