"""
Config file
Command line arguments overwrites these configs
This object saves the input and output paths
"""
import os
import ntpath


class DefaultConfigs:

    def __init__(self, args=None):
        self.inputPath = args.inputPath
        self.writePath = args.writePath
        self.schemaPath = args.schemaPath
        if not os.path.exists(self.writePath):
            os.mkdir(self.writePath)

        self.node_schema = os.path.join(
            os.getcwd(), "Json Schema", "Nodes_schema.json")
        self.ways_schema = os.path.join(
            os.getcwd(), "Json Schema", "Ways_schema.json")

        self.do_all_validations = True
        self.do_eda = True
        self.do_schema_validations = True
        self.do_intersecting_validation = True
