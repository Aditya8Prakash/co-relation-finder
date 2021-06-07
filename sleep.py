import csv
import numpy as np

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        
        for row in df :
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

        return {"y":coffee_in_ml,"x":sleep_in_hours}

def findcorelation (data_source) :
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    relation = round(correlation[0,1])

    info = 'data is '
    if relation > 0 :
        info = info + 'co-related'
    elif relation < 0 :
        info = info + 'inversly co-related'
    if relation == 0 :
        info = info + 'not co-related'

    print(info)
    print("correlation is ",correlation[0,1])

findcorelation(getDataSource('./sleep.csv'))