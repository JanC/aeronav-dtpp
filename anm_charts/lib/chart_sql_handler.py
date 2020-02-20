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
        self.conn.execute("""
        CREATE TABLE dtpp (
            icao_ident TEXT, apt_ident TEXT, apt_name TEXT, 
            chart_seq TEXT, chart_name TEXT, chart_code TEXT,
            pdf_name TEXT, state_code TEXT, state_name TEXT)""")

        self.conn.execute('CREATE TABLE cycle (cycle text, from_date text, to_date text)')

    def on_cycle_parsed(self, faa_cycle: FAACycle):
        sql = "INSERT INTO cycle(cycle, from_date, to_date) VALUES (?, ? , ?)"
        values = (faa_cycle.cycle,
                  faa_cycle.from_date,
                  faa_cycle.to_date)
        self.exec_sql(sql, values)

    def on_chart_parsed(self, faa_airport: FAAAirport, faa_state: FAAState, faa_chart: FAAChart):
        """
        Callback called for each chart found in the
        :param faa_state:
        :param faa_airport:
        :param faa_chart:
        """
        sql = """INSERT INTO dtpp(
            icao_ident, apt_ident, apt_name, chart_seq, chart_name,
            chart_code, pdf_name, state_code,
            state_name) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        values = (faa_airport.icao_ident,
                  faa_airport.apt_ident,
                  faa_airport.apt_name,
                  faa_chart.chart_seq,
                  faa_chart.chart_name,
                  faa_chart.chart_code,
                  faa_chart.pdf_name,
                  faa_state.code,
                  faa_state.name)

        self.exec_sql(sql, values)
        self.chart_count += 1

        if self.chart_count % 10 == 0:
            self.conn.commit()
            pass

    def exec_sql(self, sql, values):
        log.debug(sql)
        log.debug(values)
        self.conn.execute(sql, values)

    def close(self):
        self.conn.commit()
        self.conn.close()
