from .models import *
import os
import sqlite3
import logging as log


class FAASQLChartProvider:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def get_chart(self, icao) -> (FAAChart):
        """
        """
        sql = 'SELECT * FROM dtpp WHERE icao_ident == "{icao}"'.format(icao=icao)
        rows = self.exec_sql(sql)
        for row in rows:
            log.debug(row)

    def exec_sql(self, sql):
        log.debug(sql)
        return self.conn.execute(sql)

    def close(self):
        self.conn.commit()
        self.conn.close()
