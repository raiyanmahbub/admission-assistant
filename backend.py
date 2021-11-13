import pandas as pd


def load_data(input=None):

    # Load excel data into pandas dataframe
    df = pd.read_excel('PA.xlsx')

    # Declare local cache and dataframe columns
    prerequisites = dict()
    metrics = dict()

    program = df['Program']
    courses = df['Courses']

    metrics = dict()
    
    try:
        for i in range(len(df)):
            prerequisites[program[i]] = courses[i].replace(' ', '').split(',')
    except:
        pass


    try:
        for i in range(len(df)):
            metrics[program[i]] = {'GPA' : df['GPA'][i], 'PCE Hours' : df['PCE Hours'][i], 'GRE' : df['GRE'][i]}
    except:
        pass

    return prerequisites, metrics


a, b = load_data()
print(a)
print(b)