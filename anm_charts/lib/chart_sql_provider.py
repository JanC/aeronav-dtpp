from .models import *
import os
import sqlite3
import logging as log


class FAASQLChartProvider:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def get_chart(self, icao) -> (FAAAirport, [FAAChart]):
        """
        """
        sql = 'SELECT icao_ident, apt_ident, apt_name, chart_name, pdf_name, chart_code, chart_seq FROM dtpp WHERE icao_ident == "{icao}"'.format(icao=icao)
        rows = self.exec_sql(sql)
        results = []
        airport = None
        for row in rows:
            airport = FAAAirport(sql_row=row[0:3])
            chart = FAAChart(sql_row=row[3:])
            results.append(chart)
        return airport, results

    def get_cycle(self):
        sql = 'SELECT cycle from cycle'
        row = self.exec_sql(sql).fetchone()
        return row[0]



    def exec_sql(self, sql):
        log.debug(sql)
        return self.conn.execute(sql)

    def close(self):
        self.conn.commit()
        self.conn.close()
