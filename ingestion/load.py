"""Functions for loading the transformed data into a Data Warehouse"""
from .queries import BaseQueries


def create_databases(queries: BaseQueries):
    queries.create_raw_db()
    queries.create_dw_db()


def create_dimension_tables(queries: BaseQueries):
    queries.create_dim_host()
    queries.create_dim_ip()
    queries.create_dim_dhcp()
    queries.create_dim_kafka()
    queries.create_dim_raw_msg()


def insert_dimensions(queries: BaseQueries):
    queries.insert_dim_host()
    queries.insert_dim_ip()
    queries.insert_dim_dhcp()
    queries.insert_dim_kafka()
    queries.insert_dim_raw_msg()


def insert_rawdata(queries: BaseQueries):
    queries.insert_raw_data()

def create_fact_table(queries: BaseQueries):
    queries.create_fact_kafka_logs()

def insert_fact_table(queries: BaseQueries):
    queries.insert_fact_kafka_logs()