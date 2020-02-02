from .models import *
import os
import sqlite3
import logging as log


class FAASQLChartHandler:
    def __init__(self, db_file):
        if not os.path.exists(os.path.dirname(db_file)):
            os.makedirs(os.path.dirname(db_file))

        self.conn = sqlite3.connect(db_file)
        self.drop_tables()
        self.create_tables()
        self.chart_count = 0
        pass

    def drop_tables(self):
        self.conn.execute('DROP TABLE IF EXISTS dtpp')
        self.conn.execute('DROP TABLE IF EXISTS cycle')

    def create_tables(self):
        self.conn.execute(
            'CREATE TABLE dtpp (icao_ident text, chart_seq text, chart_name text, chart_code text, pdf_name text, '
            'state_code text, state_name text)')
        self.conn.execute(
            'CREATE TABLE cycle (cycle text, from_date text, to_date text)')

    def on_cycle_parsed(self, faa_cycle: FAACycle):
        sql = "INSERT INTO cycle VALUES ('{cycle}','{from_date}' ,'{to_date}')".format(
            cycle=faa_cycle.cycle,
            from_date=faa_cycle.from_date,
            to_date=faa_cycle.to_date)
        self.exec_sql(sql)

    def on_chart_parsed(self, faa_airport: FAAAirport, faa_state: FAAState, faa_chart: FAAChart):
        """
        Callback called for each chart found in the
        :param faa_state:
        :param faa_airport:
        :param faa_chart:
        """
        sql = "INSERT INTO dtpp VALUES ('{icao_ident}','{chart_seq}' ,'{chart_name}','{chart_code}','{pdf_name}', '{state_code}', '{state_name}')".format(
            icao_ident=faa_airport.icao_ident,
            chart_seq=faa_chart.chart_seq,
            chart_name=faa_chart.chart_name,
            chart_code=faa_chart.chart_code,
            pdf_name=faa_chart.pdf_name,
            state_code=faa_state.code,
            state_name=faa_state.name,
        )
        self.exec_sql(sql)
        self.chart_count += 1

        if self.chart_count % 10 == 0:
            self.conn.commit()
            pass

    def exec_sql(self, sql):
        log.debug(sql)
        self.conn.execute(sql)

    def close(self):
        self.conn.commit()
        self.conn.close()
