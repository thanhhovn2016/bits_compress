numbers = [0, 1, 2, 3, 6, 9]
#print(numbers[5])
five_predict_high = 1
five_predict_low = 0 
#My_Dict = {1: 0, 2: 1, 3: 2, 4: 3 + five_predict_low, 5: 3 + 1 + five_predict_low, 6: 3 + 2 + five_predict_low, 7: numbers[4], 8: numbers[4] + 1 + five_predict_low, 9: numbers[4] + 2 + five_predict_low}
#My_Dict_h = {"A" : My_Dict[1] + numbers[5], "B": My_Dict[2] + numbers[5] , "C": My_Dict[3] + numbers[5], "D": My_Dict[4] + numbers[5], "E": My_Dict[5] + numbers[5], "F": My_Dict[6] + numbers[5], "G": My_Dict[7] + numbers[5], "H": My_Dict[8] + numbers[5], 17: My_Dict[9] + numbers[5]}

My_Dict = {1: 1, 2: 2, 3: 3 + five_predict_low, 4: 3 + 1 + five_predict_low, 5: 3 + 2 + five_predict_low, 6: numbers[4], 7: numbers[4] + 1 + five_predict_low, 8: numbers[4] + 2 + five_predict_low}
My_Dict_h = {9 : numbers[5], "A": My_Dict[1] + numbers[5] , "B": My_Dict[2] + numbers[5], "C": My_Dict[3] + numbers[5], "D": My_Dict[4] + numbers[5], "E": My_Dict[5] + numbers[5], "F": My_Dict[6] + numbers[5], "G": My_Dict[7] + numbers[5]}


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
#My_hex = {"st": "1", "match":"111" ,"end":"11" ,2: "10",3: "100",4: "110",5: "1000" ,6: "1010",7: "1100",8: "1110"}
#My_hex = {"end": "0","match":"000" ,1: "1",2: "11",3: "101",4: "111" ,5: "1001",6: "1011",7: "1101",8: "1111",0 : "1100",9: "1000"}

My_hex = {"end": "0","match":"000" ,0: "10000",1: "11",2: "101",3: "111" ,4: "1001",5: "1011",6: "1101",7: "1111",9: "100000"}

#test_var = {"C": 12,"G" : 16, 0 : "Z"}
#test_var = {"C": 12, "G" : 16}
test_var_key = ["0", "9", "A", "C", "D", "F"]
test_var_value = [9, 0, 10, 12, 13, 15]

#lookup_str = {0: 9,1: 0}
#print(lookup_str["0"])
#print(My_Dict_h[lookup_str["0"]])
#firstchar = int(My_Dict[lookup_str[0]])
strout = ""
hidebit = 0

print("***-***")
#print(My_hex[9])
#print(len(test_var_key))

for my_var in range(len(test_var_key)):
    print(test_var_key[my_var])

for firstchar in range(len(test_var_key)):
    print("'''")
    #strout += "0"
    print(test_var_value[firstchar] == 0)
    firstcharval = 0

    if(test_var_value[firstchar] == 9):
        #print(My_Dict_h[firstchar])
        firstcharval = 0

    if(test_var_value[firstchar] == 0):
        #print(My_Dict_h[firstchar])
        firstcharval = 9

    if(test_var_value[firstchar] == 10):
        #print(My_Dict_h[firstchar])
        firstcharval = 10

    if(test_var_value[firstchar] == 12):
        #print(My_Dict_h[firstchar])
        firstcharval = 12

    if(test_var_value[firstchar] == 13):
        #print(My_Dict_h[firstchar])
        firstcharval = 13

    if(test_var_value[firstchar] == 15):
        #print(My_Dict_h[firstchar])
        firstcharval = 15
    
    if(int(test_var_value[firstchar]) == 9):
        print("Found9")
        strout += str(My_hex[9])
        strout += "0"
        #strout += "000"

    if(int(test_var_value[firstchar]) == 0):
        print("Found0")
        strout += str(My_hex[0])
        strout += "0"
        #strout += "000"

    if((int(test_var_value[firstchar]) <9) & (int(test_var_value[firstchar]) !=0 )):
        strout += str(My_hex[int(firstcharval)])
        strout += "0"
        strout += "000"

    if(int(test_var_value[firstchar]) >9):
        hidebit = 1
        result_sub = int(test_var_value[firstchar]) - 9
        print("sub:")
        print(result_sub)
        strout += str(My_hex[result_sub])
        strout += "0"
        strout += "1000"
        
#print("***-***")
#print(lookup_str[1])
#print(My_Dict_h[lookup_str[1]])

print("###'###")
print(strout)

mystr = "1000000100000110100011101000100101000110101000"
#detect 9
try:
    result = mystr.index('1000')
    print(result)

    #idx_nine = result + 4
    #print(idx_nine)
    #print(mystr[idx_nine:(idx_nine + 1)])
    
    #char_nine = mystr[0:4]
    #if(char_nine == "1000"):
    #    print("9")

    #char_zero = mystr[(idx_nine + 4):(idx_nine + 7)]
    #if(char_zero == "110"):
    #    print("0")

except:
    print("Str Not found")