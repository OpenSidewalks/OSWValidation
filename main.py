import argparse as ag
import os
import sys
import json
from OSWValidation.json_structure import validate_json_structure
# from intersectingValidation import intersectLineStringInValidFormat
from glob import glob
# from node_connectivity import plot_nodes_vs_ways, subgraph_eda, get_invalidNodes
from config import DefaultConfigs
from OSWValidation.util_data import UtilData
# from Validate_JsonFile_Schema import validate_json_schema
import ntpath
from OSWValidation.util_defs import merge_dicts, write_outputs
import copy

if __name__ == '__main__':
    parser = ag.ArgumentParser()
    parser.add_argument("--inputPath", help="Relative input path to GeoJSON files. Default: TestData\input",
                        default=os.path.join(os.getcwd(), "TestData\input"))
    parser.add_argument("--writePath", help="Relative output path to write the validation errors. Default: TestData\Output",
                        default=os.path.join(os.getcwd(), "TestData\Output"))
    args = parser.parse_args()
    cf = DefaultConfigs(args)

    json_files = glob(os.path.join(cf.inputPath, "*.geojson"))
    print("Reading files from :", cf.inputPath)
    print("Number of geojson files :", len(json_files))
    nodes_files = sorted([x for x in json_files if 'node' in x.lower()])
    ways_files = sorted([x for x in json_files if 'node' not in x.lower()])

    for ind, (nodes_file, ways_file) in enumerate(zip(nodes_files, ways_files)):
        print('Processing the following files : \n{}\n{}'.format(ntpath.basename(nodes_file),
                                                                 ntpath.basename(ways_file)))

        utild = UtilData(nodes_file, ways_file, cf)
        utildOriginal = copy.deepcopy(utild)

        if cf.do_all_validations or cf.do_schema_validations:
            # invalid_schema_nodes_dict = validate_json_schema(nodes_file, cf.node_schema, cf.writePath)
            with open(os.path.join(sys.path[0], ways_file), 'r') as fp:
                ways_geojson = json.load(fp)
            invalid_schema_ways_dict = validate_json_structure(ways_geojson)

        # invalid_nodes_dict, invalid_ways_dict = get_invalidNodes(utild, cf)

        # merged_nodes_dict = merge_dicts(invalid_schema_nodes_dict, invalid_nodes_dict)
        # merged_ways_dict = merge_dicts(invalid_schema_ways_dict, invalid_ways_dict)

        write_outputs(utild, cf, invalid_schema_ways_dict)

        # if cf.do_intersecting_validation:
        #     intersectLineStringInValidFormat(utildOriginal.ways_json, "brunnel", cf, ntpath.basename(ways_file))

        if cf.do_eda:
            print("--" * 10)
            print("eda")
            print("--" * 10)
            #plot_nodes_vs_ways(utild, cf)
            # subgraph_eda(utildOriginal, cf)
    print("\n Output files written at the following location ", cf.writePath)
