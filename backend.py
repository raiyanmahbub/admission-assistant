import pandas as pd


def load_data(input=None):

    # Load excel data into pandas dataframe
    df = pd.read_csv('PA_dummy_data.csv')

    # Declare local cache and dataframe columns
    prerequisites = dict()
    metrics = dict()

    program = df['Program']
    courses = df['Courses']

    
    try:
        for i in range(len(df)):
            prerequisites[program[i]] = courses[i].replace(' ', '').split(',')
    except:
        pass

    return prerequisites, df


def output_data(input=None):

    # Load excel data into pandas dataframe
    #df = pd.read_excel('PA.xlsx')
    df = pd.read_csv("PA_dummy_data.csv")

    # Declare local cache and dataframe columns
    
    gpa = 3.2
    pce = 1000
    gre = "No"
    
    studentB = df.loc[df.GPA <= gpa][df.PCE_Hours <= pce][df.GRE == gre]
    studentB.sort_values(
        by = "GPA",
        ascending = False
    )
    studentB = studentB.sort_values(by='GPA', ascending=False)

    print(studentB.Program)


output_data()
