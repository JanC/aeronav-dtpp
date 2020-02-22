class FAACycle:
    def __init__(self, faa_digital_tpp):
        """

        :param faa_digital_tpp:
        """
        self.cycle = faa_digital_tpp["cycle"]
        self.from_date = faa_digital_tpp["from_edate"]
        self.to_date = faa_digital_tpp["to_edate"]


class FAAChart:
    def __init__(self, faa_record=None, sql_row=None):
        """
           {'chartseq': '10100', 'chart_code': 'MIN', 'chart_name': 'TAKEOFF MINIMUMS', 'useraction': None, 'pdf_name': 'SW3TO.PDF', 'cn_flg': 'N', 'cnsection': None, 'cnpage': None, 'bvsection': 'L', 'bvpage': None, 'procuid': None, 'two_colored': 'N', 'civil': None, 'faanfd18': None, 'copter': None, 'amdtnum': None, 'amdtdate': None} 
        """
        if faa_record is not None:
            self.pdf_name = faa_record["pdf_name"]
            self.chart_code = faa_record["chart_code"]
            self.chart_name = faa_record["chart_name"]
            self.chart_seq = faa_record["chartseq"]

        if sql_row is not None:
            (self.chart_name, self.pdf_name, self.chart_code, self.chart_seq) = sql_row

class FAAState:
    def __init__(self, faa_record):
        """

        """
        self.code = faa_record["ID"]
        self.name = faa_record["state_fullname"]


class FAAAirport:

    def __init__(self, faa_record=None, sql_row=None):
        """
            {'ID': 'AFTON MUNI', 'military': 'N', 'apt_ident': 'AFO', 'icao_ident': 'KAFO', 'alnum': '9116'}
        """
        if faa_record is not None:
            self.apt_name = faa_record["ID"]
            self.apt_ident = faa_record["apt_ident"]
            self.icao_ident = faa_record["icao_ident"]
        if sql_row is not None:
            (self.icao_ident, self.apt_ident, self.apt_name) = sql_row
