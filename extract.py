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
import helpers
import math

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    record_list = []
    with open(neo_csv_path,'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for record in csvreader:
            designation = record['pdes']
            name = record['name'] or None
            hazardous = record['pha'] == 'Y'
            diameter = float(record['diameter']) if record['diameter'] else math.nan
            record_list.append(NearEarthObject(designation,name,diameter,hazardous))
    
    return record_list
        

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    with open(cad_json_path,'r') as jsonfile:
        root_object = json.load(jsonfile)
        fields = root_object.get('fields')
        data_list = [dict(zip(fields,data)) for data in root_object.get('data')]
        return list(CloseApproach(data['des'],helpers.cd_to_datetime(data['cd']),float(data['dist']),float(data['v_rel'])) for data in data_list)
    
