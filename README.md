# Sandbox for Open Data Cube with Digital Twins Environment

Based on [Digital Twins](https://github.com/GeospatialResearch/Digital-Twins) and [DEA Sandbox](https://github.com/GeoscienceAustralia/dea-sandbox).

## Setup

1. git clone to the local host.

1. open the terminal, and go to the repository directory.

1. fill the `.env` file referring to the `.env.example`.

1. open `docker-compose.yml` and replace path `../datastorage` in `- "../datastorage:/home/jovyan/datastorage"` to real datastorage path.

1. execute `docker-compose build`.

1. execute `docker-compose up`.

1. copy the Jupyter link and open it on a web browser.

## Remaining problems

1. running the BG_FLood model in the container.

1. the postgres database report below errors when indexing stac data using `stac_api_to_odc()` function.
```
  ERROR:  could not serialize access due to read/write dependencies among transactions
  DETAIL:  Reason code: Canceled on identification as a pivot, during commit attempt.
```
