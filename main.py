from file_reader import FileReader
reader = FileReader("datasetTest")
pathFile=reader.read_Files()
examples,attributes= reader.read_dataset()
print(examples)
target_attribute=reader.chose_targetattribute()
print(target_attribute)
new_record =reader.read_newState()
record_dict = dict(zip(attributes, new_record))
print('The new record:\n\t' + str(record_dict) + ' ' + target_attribute + '=?' )
print('Run of Baysean Alrotihm')
from runBaysaen import Baysaen
baysaen=Baysaen(examples,attributes,target_attribute,record_dict)
baysaen.predict_class()
