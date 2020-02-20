
# FAA D-TPP Parser


An easy tool to download and parse the FAA D-TPP xml into a sqlite database

#### References
- [FAA D-TPP](https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/)


## Installation


To install the package system wide (as root):

```
pip3 install git+https://github.com/JanC/aeronav-dtpp
```

For recent `pip` versions, it is possible (and for development, recommended) to
install it to the user's home directory. By default, the binaries are in
`~/.local/bin`, which should be added to the `PATH`.

```
pip3 install --user git+https://github.com/JanC/aeronav-dtpp
```

## Usage


```
anm-dtpp
Usage: anm-dtpp [OPTIONS] COMMAND [ARGS]...

  CLI to download and process the DTPP from FAA. The script reads the latest
  FAA cycle xml and generates a sqlite DB with the PDF chart names. Hello

Options:
  --help  Show this message and exit.

Commands:
  download  Downloads the FAA d-TPP xml.
  parse     Reads the FAA d-TPP xml and creates a sql database from it.
  
```

## Examples



```bash
anm-dtpp download
INFO: Downloading https://nfdc.faa.gov/webContent/dtpp/current.xml
INFO: Writing xml to ./output/current.xml
INFO: Done
```

```bash
anm-dtpp parse
INFO: Reading output/current.xml
INFO: Parsed 23930 charts in ./output/dtpp.sqlite
```

## Samples

A sample .xml and .sqlite are located in the [samples](samples) folder. Those contain only the charts from the KSBP airport.

## Development 

This section is meant for development tips

Running from command line

```
python3 -m anm_charts.__main__ catalogue
python3 -m anm_charts.__main__ create-db
```