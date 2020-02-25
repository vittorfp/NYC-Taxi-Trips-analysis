from os import path
import logging
import click
import sqlite3


@click.command()
@click.argument('db_path')
def create_db(db_path):
    logger = logging.getLogger(__name__)

    if path.isfile(db_path):
        logger.info('The DB has been already created: {}'.format(db_path))
        return

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # vendor lookup
    c.execute(
        '''CREATE TABLE vendor_lookup
            (
                vendor_id text, 
                name text, 
                address text, 
                city text, 
                state text,
                zip integer,
                country text,
                contact text,
                current bool
            )'''
    )

    c.execute(
        '''CREATE TABLE trips
            (
                vendor_id text,
                pickup_datetime date,
                dropoff_datetime date,
                passenger_count integer,
                trip_distance float,
                pickup_longitude float,
                pickup_latitude float,
                rate_code integer,
                store_and_fwd_flag integer,
                dropoff_longitude float,
                dropoff_latitude float,
                payment_type text,
                fare_amount float,
                surcharge float,
                tip_amount float,
                tolls_amount float,
                total_amount float
        )'''
    )


    # payment lookup table
    c.execute(
        '''CREATE TABLE payment_lookup
            (
                payment_type text, 
                payment_lookup text
            )'''
    )

    conn.commit()
    conn.close()
    logger.info('Database created successfully: {}'.format(db_path))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    create_db()
