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


def clean_data(form_data):
    return form_data





def output_data(input, gpa, pce, gre):

    prereq, df = load_data()


    student = df.loc[df.GPA <= gpa][df.PCE_Hours <= pce][df.GRE == gre]
    student.sort_values(
        by = "GPA",
        ascending = False
    )

    program = student.Program.values
    courses = student.Courses.values

    output = []
    final = []
    
    for i in range(len(courses)):
        output.append(courses[i].replace(' ', '').split(','))
    output = output[0]

    for i in prereq:
        if set(prereq[i]).issubset(set(input)):
            if i in program:
                final.append(i)

    print(final)
    
              

    


output_data(['HumanAnatomy', 'HumanPhysiology', 'Biochemistry'], 3.4, 1000, 'No')
