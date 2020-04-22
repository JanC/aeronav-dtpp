import requests
import logging as log
import os
from anm_charts.lib.chart_sql_provider import FAASQLChartProvider


def get_dtpp_catalogue(out_file, url="https://nfdc.faa.gov/webContent/dtpp/current.xml"):
    log.info("Downloading {}".format(url))
    r = requests.get(url)
    if r.status_code > 299 or r.status_code < 200:
        log.error("Invalid response code: {}".format(r.status_code))
        return

    create_dir(os.path.dirname(out_file))
    f = open(out_file, "w+")

    log.info("Writing xml to {}".format(out_file))
    f.write(r.text)
    f.close()
    log.info("Done")


def get_gtpp_charts(icao: str, provider: FAASQLChartProvider, out_folder):
    cycle = provider.get_cycle()
    airport, charts = provider.get_chart(icao)

    log.info("Getting charts for {airport}".format(airport=airport.apt_name))

    chart_root_dir = os.path.join(out_folder, airport.icao_ident)
    create_dir(chart_root_dir)

    for chart in charts:
        chart_dir = os.path.join(chart_root_dir, chart.chart_code)
        chart_url = "http://aeronav.faa.gov/d-tpp/{cycle}/{pdf_name}".format(cycle=cycle, pdf_name=chart.pdf_name)
        log.info("{chart_code}: {chart_name}".format(chart_code=chart.chart_code, chart_name=chart.chart_name))
        download_file(chart_url, chart_dir, chart.pdf_name)


def download_file(url, out_dir, out_file):
    create_dir(out_dir)
    r = requests.get(url)
    if r.status_code > 299 or r.status_code < 200:
        log.error("Invalid response code: {} GET {}".format(r.status_code, url))
        return
    out_path = os.path.join(out_dir, out_file)
    f = open(out_path, "wb")
    log.debug("Writing  to {}".format(out_path))
    f.write(r.content)
    f.close()


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
