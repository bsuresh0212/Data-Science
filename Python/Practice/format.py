age = 20
name = "SureshB"

# start index for 0 in format menthod
#why format menthod
    # 1.fomat method internally conert as a string
    # 2.prober way to use
print('{0} was {1} years old'.format(name,age))

#without using number also automatically print the format method arguments
print('{} was {} years old'.format(name,age))

#decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/1.0))

#fill with underscore(_) with the text centered
#(^) to 11 width ''
print('{0:.^20}'.format('SureshB'))

#keyword-based 
print('{name} from {place}'.format(name = "SureshB",place="Gudiyatham"))