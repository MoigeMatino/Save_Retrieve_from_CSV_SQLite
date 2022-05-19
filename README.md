# Saving and Retrieving data from CSV Files and SQLite

This program defines two controllers that define how to save and retrieve data from csv files and sqlite database built in Python.

## Installation

To run this program:

Clone this repository to your local machine using:

```sh
git clone https://github.com/MoigeMatino/Save_Retrieve_from_CSV_SQLite
```

## Running

To run the program, `cd` into the project then run this command (on Windows):

```sh
python main.py 
```

On Linux/Mac, run the following command:

```sh
python3 main.py 
```

## How it works

The program is made up of two controllers, namely:

- `class ControllerCsv` : this consists of two methods that define how data is saved and queried from a csv file.

- `class ControllerSqlite` : this contoller consists of two methods that define how data is saved and queried from a sqlite table.

### class ControllerCsv 

This controller consists of two methods defined below:

- `def write_to_csv(self,data:User)` : takes in the parameter `data` from the user then writes this data to a csv file.

- `def query_csv(self, obj_id:int)`: takes in the parameter `obj_id` from the user to be used to query the csv file for a record whose `id` matches  `obj_id`

### class ControllerSqlite

This controller consists of two methods defined below:

- `def save_to_db(self,data:User)` : takes in the parameter `data` from the user then writes this data to a csv file.

- `def query_db(self, obj_id:int)`: takes in the parameter `obj_id` from the user to be used to query the table for a record whose `id` matches  `obj_id`

## Note

The `main()` method defines the workflow of the running of the  program to execute the requisite functionalities. Defined also in the `main()` method, are the test data sets to be passed into the respective methods. This test data sets can be altered to aid in further testing.

The `*_data_set` test data are sample inputs to save into the database/csv file.

The `*_query_set` test data are sample ids to query against the database/csv file.


