import json
import requests

dictionary_courses = {}


def list_courses():
    r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
    print(r.status_code)
    list_courses = []
    final_list_course = []

    for students in r.json():
        for courses in students["courses"]:
            list_courses.append(courses["name"])
    for item in set(list_courses):
        final_list_course.append(item)

    for i in range(0, len(final_list_course)):
        dictionary_courses[i] = final_list_course[i]

    for courses in dictionary_courses:
        print("[{}]-{}".format(courses, dictionary_courses[courses]))

    return dictionary_courses


def match_teams(course_id, team_size, group_time):
    r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
    course_name = dictionary_courses[course_id]
    list_student = []
    group_list = []

    for student in r.json():
        for course in student["courses"]:
            if course['group'] == group_time and course['name'] == course_name:
                list_student.append(student['name'])

    for students in list_student:
        group_list.append(students)
        if len(group_list) == team_size:
            for i in group_list:
                print("\n{} \n".format(i))
            print("==========================")
            group_list = []


def main():
    #print(r.json())
    print("Hello, you can use one the the following commands:\nlist_courses - this lists all the courses that are available now.\nmatch_teams <course_id>, <team_size>, <group_time>")
    while True:
        command = input("> ")
        if command == "list_courses":
            list_courses()
        elif command.find("match_teams") != -1:
                args = command.split(" ")
                if len(args) != 4:
                    print("Invalid match_teams arguments")
                list_courses()
                match_teams(int(args[1]), int(args[2]), int(args[3]))
if __name__ == '__main__':
    main()
