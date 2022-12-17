import pandas as pd
from itertools import combinations
from infra.infra import insertDatabase
from data.subsetsTable import subsets 
import os

class algoritmos:
    def __init__(self, num):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.num = num
        tbl = subsets()
        tbl.update()
        self.loadData()
        self.subsetSum(5, self.vector, self.num)
        self.saveSubsets()

    def loadData(self):
        data = pd.read_csv(f'{self.current_path}/../files/data_vector.csv')
        self.vector = data.drop_duplicates().sort_values("11", ascending=True)["11"].to_list()

    def subsetSum(self, n, arr, x): 
        out = []
        for i in range(n+1):
            for subset in combinations(arr, i): 
                if sum(subset) == x:
                    out.append(','.join(map(str, list(subset))))

        self.subsets = pd.DataFrame(out, columns=["subset"])

    def saveSubsets(self): 
        self.subsets.apply(lambda x: insertDatabase(f'''INSERT INTO subsets (subset) VALUES ('{x["subset"]}')'''), axis=1)
