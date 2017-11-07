if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        markes = student_marks[query_name]
        print(type(markes))
        tot = 0.0
        for mar in markes:
            print(mar)
            tot += mar
        print('{0:.2f}'.format(tot/len(markes)))