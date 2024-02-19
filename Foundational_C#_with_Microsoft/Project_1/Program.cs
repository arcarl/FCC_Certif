// See https://learn.microsoft.com/fr-fr/training/paths/get-started-c-sharp-part-1/  for more information about the content of the course


// Part 1
using System.Reflection.Metadata;

Console.WriteLine("Part 1 - Calculayte and print Student grade:\n");


// initialize variables - graded assignments 
int currentAssignments = 5;

int sophia1 = 93;
int sophia2 = 87;
int sophia3 = 98;
int sophia4 = 95;
int sophia5 = 100;

int nicolas1 = 80;
int nicolas2 = 83;
int nicolas3 = 82;
int nicolas4 = 88;
int nicolas5 = 85;

int zahirah1 = 84;
int zahirah2 = 96;
int zahirah3 = 73;
int zahirah4 = 85;
int zahirah5 = 79;

int jeong1 = 90;
int jeong2 = 92;
int jeong3 = 98;
int jeong4 = 100;
int jeong5 = 97;

// calculate average
decimal avg_sophia = (sophia1 + sophia2 + sophia3 + sophia4 + sophia5)/5;
decimal avg_nicolas = (nicolas1 + nicolas2 + nicolas3 + nicolas4 + nicolas5)/5;
decimal avg_zahirah= (zahirah1 + zahirah2 + zahirah3 + zahirah4 + zahirah5)/5;
decimal avg_jeong = (jeong1 + jeong2 + jeong3 + jeong4 + jeong5)/5;


// return the average for every student
Console.WriteLine("Student\t\tGrade\n");
Console.WriteLine("Sophia:\t\t" + avg_sophia + "\tA");
Console.WriteLine("Nicolas:\t" + avg_nicolas + "\tB" );
Console.WriteLine("Zahirah:\t" + avg_zahirah + "\tB");
Console.WriteLine("Jeong:\t\t" + avg_jeong + "\tA \n\n");

// Part 2 
Console.WriteLine("Part 2 - Calculate final GPA\n");

// courses and associated credits
string studentName = "Sophia Johnson";
string course1Name = "English 101";
string course2Name = "Algebra 101";
string course3Name = "Biology 101";
string course4Name = "Computer Science I";
string course5Name = "Psychology 101";

int course1Credit = 3;
int course2Credit = 3;
int course3Credit = 4;
int course4Credit = 4;
int course5Credit = 3;

// Grades value and grade per course
int grade_A = 4;
int grade_B = 3;

int grade_c1 = grade_A;
int grade_c2 = grade_B;
int grade_c3 = grade_B;
int grade_c4 = grade_B;
int grade_c5 = grade_A;


// calculate GPA
int all_credit = course1Credit + course2Credit +course3Credit + course4Credit + course5Credit;
int all_points = grade_c1 * course1Credit + grade_c2 * course2Credit + grade_c3 * course3Credit + grade_c4 * course4Credit + grade_c5 * course5Credit;
decimal gpa =  (decimal) all_points/all_credit;
int int_gpa = (int) gpa;
int fdigit = (int) (gpa * 10 ) % 10;
int sdigit = (int) (gpa * 100 ) % 10;


//return the requested output format
Console.WriteLine($"Student: {studentName}\n");

Console.WriteLine("Course\t\t\tGrade\t\tCredit Hours");
Console.WriteLine($"{course1Name}\t\t{grade_c1}\t\t{course1Credit}");
Console.WriteLine($"{course2Name}\t\t{grade_c2}\t\t{course2Credit}");
Console.WriteLine($"{course3Name}\t\t{grade_c3}\t\t{course3Credit}");
Console.WriteLine($"{course4Name}\t{grade_c4}\t\t{course4Credit}");
Console.WriteLine($"{course5Name}\t\t{grade_c5}\t\t{course5Credit}\n");

Console.WriteLine($"Final GPA:\t\t {int_gpa}.{fdigit}{sdigit}");





