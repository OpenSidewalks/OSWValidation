# OpenSidewalks data schema, and its validators

This repository is created to perform validations on the geojson files provided against OpenSideWalks Schema.

### Steps to run:

1. Create a Virtual environment in Python
2. Activate virtual environment
3. Install the required packages to run the code

 
#### Using Pip
1.  `python3 -m venv env`
2.  `source env/bin/activate`
3.  `pip install -r pip_reqs.txt`

##### How to run the code:

  `python main.py --inputPath <<input folder>> --writePath <<Output Directory to Write To>> --schemaPath <<Path of schema file to validate against>>`

Example:

`python main.py --inputPath TestData/input --writePath TestData/Output --schemaPath TestData/Ways_schema.json`

#####  Expected Input:
Input folder should contain nodes (optional), and ways files belonging to a region with the same prefix.   For example:
|FileName  | Data it should contain |
|--|--|
|1. Redmond_nodes.geojson  | Contains all the points in that region |
|2. Redmond_ways.geojson   | Contains all the ways in that region |

##### Output:
The program writes the following files in the output folder
|FileName  | Data it contains |
|--|--|
|1. Redmond_nodes_valid.geojson  | All the points in the region that adhere to OSW Schema |
|2. Redmond_ways_valid.geojson   | All the ways in the region that are in accordance with OSW schema |
|3. Redmond_nodes_invalid.geojson | All the points in the region that do **NOT** adhere to OSW schema|
|4. Redmond_ways_invalid.geojson | All the ways in the region that do **NOT** adhere to OSW schema |
|5. Redmond_ways_Missing_Intersection.geojson | Shows the ways that are probably intersecting but don't have a intersecting node|
|6. Redmond_ways_recommended_Intersection.geojson| Recommended Potential Intersecting points for the ways in *Missing_Intersection.geojson*|
|7. Redmond_ways_connected.geojson | All the ways that are connected to atleast one another way |
|8. Redmond_ways_isolated.geojson | Ways that are not connected to any other ways |
|9. Redmond_ways_subgraph_\*.geojson | Shows a connected island of the region given |

##### How to use the output files:

For the *invalid* files, please look at the tag "fixme" in them to know what is the possible reason for the point or way being invalidated and take the necessary action to fix them.  

Load *Missing_Intersection* file in QGIS to see the ways that are potentially intersecting but don't have an intersecting node.  
Load *Recommended_Intersection* file on top of *Missing_Intersection* files to see recommended intersection points.

#### How to build into an executable:

1. `pyinstaller OSWValidation.py -F`
2. `pyinstaller OSWValidation.spec`
The resulting executable can be found in the dist/ directory.


#### How to file issues:

Please open a GitHub issue for any for any bugs/requested features. For each issue, please provide:
 - Branch commit your code is based on. This could be done in a couple of ways:
  -- pick the 'commit' tag from the first line of the command 'git log' 
  -- If the code you're working on is based on a release tag, provide the release tag 
- Provide potential test input files you used while running the code
