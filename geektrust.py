from sys import argv   
from LearningManagementSystem import LearningManagementSystem as LMS
        
def parse_input(inputs, LMS_object) -> None:
    for input in inputs:
        command,params = input.split(" ",1)
        params = params.strip("\n").split(" ")
        match command:
            case 'ADD-COURSE-OFFERING':
                try:
                    print(LMS_object.add_course_offering(*params),"\n")
                except TypeError as e:
                    print("INPUT_DATA_ERROR\n")
            case 'REGISTER':
                try:
                    print(LMS_object.register(*params),"\n")
                except TypeError as e:
                    print("INPUT_DATA_ERROR\n")
            case 'ALLOT':
                try:
                    print(LMS_object.course_allotment(*params),"\n")
                except TypeError as e:
                    print("INPUT_DATA_ERROR\n")
            case 'CANCEL':
                try:
                    print(LMS_object.cancel_registration(*params),"\n")
                except TypeError as e:
                    print("INPUT_DATA_ERROR\n")
            case _:
                print("INPUT_DATA_ERROR")  
    
def main():
    if len(argv) != 2:
        raise Exception("Input file path not entered")
    input_file_path = argv[1]
    input_file = open(input_file_path, 'r')
    inputs = input_file.readlines()
    LMS_object = LMS()
    parse_input(inputs, LMS_object)
    
    
if __name__ == "__main__":
    main()