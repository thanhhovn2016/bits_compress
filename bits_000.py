numbers = [0, 1, 2, 3, 6, 9]
#print(numbers[5])
five_predict_high = 1
five_predict_low = 0 
#My_Dict = {1: 0, 2: 1, 3: 2, 4: 3 + five_predict_low, 5: 3 + 1 + five_predict_low, 6: 3 + 2 + five_predict_low, 7: numbers[4], 8: numbers[4] + 1 + five_predict_low, 9: numbers[4] + 2 + five_predict_low}
#My_Dict_h = {"A" : My_Dict[1] + numbers[5], "B": My_Dict[2] + numbers[5] , "C": My_Dict[3] + numbers[5], "D": My_Dict[4] + numbers[5], "E": My_Dict[5] + numbers[5], "F": My_Dict[6] + numbers[5], "G": My_Dict[7] + numbers[5], "H": My_Dict[8] + numbers[5], 17: My_Dict[9] + numbers[5]}

My_Dict = {1: 1, 2: 2, 3: 3 + five_predict_low, 4: 3 + 1 + five_predict_low, 5: 3 + 2 + five_predict_low, 6: numbers[4], 7: numbers[4] + 1 + five_predict_low, 8: numbers[4] + 2 + five_predict_low}
My_Dict_h = {9 : My_Dict[1] + numbers[5], "A": My_Dict[2] + numbers[5] , "B": My_Dict[3] + numbers[5], "C": My_Dict[4] + numbers[5], "D": My_Dict[5] + numbers[5], "E": My_Dict[6] + numbers[5], "F": My_Dict[7] + numbers[5], "G": My_Dict[8] + numbers[5]}


print("Check my dict")
#print(My_Dict[5]) 
#print(numbers[5])

print(My_Dict[1])
print(My_Dict[2])
print(My_Dict[3])
print(My_Dict[4])
print(My_Dict[5])
print(My_Dict[6])
print(My_Dict[7])
print(My_Dict[8])

print("---*---")
print(My_Dict_h[9])
print(My_Dict_h["A"])
print(My_Dict_h["B"])
print(My_Dict_h["C"])
print(My_Dict_h["D"])
print(My_Dict_h["E"])
print(My_Dict_h["F"])
print(My_Dict_h["G"])

#hexagon
#My_hex = {1: "0",2: "1",3: "10",4: "11",5: "100" ,6: "101",7: "110",8: "111"}
My_hex = {"st": "1", "match":"11" ,"end":"111" ,2: "10",3: "100",4: "110",5: "1000" ,6: "1010",7: "1100",8: "1110"}

#test_var = {"C": 12,"G" : 16, 0 : "Z"}
test_var = {"C": 12, "G" : 16}
lookup_str = {0: "C",1: "A"}
print(lookup_str[0])
print(My_Dict_h[lookup_str[0]])
firstchar = int(My_Dict_h[lookup_str[0]])
strout = ""
hidebit = 0

for firstchar in test_var:
    print(firstchar)
    
for firstchar in test_var:
    print(firstchar)
    if(firstchar == "C"):
        #print(My_Dict_h[firstchar])
        firstchar = 13

    if(firstchar == "G"):
        print(My_Dict_h[firstchar])
        firstchar = 17

    if(int(firstchar) == 0):
        strout += str("0")

    if(int(firstchar) == 9):
        strout += str("1")
        

    if(int(firstchar) <9):
        strout += str(int(firstchar))

    if(int(firstchar) >9):
        hidebit = 1
        result_sub = int(firstchar) - 9
        print("sub:")
        print(result_sub)
        strout += "1" + str(result_sub)

#print("***-***")
#print(lookup_str[1])
#print(My_Dict_h[lookup_str[1]])

print("###'###")
print(strout)

bitstr = ""
for element in strout:
    print(element)
#    if(int(element) == 0):
#        #pass
#        print("0uk")
#
    if(int(element) == 1):
        print("9th")

    if(int(element) == 4):
        print(My_hex[int(element)])
        bitstr += "1"
        bitstr += My_hex[int(element)]
        bitstr += "111"

    if(int(element) == 8):
        print(My_hex[int(element)])
        bitstr += "1"
        bitstr += My_hex[int(element)]
        bitstr += "111"

print(bitstr)
