"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import traceback

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        neos = []
        reader = csv.DictReader(infile)
        for elem in reader:
            try:
                neo = NearEarthObject(
                    designation=elem["pdes"] if elem["pdes"] else '', 
                    name=elem["name"] if elem["name"] else None, 
                    hazardous=True if elem["pha"]=='Y' else False,
                    diameter=float(elem["diameter"] if elem["diameter"] else 'nan')
                )
            except Exception as e:
                print("load_neos: ",e,"Traceback: ",traceback.format_exc())
            else:
                neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)  # Parse JSON data into a Python object.
        reader = [dict(zip(contents["fields"], data)) for data in contents["data"]]
        close_approaches = []
        for elem in reader:
            try:
                ca = CloseApproach(
                    designation=elem["des"],
                    time=elem["cd"],
                    distance=float(elem["dist"]),
                    velocity=float(elem["v_rel"]),
                )
            except Exception as e:
                print("load_approaches: ",e,"Traceback: ",traceback.format_exc())
            else:
                close_approaches.append(ca)    
    return close_approaches




