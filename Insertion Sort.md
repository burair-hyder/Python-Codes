# This contains code and explanation for Insertion Sort in Python

````
# INSERTION SORT

# its an algorithm to arrange an array in
# either ascending orr descending order

# what is the diff between bubble sort and insertion sort??


# the main diff between bubble sort and insertion sort is that bubble sort performs sorting by
# checking the neighboring data elements and swapping them if they are in
# wrong order while insertion sort performs sorting by transferring one element to
# a partially sorted array at a time .

# in  insertion sort consider each element as a card. first  element is considered
# to be sorted and then 2nd element is then moved towards the correct position

# there will be two loops one outer loop and one innner looo

# outer loop will be for loop which will check each element and the inner loop\
# will be conditional while loop which will find the correct position of the element

# for loop ( each element )
# shifting and correct position ( while loop )

# CODE FOR INSERTION SORT


#            0  1 2 3 4 5  6  7  8  9

def InsertionSort():
    arraysize = len(arrayData)

    for pointer in range(1,arraysize):
        valuetoinsert = arrayData[pointer]
        holeposition = pointer

        while (holeposition > 0) and (arrayData[holeposition-1]> valuetoinsert):

            arrayData[holeposition] = arrayData[holeposition-1]
            holeposition = holeposition-1

        arrayData[holeposition] = valuetoinsert

InsertionSort()
print(arrayData)
````
