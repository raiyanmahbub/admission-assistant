import pandas as pd


def load_data(input=None):

    # Load excel data into pandas dataframe
    df = pd.read_csv('PA_dummy_data.csv')

    # Declare local cache and dataframe columns
    prerequisites = dict()

    program = df['Program']
    courses = df['Courses']
 
    try:
        for i in range(len(df)):
            prerequisites[program[i]] = courses[i].replace(' ', '').split(',')
        else:
            print(df[i])
    except:
        pass

    return prerequisites, df



def clean_data(form_data):
    gpa = float(form_data['gpa'])
    pce = int(form_data['pce'])
    try:
        gre = 'Yes' if form_data['gre'] == '1' else 'No'
    except:
        gre = 'No'

    prereq_list = []
    for key in form_data.keys():
        prereq_list.append(key)

    try:
        prereq_list.remove('gpa')
        prereq_list.remove('pce')
        prereq_list.remove('gre')
    except:
        pass


    final = output_data(prereq_list, gpa, pce, gre)
    print(final)

    return final



def output_data(input, gpa, pce, gre):

    prereq, df = load_data()

# =============================================================================
#     if df.GRE == 'No':
#         student = df.loc[
#             (df.GPA <= gpa) &
#             (df.PCE_Hours <= pce)
#         ]
#     else:
#         student = df.loc[
#             (df.GPA <= gpa) &
#             (df.PCE_Hours <= pce)  &
#             (df.GRE == gre)
#         ]
# =============================================================================

    student = df.loc[
        (df.GPA <= gpa) &
        (df.PCE_Hours <= pce)  &
        ((df.GRE == gre) | (df.GRE == 'Yes'))
        ]

    print(student)

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

    return final
    
              


# output_data(['HumanAnatomy', 'HumanPhysiology', 'Biochemistry'], 3.4, 1000, 'No')
clean_data({'gpa': '4.0', 'pce': '1000000', 'gre': 'Yes', 'HumanAnatomy': '1', 'HumanPhysiology': '1', 'Biochemistry': '1', 'Microbiology': '1', 'OrganicChemistryI': '1', 'Genetics': '1', 'Psychology': '1', 'Statistics': '1', 'MedicalTerminology': '1'})
