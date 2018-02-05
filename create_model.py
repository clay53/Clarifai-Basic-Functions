from clarifaif import create_model

name = raw_input('Enter model name \n')

input1 = raw_input('Enter concepts (seperated by commas NO spaces) \n')
concepts = input1.split(',')

create_model(name, concepts)