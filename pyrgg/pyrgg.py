import random
import os
import time
def get_input():
    '''
    This function get input from user and return as dictionary
    :return: inputs as dictionary
    '''
    try:
        file_name=input("File Name : ")
        if file_name+".gr" in os.listdir():
            raise Exception("There is file with this name")
        vertices=int(input("Vertices Number : "))
        max_weight=int(input("Max Weight : "))
        min_weight = int(input("Min Weight : "))
        return {"file_name":file_name,"vertices":vertices,"max_weight":max_weight,"min_weight":min_weight}
    except Exception as e:
        print(e)


def branch_gen(random_edge,vertices_number,min_range,max_range):
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
        random_tail = random.randint(1, vertices_number + 1)
        random_weight=random.randint(min_range,max_range)
        if random_tail not in branch_list:
            branch_list.append(random_tail)
            weight_list.append(random_weight)
            index += 1
            print(index)
    return [branch_list,weight_list]
def edge_gen(vertices_number,min_range,max_range):
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
    for i in vertices_id:
        random_edge=random.randint(0,vertices_number)
        temp_list=branch_gen(random_edge,vertices_number,min_range,max_range)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp=temp+random_edge
    return [dict(zip(vertices_id,vertices_edge)),dict(zip(vertices_id,weight_list)),temp]
def file_init(file,file_name,min_range,max_range,vertices,edge):
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
    file.write("p sp "+str(vertices)+" "+str(edge)+"\n")

def file_maker(file_name,min_range,max_range,vertices):
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
    :return: None
    '''
    try:
        file=open(file_name+".gr","w")
        dicts=edge_gen(vertices,min_range,max_range)
        edge_dic=dicts[0]
        weight_dic=dicts[1]
        edge_number=dicts[2]
        file_init(file,file_name,min_range,max_range,vertices,edge_number)
        for i in edge_dic.keys():
            for j,value in enumerate(edge_dic[i]):
                file.write("c "+str(i)+" "+str(value)+" "+str(weight_dic[i][j])+"\n")
        file.close()
    except Exception as e:
        print("Error In File Creation")
        if file.closed()==False:
            file.close()
if __name__=="__main__":
    first_time=time.perf_counter()
    input_dict=get_input()
    file_maker(input_dict["file_name"],input_dict["min_weight"],input_dict["max_weight"],input_dict["vertices"])
    second_time=time.perf_counter()
    print("Graph Generated In "+str(second_time-first_time)+" sec")








