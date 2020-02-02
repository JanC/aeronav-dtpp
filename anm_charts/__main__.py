#!/usr/bin/env python3

import click
import logging as log

from anm_charts.lib.handler import FAAChart, FAAHandler
from anm_charts.lib.chart_sql_handler import FAASQLChartHandler
from anm_charts.lib.dtpp_downloader import get_dtpp
from anm_charts.lib.parser import read_xml


@click.group()
def cli():
    """
    CLI to download and process the DTPP from FAA. The script reads the latest FAA cycle xml and generates a sqlite DB with the PDF chart names.
    """
    pass


@cli.command()
@click.option("--in", "-i", "in_file",
              default="output/current.xml",
              required=True,
              help="Path to xml file to be processed (Downloaded via the download command).",
              type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option("--out-file", "-o",
              default="./output/dtpp.sqlite",
              help="Path to file to store resulting databse.",
              type=click.Path(dir_okay=False))
@click.option('-v', '--verbose', is_flag=True, default=False)
def parse(in_file, out_file, verbose):
    """
    Reads the FAA d-TPP xml and creates a sql database from it.
    """
    configure_log(verbose)

    chart_handler = FAASQLChartHandler(out_file)

    handler = FAAHandler(chart_handler.on_cycle_parsed, chart_handler.on_chart_parsed)

    read_xml(in_file,
             handler.faa_cycle_handler,
             handler.faa_state_code_handler,
             handler.faa_airport_handler,
             handler.faa_airport_record_handler)

    chart_handler.close()
    log.info("Parsed %d charts in %s" % (chart_handler.chart_count, out_file))


@cli.command()
@click.option("--out-file", "-o",
              default="./output/current.xml",
              help="Path to the xml file to store the downloaded file.",
              type=click.Path(dir_okay=False))
@click.option('-v', '--verbose', is_flag=True, default=False)
def download(out_file, verbose):
    """
    Downloads the FAA d-TPP xml.
    """
    configure_log(verbose)
    get_dtpp(out_file)


def configure_log(verbose):
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG if verbose else log.INFO)


if __name__ == "__main__":
    cli()
