
def findAverage(dictionary):
    for key in dictionary:

        sumArray = 0
        for i in dictionary[key]:
            sumArray = sumArray + i
            avg = round(sumArray / len(dictionary[key]), 2)
        print(f'the average score for {key} is {str(avg)}')

dictionary = {
    'valentine': [1,3,4],
    'Romeo': [2,2,3],
    'juliet': [3,5,6]
}
findAverage(dictionary)
        