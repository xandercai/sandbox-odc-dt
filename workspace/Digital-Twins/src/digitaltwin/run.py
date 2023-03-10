# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:21:34 2021

@author: pkh35
"""
import json
import pathlib

from src import config
from src.digitaltwin import insert_api_to_table
from src.digitaltwin import setup_environment


def input_data(file):
    """Read json instruction file to store record i.e. api details to the database."""
    # load in the instructions to add building outlines api from LINZ
    file_path = pathlib.Path().cwd() / pathlib.Path(file)
    with open(file_path, "r") as file_pointer:
        instructions = json.load(file_pointer)
    instruction_node = instructions["instructions"]

    return instruction_node


def main():
    # Read in the database - will fail if the database hasn't been setup.
    engine = setup_environment.get_database()
    stats_nz_api_key = config.get_env_variable("StatsNZ_API_KEY")
    # Create region_geometry table if it doesn't exist in the database
    # No need to call region_geometry_table function if region_geometry
    # table exist in the database
    insert_api_to_table.region_geometry_table(engine, stats_nz_api_key)

    record = input_data("Digital-Twins/src/digitaltwin/instructions_run.json")

    # Substitute api key into link template
    linz_api_key = config.get_env_variable("LINZ_API_KEY")
    record["api"] = record["api"].format(api_key=linz_api_key)

    # Call the function to insert record in apilinks table
    insert_api_to_table.insert_records(
        engine,
        record["data_provider"],
        record["source_name"],
        record["api"],
        record["region_name"],
        record["geometry_col_name"],
        record["url"],
        record["layer"],
    )


if __name__ == "__main__":
    main()
