import os #imports the os module



os.mkdir("Score")#creates a directory called "Score"
os.chdir("Score") #after creating the directory, change the files into that directory
print("the current working directory is: ", os.getcwd()) #finds what current directory we are on

def Score_Input(): #asks for the inputs from the user
    Algebra = eval(input("enter the students algebra score: "))
    English = eval(input("enter the students english score: "))
    Statistics = eval(input("Enter the students statistics score: "))
    History = eval(input("enter the students history score: "))
    Biology = eval(input("enter the students biology score: "))
    Physics = eval(input("enter the students physics score: "))
    Computing = eval(input("enter the students computing score: "))
    return Algebra, English, Statistics, History, Biology, Physics, Computing



def score(): #creates the files for each student inputed
    Student_Info = {} #A dictionary that holds the information of each student
    Num_Of_Students = int(input("Enter the number of students: "))#asks for the number of students
    
    

    for i in range(Num_Of_Students):#iterates through the amount of stuents
        names = input("enter the name of the student: ")#asks for the students name
        a,e,s,h,b,p,c =  Score_Input()#variables that takes the values of the inputs
        total = a + e + s + h + b + p + c #adds all the values together
        average = total / 7 #takes the average of all the values
        Student_Info[names] = (a,e,s,h,b,p,c, total, average)#stores all values in the dictionary
        print(Student_Info)#prints out the dictionary



    for name in sorted(Student_Info.keys()):#creates a file for each student and stores them
        #in the directory
        #each file contains the subject and the grade along with the total and average
        f = open(name+'.txt', 'w')
        f.write("Algebra")
        f.write("      ")
        f.write(str(Student_Info[name][0])+"\n")
        f.write("English")
        f.write("      ")
        f.write(str(Student_Info[name][1])+"\n")
        f.write("Statistics")
        f.write("    ")
        f.write(str(Student_Info[name][2])+"\n")
        f.write("History")
        f.write("      ")
        f.write(str(Student_Info[name][3])+"\n")
        f.write("Biology")
        f.write("      ")
        f.write(str(Student_Info[name][4])+"\n")
        f.write("Physics")
        f.write("      ")
        f.write(str(Student_Info[name][5])+"\n")
        f.write("Computing")
        f.write("      ")
        f.write(str(Student_Info[name][6])+"\n")
        f.write("Total")
        f.write("      ")
        f.write(str(Student_Info[name][7])+"\n")
        f.write("Average")
        f.write("      ")
        f.write(str(Student_Info[name][8])+"\n")
        f.close()

score()#tests the function
       
        
if __name__ == "__main__":

    
    #this part asks for a students name and attempts to find the file information
    Student_Name_Input = input("enter a students name: ")
    for file in os.getcwd():
        if file == Student_Name_Input+'.txt':
            f = open(Student_Name_Input+'.txt', 'r')
