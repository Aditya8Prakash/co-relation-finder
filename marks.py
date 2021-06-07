import csv
import numpy as np

def getDataSource(data_path):
    marks_gained = []
    days_present = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)

        for row in df :
            marks_gained.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

        return {"y":marks_gained,"x":days_present}

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

findcorelation(getDataSource('./marks.csv'))