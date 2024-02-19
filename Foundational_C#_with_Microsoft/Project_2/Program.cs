using System;

// initialize variable - names - grades
int examAssignments = 5;

string[] students = new string[] { "Sophia", "Andrew", "Emma", "Logan", "Becky", "Chris", "Eric", "Gregor" };
int[] sophiaGrades = new int[] { 90, 86, 87, 98, 100, 94, 90 };
int[] andrewGrades = new int[] { 92, 89, 81, 96, 90, 89 };
int[] emmaGrades = new int[] { 90, 85, 87, 98, 68, 89, 89, 89 };
int[] loganGrades = new int[] { 90, 95, 87, 88, 96, 96 };
int[] beckyGrades = new int[] { 92, 91, 90, 91, 92, 92, 92 };
int[] chrisGrades = new int[] { 84, 86, 88, 90, 92, 94, 96, 98 };
int[] ericGrades = new int[] { 80, 90, 100, 80, 90, 100, 80, 90 };
int[] gregorGrades = new int[] { 91, 91, 91, 91, 91, 91, 91 };    



// report header
Console.WriteLine("Student\t\tGrade\n");

// loop to calculate the grade of every student
foreach (string name in students){
    
    int sumStudent = 0;
    int[] gradesStudent = new int[examAssignments];

    // affecting gradesStudent to the right student
    if (name == "Sophia"){
        gradesStudent = sophiaGrades;
    }
    else if (name == "Andrew"){
        gradesStudent = andrewGrades;
    }
    else if (name == "Emma"){
        gradesStudent = emmaGrades;
    }
    else if (name == "Logan"){
        gradesStudent = loganGrades;
    }
    else if (name == "Becky"){
        gradesStudent = beckyGrades;
    }
    else if (name == "Chris"){
        gradesStudent = chrisGrades;
    }
    else if (name == "Eric"){
        gradesStudent = ericGrades;
    }
    else if (name == "Gregor"){
        gradesStudent = gregorGrades;
    }

    // initialize the number of assignments
    int gradedAssignments = 0;

    // accumulate the grades - and extra work
    foreach (int grade in gradesStudent)
    {
        gradedAssignments += 1;
        if (gradedAssignments <= examAssignments)
        {
            sumStudent += grade;

        }
        else
            sumStudent += grade / 10;
    }

    // calculate the current grade 
    decimal currentGrade = (decimal) sumStudent/examAssignments;
    string currentLetter = "?";

    // assining the correct grade
    if (currentGrade >= 97)
        currentLetter = "A+";

    else if (currentGrade >= 93)
        currentLetter = "A";

    else if (currentGrade >= 90)
        currentLetter = "A-";

    else if (currentGrade >= 87)
        currentLetter = "B+";

    else if (currentGrade >= 83)
        currentLetter = "B";

    else if (currentGrade >= 80)
        currentLetter = "B-";

    else if (currentGrade >= 77)
        currentLetter = "C+";

    else if (currentGrade >= 73)
        currentLetter = "C";

    else if (currentGrade >= 70)
        currentLetter = "C-";

    else if (currentGrade >= 67)
        currentLetter = "D+";

    else if (currentGrade >= 63)
        currentLetter = "D";

    else if (currentGrade >= 60)
        currentLetter = "D-";

    // printing the final grade
    Console.WriteLine($"{name}\t\t{currentGrade}\t{currentLetter}");
}
Console.ReadLine();
