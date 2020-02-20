class FAACycle:
    def __init__(self, faa_digital_tpp):
        """

        :param faa_digital_tpp:
        """
        self.cycle = faa_digital_tpp["cycle"]
        self.from_date = faa_digital_tpp["from_edate"]
        self.to_date = faa_digital_tpp["to_edate"]


class FAAChart:
    def __init__(self, faa_record):
        """
           {'chartseq': '10100', 'chart_code': 'MIN', 'chart_name': 'TAKEOFF MINIMUMS', 'useraction': None, 'pdf_name': 'SW3TO.PDF', 'cn_flg': 'N', 'cnsection': None, 'cnpage': None, 'bvsection': 'L', 'bvpage': None, 'procuid': None, 'two_colored': 'N', 'civil': None, 'faanfd18': None, 'copter': None, 'amdtnum': None, 'amdtdate': None} 
        """
        self.pdf_name = faa_record["pdf_name"]
        self.chart_code = faa_record["chart_code"]
        self.chart_name = faa_record["chart_name"]
        self.chart_seq = faa_record["chartseq"]


class FAAState:
    def __init__(self, faa_record):
        """

        """
        self.code = faa_record["ID"]
        self.name = faa_record["state_fullname"]


class FAAAirport:

    def __init__(self, faa_record):
        """
            {'ID': 'AFTON MUNI', 'military': 'N', 'apt_ident': 'AFO', 'icao_ident': 'KAFO', 'alnum': '9116'}
        """
        self.apt_name = faa_record["ID"]
        self.apt_ident = faa_record["apt_ident"]
        self.icao_ident = faa_record["icao_ident"]
