import pandas as pd
class Dataset:
    def __init__(self, link):
        self.df = pd.read_csv(link)

    def frame(self):
        return self.df

    #To get number of rows
    def row_count(self):
        return len(self.df.index)

    #To get number of columns
    def column_count(self):
        return len(self.df.columns)

    #To remove duplicates
    def remove_duplicates(self, keep='first'):
        self.df = self.df.drop_duplicates(keep=keep, ignore_index=True)

    #To remove empty rows
    def remove_empty(self, axis=0):
        self.df = self.df.dropna(axis)

    #To replace empty int values with mean
    def replace_with_mean(self, columnName):
        self.df[columnName].fillna(value=self.df[columnName].mean(), inplace=True)

    #To replace empty int values with median
    def replace_with_median(self, columnName):
        self.df[columnName].fillna(value=self.df[columnName].meadian(), inplace=True)

    #To replace empty int values with mode
    #def replace_with_mode(self, columnName):
def main():
    df = Dataset("movies.csv")
    print(df.frame()[:10])




if __name__ == "__main__":
    #main()
    a = 0
    i = 1
    for k in range(0,10):
        i = k^2
        for j in range(i):
            a += 1
        a+=1
    print(a)
