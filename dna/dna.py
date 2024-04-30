from cs50 import get_int, get_string, get_float
import csv
from sys import argv, exit

db_arg = argv[1]
sq_arg = argv[2]
# the main function only call the others function that contend the logical
def main():
    input_validation()
    sequence = add_sequence()
    db, key = add_db()
    STRs = count_STRs(key,sequence)
    compare(STRs, db)

# Validate user input comand-line
def input_validation():
    if len(argv) != 3:
        print("please entre correct usage 3")
        return exit(1)
# add the sequence .txt in a list and return itself
def add_sequence():
    with open(sq_arg, "r") as file:
        seq_path = list(file)
        return seq_path
# add sequence of data base of SRT in a list of dict and return itself
# and return the fieldnames, of SRTs names to compare and return itself
def add_db():
    with open(db_arg, "r") as file:
        reader = csv.DictReader(file)
        db_path = list(reader)
        keylist = reader.fieldnames
        keylist.remove("name")
        return db_path , keylist

# count the run of STRs in a sequence, and return a dictionary key-values to be compared
# this part "while sequence[(i + pos):(i + pos + len(strs))] == str" was hard for me understand first, coming from C where everything must be specified or iterated. basically you sellect the start and the end, a
# list have postions, list[position], what it does is "list[start : end] == x", where will get this part of the list and compare with x 
def count_STRs(keylist, sequence):
    #convert the sequence to a string
    sequence = "".join(sequence)
    max_found = {}
    for key in range(len(keylist)):
        strs = keylist[key]
        max_found[strs] = 0
        for i in range (len(sequence)):
            if sequence[i: i + len(strs)] == strs:
                pos = 0
                STR_count = 0
                while sequence[(i + pos):(i + pos + len(strs))] == strs:
                    STR_count +=1
                    pos += len(strs)
                if STR_count > int(max_found[strs]):
                    max_found[strs] = str(STR_count)
    return max_found

#this function compare two dicts specific keys
# this "keys" assign  the selected keys, this way i can compare the key values excluding the name field
# according the presented problem, this only can return one name, of more SRTs matches would be found, the code will need be changed
def compare(STRs, db):
    count = 0
    keys = STRs.keys()
    for i in range(len(db)):
        count = 0
        for key in keys:
            if STRs.get(key) == db[i].get(key):
                count += 1
        if count == len(keys):
            print(db[i]["name"])
            break
    if count != len(keys):
        print("No match")

main()
