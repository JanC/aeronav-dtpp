import requests
import logging as log


def get_dtpp(out_file, url="https://nfdc.faa.gov/webContent/dtpp/current.xml"):
    log.info("Downloading {}".format(url))
    r = requests.get(url)
    if r.status_code > 299 or r.status_code < 200:
        log.error("Invalid response code: {}".format(r.status_code))
        return

    f = open(out_file, "w+")
    log.info("Writing xml to {}".format(out_file))
    f.write(r.text)
    f.close()
    log.info("Done")
