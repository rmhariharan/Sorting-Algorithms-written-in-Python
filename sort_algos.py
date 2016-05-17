class Sorts(object):
    '''Contains three different sorting functions'''
    def __init__(self,mylist):
        self.mylist = mylist
    def selection_sort(self):
        '''Implements selection sort, a not very efficient way of sorting a list'''
        left_list = list()
        right_list = self.mylist
        assert type(right_list) == list 
        x = len(right_list) 
        y = 1
        smallest = None
        first = None
        for i in range(0,x):
            first = right_list[0]
            while y < len(right_list):
                if first > right_list[y]:
                    smallest = right_list[y]
                    first = smallest
                elif first == right_list[y]:
                    smallest = first
                elif first < right_list[y]:
                    smallest = first
                y = y+1
            y = 1
            left_list.append(smallest)
            right_list.remove(smallest)
            if len(right_list) == 1:
                left_list.append(right_list[0])
                break
        return left_list
    def insert_sort(self):
        '''Implements insert sort, a not very efficient way of sorting a list'''
        x = 0
        y = 1
        myindex = 0
        mylist = self.mylist
        assert type(mylist) == list
        for i in range(0,len(mylist)):
            while x < len(mylist) and y < len(mylist):
                if mylist[x] > mylist[y]:
                    myindex = y
                    mylist.insert(y+1,mylist[x])
                    mylist.remove(mylist[x])
                x = x+1
                y = y+1
            x = 0
            y = 1
            myindex = 0
            sorted_list = mylist
        return sorted_list
    def merge_sort(self):
        '''Implements merge sort, a common and efficient sorting algorithm'''
        startlist = self.mylist
        assert type(startlist) == list
        mylist = list()
        sublist = list()
        for i in startlist:
            sublist.append(i)
            mylist.append(sublist)
            sublist = list()
        sublist1 = list()
        sublist2 = list()
        newlist = list()
        sublist1 = mylist[0]
        sublist2 = mylist[1]
        while len(mylist) >1:
            if sublist1 == [] and sublist2 == []:
                mylist.remove([])
                mylist.remove([])
                mylist.append(newlist)
                if len(mylist) >= 2:
                    newlist = list()
                    sublist1 = mylist[0]
                    sublist2 = mylist[1]
            elif sublist1 == [] and sublist2 != []:
                newlist.append(sublist2[0])
                sublist2.remove(sublist2[0])
            elif sublist2 == [] and sublist1 != []:
                newlist.append(sublist1[0])
                sublist1.remove(sublist1[0])        
            elif sublist1[0] >= sublist2[0]:
                newlist.append(sublist2[0])
                sublist2.remove(sublist2[0])
            elif sublist1[0] < sublist2[0]:
                newlist.append(sublist1[0])
                sublist1.remove(sublist1[0])
        return newlist
