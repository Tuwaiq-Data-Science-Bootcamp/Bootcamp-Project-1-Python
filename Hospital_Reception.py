# This function is used to collect patient information
def get_patient_information():
    patient_information = {'name': str, 'age': int,
                           'the disease': str, 'gender': str}
    patient_name = input("your name: ")
    patient_age = input('your age: ')
    patient_gender = input('your gender: ')
    patient_information.update({'name': patient_name})
    patient_information.update({'age': patient_age})
    patient_information.update({'gender': patient_gender})
    patient_information.update({'the disease': None})
    return patient_information


# This post is to find out about the disease
def get_disease(patient_information):
    print("(yes/no)")
    if input('Do you feel cold? ').upper() == 'YES':
        patient_information.update({'the disease': 'cold'})

    elif input('Do you feel allergies? ').upper() == 'YES':
        patient_information.update({'the disease': 'allergies'})

    elif input('Do you feel diarrhea? ').upper() == 'YES':
        patient_information.update({'the disease': 'diarrhea'})

    elif input('Do you feel headaches? ').upper() == 'YES':
        patient_information.update({'the disease': 'headaches'})

    elif input('Do you feel mononucleosis? ').upper() == 'YES':
        patient_information.update({'the disease': 'mononucleosis'})

    elif input('Do you feel stomach aches? ').upper() == 'YES':
        patient_information.update({'the disease ': 'stomach aches'})
    else:
        print("Seems you are alright don't be a baby.")
        patient_information.update({'the disease': None})



# This function is to find out the duration of the vacation
def get_the_sick_leave(patient_information):
    sick_leave_days = input('you can take (1-5) days: ')
    #sick_leave_validation = lambda a , b : patient_information.get('the disease') == a or patient_information.get('the disease') == b
    sick_leave_validation = lambda a , b : patient_information.get('the disease') == a or patient_information.get('the disease') == b
    if sick_leave_validation('cold',None):
        print('Sorry, you don\'t need a Sick Leave, your disease is not worth of Sick Leave.')
    else:
        print(' ________________________________________________________________________\n',
        '|| Patient\'s name', patient_information.get('name') , 'patient\'s age', patient_information.get('age'), 'patient\'s gender', patient_information.get('gender'),'||\n', 
        '|| the disease', patient_information.get('the disease'),'||\n',
        '|| duration of Sick Leave', sick_leave_days, 'days ||\n',
        '||______________________________________________________________________')


patient = None
while True:
    print("Choose ( 0 - 4 ): ")
    reception = input(
        '1: Add/Update Informations || 2: Detect Disease || 3: Sick Leave || 4: View Profile || 0: Exit \n')
    if patient is None and (reception == '2' or reception == '3' or reception == '4'):
        print("#ERROR: Patient Information Must Be Added First")
        patient = get_patient_information()
    elif reception == '1':
        patient = get_patient_information()
    elif reception == '2':
        get_disease(patient)
    elif reception == '3':
        get_the_sick_leave(patient)
    elif reception == '4':
        print(patient)
    elif reception == '0':
        print('Have a good day :D')
        break
    else:
        print('Sorry, Invalid Input.')
