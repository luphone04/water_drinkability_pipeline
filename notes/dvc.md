dvc stage add -n data_collection -d src/data_collection.py -o data/raw python3 src data_collection.py

dvc stage add: add a new stage to yaml file
-n data_collection: name of the stage
-d src/data_collection.py: declare that path as input dependency
-o data/raw: stage's output
python3 src data_collection.py: command DVC will run for the stage