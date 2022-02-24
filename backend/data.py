from unittest import result
import pandas as pd


def load_data(input=None):

    # Load excel data into pandas dataframe
    df = pd.read_csv('backend/PA_dummy_data.csv')

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

    programs = {}
    results = {}

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

    programs = {'Augsburg University': {'Location': 'Minneapolis, MN', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='}, 
                'Concordia University - Wisconsin': {'Location': 'Mequon, WI', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'Des Moines University': {'Location': 'Des Moines, IA', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'Mayo Clinic College of Medicine': {'Location': 'Rochester, MN', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'Northwestern College': {'Location': 'Chicago, IL', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'St. Catherine University': {'Location': 'Minneapolis, MN', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'University of North Dakota': {'Location': 'Grand Forks, ND', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'University of South Dakota': {'Location': 'Vermillion, SD', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'University of Wisoncin - Lacrosse': {'Location': 'La Crosse, WI', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='},
                'University of Wisonsin - Madison': {'Location': 'Madison, WI', 'Image': 'https://media.istockphoto.com/photos/university-in-autumn-picture-id173598452?k=20&m=173598452&s=612x612&w=0&h=49b4CwEsyt_9zJGVeJDiYOMIYLiuy55yNlOMoj5lDq4='}}
    
    for i in programs.keys():
        if i in final:
            results[i] = programs[i]

    print(results)
    return results



def output_data(input, gpa, pce, gre):

    prereq, df = load_data()

    # GPA, PCE, GRE FILTERING
    if gre == 'Yes':
        student = df.loc[
            (df.GPA <= gpa) &
            (df.PCE_Hours <= pce)
        ]
    else:
        student = df.loc[
            (df.GPA <= gpa) &
            (df.PCE_Hours <= pce)  &
            (df.GRE == gre)
        ]

    student.sort_values(
        by = "GPA",
        ascending = False
    )

    # COURSE FILTERING
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

    # FINAL OUTPUT OF ELIGIBLE PROGRAMS
    return final
    
              


# output_data(['HumanAnatomy', 'HumanPhysiology', 'Biochemistry'], 13.4, 10000000, 'No')
# clean_data({'gpa': '4.0', 'pce': '1000000', 'HumanAnatomy': '1', 'HumanPhysiology': '1', 'Biochemistry': '1', 'Microbiology': '1', 'OrganicChemistryI': '1', 'Genetics': '1', 'Psychology': '1', 'Statistics': '1', 'MedicalTerminology': '1'})
