import sys
import json
import logging



def str_opr (str_val):
    return str_val[::-1]

def int_opr(int_val):
    return int_val*int_val

def lis_opr(list_val):
    tmp_lst=[]
    for i in  list_val:
        if(type(i)==int):
            tmp_lst.append(int_opr(i))
        elif(type(i)==str):
            tmp_lst.append(str_opr(i))
        elif(type(i)==list):
            tmp_lst.append(lis_opr(i))

    return tmp_lst

def dic_opr(dic_val):
    temp_dict={}
    for k,v in dic_val.items():
            if(type(v) == str):
                temp_dict[k]=str_opr(v)
            elif(type(v)== int):
                temp_dict[k]=int_opr(v)
    return temp_dict


try:
    with open('problem_one.json', 'r') as json_file:
      
        dat=json.load(json_file)
            

            
except Exception as Arg:

    f_log=open("log_prob2.txt","a")
    f_log.write(str(Arg)+"\n")
    f_log.close
    if(str(Arg)=='list index out of range'):
        print("Please provide file path as argumnet")
    else:
        print("Please check input file")
    
    exit(0)



for key,val in dat.items():

    
    if(type(val) == str):
        dat[key]=str_opr(val)

    elif(type(val)== int):
        dat[key]=int_opr(val)

    elif(type(val)== list):
        dat[key]=lis_opr(val)

    elif(type(val)== dict):
        dat[key]=dic_opr(val)



with open("out_prob2.json",'w') as f_dump:
    json.dump(dat,f_dump,indent=5)
    print("Please check \\out_prob2.json for the output")
    






     
