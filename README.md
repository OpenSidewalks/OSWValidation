# OpenSidewalks data schema, and its validators

This repository is created to perform validations on the geojson files provided against OpenSideWalks Schema.

## Usage

### Steps to run:

1. Create a Virtual environment in Python
2. Activate virtual environment
3. Install the required packages to run the code

 
### Using Pip
1.  `python3 -m venv env`
2.  `source env/bin/activate`
3.  `pip install -r pip_reqs.txt`

### How to run the code:

  `python main.py --inputPath <<input folder>> --writePath <<Output Directory to Write To>> --schemaPath <<Path of schema file to validate against>>`

Example:

`python main.py --inputPath TestData/input --writePath TestData/Output --schemaPath TestData/Ways_schema.json`

####  Expected Input:
Input folder should contain nodes (optional), and ways files belonging to a region with the same prefix.   For example:
|FileName  | Data it should contain |
|--|--|
|1. Redmond_ways.geojson   | Contains all the ways in that region |

#### Output:
The program writes the following files in the output folder
|FileName  | Data it contains |
|--|--|
|1. Redmond_ways_valid.geojson   | All the ways in the region that are in accordance with OSW schema |
|2. Redmond_ways_invalid.geojson | All the ways in the region that do **NOT** adhere to OSW schema |
|3. Redmond_ways_connected.geojson | All the ways that are connected to atleast one another way |
|4. Redmond_ways_isolated.geojson | Ways that are not connected to any other ways |

#### How to use the output files:

For the *invalid* files, please look at the tag "fixme" in them to know what is the possible reason for the point or way being invalidated and take the necessary action to fix them.  

### How to build into an executable:

1. `pyinstaller OSWValidation.py -F`
2. `pyinstaller OSWValidation.spec`
The resulting executable can be found in the dist/ directory.

### Running the executable on MacOS
Before running the executable, you need to Ctrl+click it in the File Explorer, then click "Open" to enable permissions to run.

After running it once using this method, you should have permissions to use the executable from the command line.

## Features
OSWValidation is a fork from the original OSWValidation project linked (here)[]. This fork supports the latest version of the OpenSidewalks schema, as well as future versions.

The newest version refactors the OSWValidation functions into an importable library, allowing the validation to be utilized across other OSW projects. A Python script is provided that invokes this library, which can be built into an executable for Linux, Mac, and Windows using PyInstaller.

Features that still need to be added:
- Sign the executable so it can be run on any Mac without running into permission issues
- Allow the OSWValidation library to be installed into any project using a command like `pip install`
- Show an error message when no arguments are provided rather than using default arguments
  - For example, when running python OSWValidation.py without any arguments, we should print an error and not do any validation
- Add in options for other sorts of validation included in the original repository, i.e. intersecting validation
- Verify or add support for points/nodes geojson file validation rather than just ways as the original repository does
  - The library should already be able to do this by providing a custom schema document, however we need an example test case and schema file to test against

### How to file issues:

Please open a GitHub issue for any for any bugs/requested features. For each issue, please provide:
 - Branch commit your code is based on. This could be done in a couple of ways:
  -- pick the 'commit' tag from the first line of the command 'git log' 
  -- If the code you're working on is based on a release tag, provide the release tag 
- Provide potential test input files you used while running the code
