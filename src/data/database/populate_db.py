import json
import logging
import click
import sqlite3
import pandas as pd


def populate_trip_table(cursor):
    logger = logging.getLogger(__name__)
    files = [
        'data/raw/data-sample_data-nyctaxi-trips-2009-json_corrigido.json',
        'data/raw/data-sample_data-nyctaxi-trips-2010-json_corrigido.json',
        'data/raw/data-sample_data-nyctaxi-trips-2011-json_corrigido.json',
        'data/raw/data-sample_data-nyctaxi-trips-2012-json_corrigido.json'
    ]

    for file in files:
        logger.info('Reading file: {}.'.format(file))
        buffer = open(file, 'r')
        lines = buffer.readlines()
        for line in lines:
            data = json.loads(line.split('\n')[0])
            entry = [
                (
                    data['vendor_id'],
                    data['pickup_datetime'],
                    data['dropoff_datetime'],
                    data['passenger_count'],
                    data['trip_distance'],
                    data['pickup_longitude'],
                    data['pickup_latitude'],
                    data['rate_code'],
                    data['store_and_fwd_flag'],
                    data['dropoff_longitude'],
                    data['dropoff_latitude'],
                    data['payment_type'],
                    data['fare_amount'],
                    data['surcharge'],
                    data['tip_amount'],
                    data['tolls_amount'],
                    data['total_amount']
                )
            ]
            cursor.executemany("INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", entry)


def populate_vendor_table(cursor):
    df = pd.read_csv('data/raw/data-vendor_lookup-csv.csv')
    df.columns = ['vendor_id', 'name', 'address', 'city', 'state', 'zip', 'country', 'contact', 'current']

    entries = [
        (
            row.vendor_id,
            row['name'],
            row.address,
            row.city,
            row.state,
            row.zip,
            row.country,
            row.contact,
            row.current == 'Yes'
        )
        for _, row in df.iterrows()
    ]
    cursor.executemany('''INSERT INTO vendor_lookup VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', entries)


def populate_payment_table(cursor):
    df = pd.read_csv('data/raw/data-payment_lookup-csv.csv', skiprows=1)
    entries = [
        (row.payment_type, row.payment_lookup)
        for _, row in df.iterrows()
    ]
    cursor.executemany('''INSERT INTO payment_lookup VALUES (?, ?)''', entries)


@click.command()
@click.argument('db_path')
def populate_db(db_path):
    logger = logging.getLogger(__name__)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    logger.info('Populating vendor table.')
    populate_vendor_table(c)

    logger.info('Populating payment table.')
    populate_payment_table(c)

    logger.info('Populating trip table.')
    populate_trip_table(c)

    conn.commit()
    conn.close()
    logger.info('Databases populated successfully: {}'.format(db_path))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    populate_db()
