import pandas as pd


def load_data(input=None):

    # Load excel data into pandas dataframe
    df = pd.read_excel('PA.xlsx')

    # Declare local cache and dataframe columns
    cache = dict()
    program = df['Program']
    courses = df['Courses']

    try:
        for i in range(len(df)):
            cache[program[i]] = courses[i].replace(' ', '').split(',')
    except:
        pass

    print(cache)


load_data()