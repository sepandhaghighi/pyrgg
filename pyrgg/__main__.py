from .pyrgg import *
import time
if __name__=="__main__":
    first_time=time.perf_counter()
    input_dict=get_input()
    file_name=input_dict["file_name"]
    min_weight=input_dict["min_weight"]
    max_weight=input_dict["max_weight"]
    vertices_number=input_dict["vertices"]
    min_edge=input_dict["min_edge"]
    max_edge=input_dict["max_edge"]
    sign=input_dict["sign"]
    edge_number=file_maker(file_name,min_weight,max_weight,vertices_number,min_edge,max_edge,sign)
    second_time=time.perf_counter()
    elapsed_time=second_time-first_time
    elapsed_time_format=time_convert(str(elapsed_time))
    print("Graph Generated In "+elapsed_time_format)
    print("Where --> "+Source_dir)
    logger(vertices_number,edge_number,file_name+".gr",elapsed_time_format)