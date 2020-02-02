import xml.etree.ElementTree as ET
from typing import Callable
from .models import *


class FAAHandler:

    def __init__(self,
                 on_cycle_parsed: Callable[[FAACycle], None],
                 on_chart_parsed: Callable[[FAAAirport, FAAState, FAAChart], None],
                 ):
        self.airport = None
        self.state = None
        self.on_cycle_parsed = on_cycle_parsed
        self.on_chart_parsed = on_chart_parsed

    def faa_cycle_handler(self, digital_tpp_attributes):
        """
        :param digital_tpp_attributes: {'cycle': '2002', 'from_edate': '0901Z  01/30/20', 'to_edate': '0901Z  02/27/20'}
        """
        self.on_cycle_parsed(FAACycle(digital_tpp_attributes))

    def faa_state_code_handler(self, state_code_attributes):
        self.state = FAAState(state_code_attributes)

    def faa_airport_handler(self, airport_name_attributes):
        """
            {'ID': 'AFTON MUNI', 'military': 'N', 'apt_ident': 'AFO', 'icao_ident': 'KAFO', 'alnum': '9116'}
        """
        # print(airport_name_attributes)
        self.airport = FAAAirport(airport_name_attributes)

    def faa_airport_record_handler(self, record):
        """
           {'chartseq': '10100', 'chart_code': 'MIN', 'chart_name': 'TAKEOFF MINIMUMS', 'useraction': None, 'pdf_name': 'SW3TO.PDF', 'cn_flg': 'N', 'cnsection': None, 'cnpage': None, 'bvsection': 'L', 'bvpage': None, 'procuid': None, 'two_colored': 'N', 'civil': None, 'faanfd18': None, 'copter': None, 'amdtnum': None, 'amdtdate': None} 
        """
        self.on_chart_parsed(self.airport, self.state, FAAChart(record))
