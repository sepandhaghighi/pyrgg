# -*- coding: utf-8 -*-
"""Pyrgg params."""
import os

MENU_ITEMS1 = {
    "file_name": "File Name : ",
    "output_format": "Graph Format : \nDIMACS(.gr)[1] | JSON(.json)[2] | CSV(.csv)[3] | YAML(.yaml)[4]\n| WEL(.wel)[5] | ASP(.lp)[6] | Pickle(.p)[7] | UCINET DL Format(.dl)[8] | TGF(.tgf)[9]"}

MENU_ITEMS2 = {"vertices": "Vertices Number : ",
               "max_weight": "Max Weight : ",
               "min_weight": "Min Weight : ",
               "min_edge": "Min Edge Number :",
               "max_edge": "Max Edge Number :",
               "sign": "Signed[1] or Unsigned[2]"}




SUFFIX_MENU = {1:".gr",2:".json",3:".csv",4:".yaml",5:".wel",6:".lp",7:".p",8:".dl",9:".tgf"}


PYRGG_VERSION = "0.2"

SOURCE_DIR = os.getcwd()