import xml.etree.ElementTree as ET
import logging as log

def read_xml_state_code(xml_state_code_node, faa_airport_handler, faa_record_handler):
    for city_name_node in xml_state_code_node:
        for airport_name_node in city_name_node:
            faa_airport_handler(airport_name_node.attrib)
            for record_node in airport_name_node:
                d = dict()
                for test in record_node:
                    d[test.tag] = test.text
                faa_record_handler(d)


def read_xml(
        in_file,
        faa_cycle_handler,
        faa_state_code_handler,
        faa_airport_handler,
        faa_record_handler
):
    log.info("Reading " + in_file)
    tree = ET.parse(in_file)
    root = tree.getroot()

    ffa_cycle = root.attrib
    faa_cycle_handler(ffa_cycle)

    for xml_state_code_node in root:
        faa_state_code_handler(xml_state_code_node.attrib)
        read_xml_state_code(xml_state_code_node, faa_airport_handler, faa_record_handler)
