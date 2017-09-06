import random
import os
import datetime
import sys
import yaml
import json
import pickle

Source_dir=os.getcwd()
#random_system=random.SystemRandom()
random_system=random

def convert_bytes(num):
    """
    convert num to idiomatic byte unit
    :param num: the input number.
    :type num:int
    :return: str
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
def filesize(fileaddr):
    '''
    This function calculate output file size
    :param fileaddr: file addresses
    :type fileaddr:str
    :return: file size for print as string
    '''
    file_info=os.stat(fileaddr)
    file_size= file_info.st_size
    print("Graph File Size : "+convert_bytes(file_size))

def logger(vertices_number,edge_number,file_name,elapsed_time):
    '''
    This function save generated graphs log
    :param vertices_number: nubmer of vertices
    :type vertices_number:int
    :param edge_number: Number of edges
    :type edge_number:int;
    :param file_name:  File Name
    :type file_name:str
    :param elapsed_time: Elapsed Time
     :type elapsed_time : str
    :return:  None
    '''
    try:
        file = open("logfile.log", "a")
        file.write(str(datetime.datetime.now())+"\n")
        file.write("Filename : "+file_name+"\n")
        file.write("Vertices : "+str(vertices_number)+"\n")
        file.write("Edges : "+str(edge_number)+"\n")
        file.write("Elapsed Time : " + str(elapsed_time) + "\n")
        file.write("-------------------------------\n")
        file.close()
    except Exception:
        print("[Error] Logger Faild!")

def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    >>> zero_insert("22")
    >>> '22'
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string

def time_convert(input_string):
    '''
    This function convert input_string from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=float(input_string)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"


def get_input(input_func=input):
    '''
    This function get input from user and return as dictionary
    :return: inputs as dictionary
    '''
    try:
        file_name=input_func("File Name : ")
        if file_name+".gr" in os.listdir():
            raise Exception("There is file with this name")
        vertices=int(input_func("Vertices Number : "))
        max_weight=int(input_func("Max Weight : "))
        min_weight = int(input_func("Min Weight : "))
        min_edge=int(input_func("Min Edge Number :"))
        min_edge=max(0,min_edge)
        max_edge=int(input_func("Max Edge Number :"))
        max_edge=min(max_edge,vertices)
        sign_flag=int(input_func("Signed[1] or Unsigned[2]"))
        output_format=int(input_func("Graph Format : \nDIMACS(.gr)[1] | JSON(.json)[2] | CSV(.csv)[3] | YAML(.yaml)[4]\n| WEL(.wel)[5] | ASP(.lp)[6] | Pickle(.p)[7] | UCINET DL Format(.dl)[8] | TGF(.tgf)[9]"))
        if sign_flag not in [1,2]:
            sign_flag=2
        if output_format not in list(range(1,10)):
            output_format=1
        return {"file_name":file_name,"vertices":vertices,"max_weight":max_weight,"min_weight":min_weight,"min_edge":min_edge,"max_edge":max_edge,"sign":sign_flag,"output_format":output_format}
    except Exception:
        print("[Error] Bad Input!")
        sys.exit()

def sign_gen():
    '''
    This function return random sign
    :return: 1 or -1
    '''
    flag=random_system.randint(0,1)
    if flag==0:
        return 1
    else:
        return -1
def branch_gen(random_edge,vertices_number,min_range,max_range,sign):
    '''
    This function generate branch and weight vector of each vertex
    :param random_edge: number of vertex edges
    :type random_edge:int
    :param vertices_number: number of vertices
    :type vertices_number:int
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max range
    :type max_range:int
    :return: branch and weight list
    '''
    index = 0
    branch_list = []
    weight_list=[]
    while (index < random_edge):
        random_tail = random_system.randint(1, vertices_number + 1)
        if sign==2:
            random_weight=random_system.randint(min_range,max_range)
        else:
            random_weight = sign_gen() * random_system.randint(min_range, max_range)
        if random_tail not in branch_list:
            branch_list.append(random_tail)
            weight_list.append(random_weight)
            index += 1
    return [branch_list,weight_list]
def edge_gen(vertices_number,min_range,max_range,min_edge,max_edge,sign):
    '''
    This function generate each vertex connection number
    :param vertices_number: number of vertices
    :type vertices_number:int
    :param min_range: weight min_range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :return: list of 2 dictionary
    '''
    temp=0
    vertices_id=list(range(1,vertices_number+1))
    vertices_edge=[]
    weight_list=[]
    i=0
    while(i<len(vertices_id)):
        i+=1
        random_edge=random_system.randint(min_edge,max_edge)
        temp_list=branch_gen(random_edge,vertices_number,min_range,max_range,sign)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp=temp+random_edge
    return [dict(zip(vertices_id,vertices_edge)),dict(zip(vertices_id,weight_list)),temp]


def file_init(file,file_name,min_range,max_range,vertices,edge,min_edge,max_edge):
    '''
    This function initial output file
    :param file: output file object
    :param file_name: file name
    :type file_name:str
    :type file:file_object
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max range
    :type max_range:int
    :param vertices: vertices number
    :type vertices:int
    :param edge:  edge number
    :type edge:int
    :return: None
    '''
    file.write("c FILE                  :"+file_name+".gr"+"\n")
    file.write("c No. of vertices       :"+str(vertices)+"\n")
    file.write("c No. of directed edges :"+str(edge)+"\n")
    file.write("c Max. weight           :"+str(max_range)+"\n")
    file.write("c Min. weight           :"+str(min_range)+"\n")
    file.write("c Min. edge           :" + str(min_edge) + "\n")
    file.write("c Max. edge           :" + str(max_edge) + "\n")
    file.write("p sp "+str(vertices)+" "+str(edge)+"\n")

def dimacs_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
    This function create output file and fill in
    :param file_name: file name
    :type file_name:str
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :param vertices: number of vertices
    :type vertices:int
    :param sign: weight sign flag
    :type sign: int
    :return: edge_number
    '''
    file=open(file_name+".gr","w")
    dicts=edge_gen(vertices,min_range,max_range,min_edge,max_edge,sign)
    edge_dic=dicts[0]
    weight_dic=dicts[1]
    edge_number=dicts[2]
    file_init(file,file_name,min_range,max_range,vertices,edge_number,min_edge,max_edge)
    for i in edge_dic.keys():
        for j,value in enumerate(edge_dic[i]):
            file.write("a "+str(i)+" "+str(value)+" "+str(weight_dic[i][j])+"\n")
    file.close()
    return edge_number

def json_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
    This function create output file in json format
    :param file_name: file name
    :type file_name:str
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :param vertices: number of vertices
    :type vertices:int
    :param sign: weight sign flag
    :type sign: int
    :return: edge_number
    '''
    file = open(file_name + ".json", "w")
    dicts = edge_gen(vertices, min_range, max_range, min_edge, max_edge, sign)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes='\t\t\t"nodes":[\n'
    edges='\t\t\t"edges":[\n'
    for i in edge_dic.keys():
        nodes=nodes+'\t\t\t{\n\t\t\t\t'+'"id": '+'"'+str(i)+'"\n\t\t\t},\n'
        for j,value in enumerate(edge_dic[i]):
            edges=edges+'\t\t\t{\n\t\t\t\t"source": '+'"'+str(i)+'",\n\t\t\t\t'+'"target": '+'"'+str(value)+'",\n\t\t\t\t'+'"weight": '+'"'+str(weight_dic[i][j])+'"\n\t\t\t},\n'
    nodes=nodes[:-2]+"\n\t\t],\n"
    edges=edges[:-2]+"\n\t\t]\n\t}\n}"
    file.write('{\n\t"graph": {\n')
    file.write(nodes)
    file.write(edges)
    file.close()
    return edge_number
def csv_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
       This function create output file in csv format
       :param file_name: file name
       :type file_name:str
       :param min_range: weight min range
       :type min_range:int
       :param max_range: weight max_range
       :type max_range:int
       :param vertices: number of vertices
       :type vertices:int
       :param sign: weight sign flag
       :type sign: int
       :return: edge_number
    '''
    file=open(file_name+".csv","w")
    dicts=edge_gen(vertices,min_range,max_range,min_edge,max_edge,sign)
    edge_dic=dicts[0]
    weight_dic=dicts[1]
    edge_number=dicts[2]
    for i in edge_dic.keys():
        for j,value in enumerate(edge_dic[i]):
            file.write(str(i)+","+str(value)+","+str(weight_dic[i][j])+"\n")
    file.close()
    return edge_number

def json_to_yaml(filename):
    '''
    This function convert json file to yaml file
    :param filename: filename
    :type filename: str
    :return: None
    '''
    try:
        file=open(filename+".json","r")
        json_data=json.loads(file.read())
        yaml_file = open(filename + ".yaml", "w")
        yaml.safe_dump(json_data,yaml_file,default_flow_style=False)
        file.close()
        yaml_file.close()
    except FileNotFoundError:
        print("[Error] Bad Input File")


def json_to_pickle(filename):
    '''
    This function convert json file to yaml file
    :param filename: filename
    :type filename: str
    :return: None
    '''
    try:
        file=open(filename+".json","r")
        pickle_file=open(filename+".p","wb")
        json_data=json.loads(file.read())
        pickle.dump(json_data,pickle_file)
        pickle_file.close()
        file.close()
    except FileNotFoundError:
        print("[Error] Bad Input File")


def wel_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
       This function create output file in wel format
       :param file_name: file name
       :type file_name:str
       :param min_range: weight min range
       :type min_range:int
       :param max_range: weight max_range
       :type max_range:int
       :param vertices: number of vertices
       :type vertices:int
       :param sign: weight sign flag
       :type sign: int
       :return: edge_number
    '''
    file=open(file_name+".wel","w")
    dicts=edge_gen(vertices,min_range,max_range,min_edge,max_edge,sign)
    edge_dic=dicts[0]
    weight_dic=dicts[1]
    edge_number=dicts[2]
    for i in edge_dic.keys():
        for j,value in enumerate(edge_dic[i]):
            file.write(str(i)+" "+str(value)+" "+str(weight_dic[i][j])+"\n")
    file.close()
    return edge_number

def lp_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
    This function create output file in ASP format
    :param file_name: file name
    :type file_name:str
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :param vertices: number of vertices
    :type vertices:int
    :param sign: weight sign flag
    :type sign: int
    :return: edge_number
    '''
    file = open(file_name + ".lp", "w")
    dicts = edge_gen(vertices, min_range, max_range, min_edge, max_edge, sign)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes=''
    edges=''
    for i in edge_dic.keys():
        nodes=nodes+'node('+str(i)+").\n"
        for j,value in enumerate(edge_dic[i]):
            edges=edges+'edge('+str(i)+","+str(value)+","+str(weight_dic[i][j])+").\n"
    file.write(nodes)
    file.write(edges)
    file.close()
    return edge_number
def tgf_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
    This function create output file in Trivial Graph Format
    :param file_name: file name
    :type file_name:str
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :param vertices: number of vertices
    :type vertices:int
    :param sign: weight sign flag
    :type sign: int
    :return: edge_number
    '''
    file = open(file_name + ".tgf", "w")
    dicts = edge_gen(vertices, min_range, max_range, min_edge, max_edge, sign)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes=''
    edges=''
    for i in edge_dic.keys():
        nodes=nodes+str(i)+"\n"
        for j,value in enumerate(edge_dic[i]):
            edges=edges+str(i)+" "+str(value)+" "+str(weight_dic[i][j])+"\n"
    file.write(nodes)
    file.write("#\n")
    file.write(edges)
    file.close()
    return edge_number
def dl_maker(file_name,min_range,max_range,vertices,min_edge,max_edge,sign):
    '''
    This function create output file in UCINET DL Format
    :param file_name: file name
    :type file_name:str
    :param min_range: weight min range
    :type min_range:int
    :param max_range: weight max_range
    :type max_range:int
    :param vertices: number of vertices
    :type vertices:int
    :param sign: weight sign flag
    :type sign: int
    :return: edge_number
    '''
    file = open(file_name + ".dl", "w")
    dicts = edge_gen(vertices, min_range, max_range, min_edge, max_edge, sign)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    edges=''
    for i in edge_dic.keys():
        for j,value in enumerate(edge_dic[i]):
            edges=edges+str(i)+" "+str(value)+" "+str(weight_dic[i][j])+"\n"
    file.write("dl\nformat=edgelist1\nn="+str(vertices)+"\ndata:\n")
    file.write(edges)
    file.close()
    return edge_number
def print_test(a):
    '''
    This function added for get_input parameter injection testing
    :param a: input
    :type a:int
    :return: static "2"
    '''
    return "2"










