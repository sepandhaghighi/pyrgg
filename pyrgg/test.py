
'''
This function get a string as input if input is one digit add a zero
:param input_string: input digit az string
:type input_string:str
:return: modified output as str
>>> from pyrgg import *
>>> import coverage
>>> import random
>>> import json
>>> import yaml
>>> import pickle
>>> cov = coverage.Coverage(omit=['*/home/travis/virtualenv/python3.5.3/lib/python3.5/site-packages/yaml/*'])
>>> cov.start()
>>> logger(100,50,"test","2min")
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> zero_insert("22")
'22'
>>> zero_insert("320")
'320'
>>> zero_insert("2")
'02'
>>> zero_insert(22)
Traceback (most recent call last):
        ...
TypeError: object of type 'int' has no len()
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert("15000")
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> time_convert("sadasdasd")
Traceback (most recent call last):
        ...
ValueError: could not convert string to float: 'sadasdasd'
>>> random.seed(2)
>>> sign_gen()
1
>>> random.seed(11)
>>> sign_gen()
-1
>>> random.seed(2)
>>> branch_gen(10,40,1,20,1)
[[4, 24, 17, 3, 41, 18, 25, 11, 15, 21], [3, 10, 20, 14, -17, 1, -17, 8, 6, 5]]
>>> random.seed(20)
>>> branch_gen(4,40,1,20,2)
[[10, 41, 21, 11], [9, 4, 19, 1]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1)
[{1: [3, 6], 2: [20, 6, 13, 15, 1], 3: [13, 6, 8, 11, 17, 18, 14], 4: [12, 13, 17, 9, 15, 19, 8], 5: [20, 16, 17, 7], 6: [20, 1, 4, 21, 19, 8, 14], 7: [12, 1, 3, 5, 6, 19, 11], 8: [15, 13, 8, 11, 19, 17], 9: [9, 14, 18, 2, 5, 4, 8], 10: [15, 3, 20, 14, 1], 11: [14, 17, 4, 6, 7, 15, 18, 19], 12: [19, 16, 17, 12, 14, 10, 1, 7, 15, 9], 13: [20, 13, 4], 14: [2, 12, 17, 14, 10, 6, 9, 3, 5], 15: [21, 10, 11], 16: [10, 18, 11, 17, 6, 8, 19, 15, 13, 9], 17: [21, 18, 3, 20, 13, 15, 6, 19], 18: [13, 19, 20], 19: [16, 19, 7, 1, 3, 11, 17, 13], 20: [2, 13, 10, 12]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, -263, 228, -303], 4: [-82, -335, 250, -256, -179, -249, -358], 5: [-395, -155, -159, -262], 6: [174, 381, 294, 139, 349, 30, 29], 7: [127, 58, 20, 376, 197, 126, -15], 8: [135, 242, 338, 12, -249, -73], 9: [-310, 358, 343, -17, 87, -325, 126], 10: [128, 319, -131, -269, 18], 11: [56, 123, 10, 53, 266, -158, -108, 214], 12: [48, -9, 312, -353, 53, 396, -30, 2, 385, 62], 13: [-328, 354, 316], 14: [-148, -72, -368, -348, -118, -305, -356, 36, -34], 15: [65, -118, -88], 16: [79, -49, 366, -86, -360, -183, 238, 304, 201, -129], 17: [-184, -365, 272, 206, 160, -332, 8, -110], 18: [140, 250, 4], 19: [-262, 239, 179, -272, -345, -136, -14, -345], 20: [255, -345, 5, 275]}, 123]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2)
[{1: [18, 15, 17, 7, 21, 6, 5, 20, 1], 2: [2, 7, 20], 3: [11, 19, 17, 21, 16, 3, 14, 9, 8], 4: [1, 19, 4, 13, 7, 16], 5: [14, 19, 7, 9, 3, 11, 4, 8], 6: [1, 15, 6], 7: [7, 17, 5, 21, 4, 14, 1, 19, 6, 20], 8: [2, 7, 9], 9: [10, 3, 19, 8, 20, 12, 15], 10: [19, 13, 21, 10, 20, 7, 14, 4, 2], 11: [8, 13, 14, 16, 17, 3], 12: [16, 21, 20, 9, 7], 13: [3, 14], 14: [2, 6, 12, 19, 3], 15: [15, 17, 5, 2], 16: [12, 10, 1, 21, 16, 5, 3, 18, 2], 17: [11, 3, 16, 14], 18: [19, 20, 13, 3, 21, 9, 11, 15, 18], 19: [17, 10, 3, 1, 4, 20, 16, 11, 15, 8], 20: [9, 21, 7, 13, 19, 5, 12, 3]}, {1: [99, 57, 75, 23, 78, 12, 11, 50, 67], 2: [4, 30, 3], 3: [56, 25, 29, 37, 0, 58, 70, 40, 65], 4: [8, 98, 51, 8, 6, 48], 5: [9, 80, 99, 43, 39, 1, 17, 90], 6: [7, 62, 87], 7: [57, 24, 53, 49, 50, 27, 34, 38, 50, 82], 8: [18, 56, 1], 9: [49, 9, 81, 1, 47, 79, 16], 10: [17, 23, 19, 29, 31, 20, 6, 13, 65], 11: [94, 32, 76, 37, 22, 16], 12: [71, 78, 9, 27, 95], 13: [34, 57], 14: [5, 36, 67, 16, 46], 15: [42, 74, 75, 2], 16: [89, 4, 76, 9, 8, 9, 57, 47, 94], 17: [45, 87, 9, 3], 18: [1, 84, 48, 11, 14, 53, 49, 59, 10], 19: [3, 76, 61, 29, 63, 84, 32, 84, 63, 41], 20: [25, 55, 27, 28, 40, 63, 5, 35]}, 129]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> dimacs_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.gr","r")
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of directed edges :7
c Max. weight           :200
c Min. weight           :0
c Min. edge           :0
c Max. edge           :2
p sp 10 7
a 4 3 -64
a 5 4 148
a 5 11 110
a 6 7 -139
a 6 8 -9
a 8 8 -97
a 9 9 143
<BLANKLINE>
>>> random.seed(4)
>>> dimacs_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.gr","r")
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :30
c No. of directed edges :41
c Max. weight           :50
c Min. weight           :0
c Min. edge           :0
c Max. edge           :4
p sp 30 41
a 1 10 46
a 2 16 5
a 2 3 25
a 2 18 -48
a 4 17 -17
a 5 27 16
a 6 31 41
a 7 26 -12
a 7 6 -18
a 8 3 -42
a 8 13 11
a 9 16 -5
a 10 27 0
a 10 30 -36
a 10 23 -48
a 10 17 26
a 11 20 -27
a 11 15 14
a 11 10 -2
a 14 21 -33
a 14 18 -44
a 14 11 43
a 15 3 -12
a 16 9 22
a 16 14 -40
a 16 18 20
a 19 9 7
a 20 30 18
a 20 15 2
a 21 23 18
a 21 24 -1
a 22 10 -9
a 22 25 -39
a 24 20 28
a 24 10 16
a 25 20 21
a 25 19 23
a 25 2 -10
a 26 26 -18
a 26 19 28
a 27 14 7
<BLANKLINE>
>>> random.seed(20)
>>> dimacs_maker("testfile3",10,30,100,0,4,2)
191
>>> file=open("testfile3.gr","r")
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of directed edges :191
c Max. weight           :30
c Min. weight           :10
c Min. edge           :0
c Max. edge           :4
p sp 100 191
a 1 34 30
a 3 74 15
a 3 4 23
a 4 10 13
a 4 17 20
a 4 61 28
a 5 53 16
a 5 26 20
a 5 81 20
a 6 55 12
a 6 81 26
a 7 52 12
a 7 27 28
a 7 32 11
a 8 13 12
a 9 33 19
a 10 89 18
a 10 21 29
a 13 91 17
a 13 29 28
a 14 8 10
a 15 39 18
a 15 18 30
a 15 43 29
a 15 93 24
a 16 82 18
a 17 56 15
a 17 22 22
a 17 91 13
a 17 89 14
a 18 55 21
a 18 29 13
a 18 78 11
a 18 67 16
a 19 23 15
a 19 11 13
a 19 101 19
a 21 87 22
a 21 59 26
a 23 16 24
a 24 43 10
a 24 10 28
a 24 96 13
a 24 12 20
a 25 83 12
a 25 85 19
a 28 29 26
a 29 90 10
a 29 21 10
a 29 86 26
a 29 18 19
a 30 54 18
a 32 13 16
a 32 31 16
a 32 29 13
a 33 17 27
a 33 50 14
a 35 63 10
a 35 23 16
a 35 82 19
a 36 13 19
a 36 27 21
a 36 80 19
a 37 87 13
a 39 8 22
a 39 48 19
a 40 60 13
a 40 9 28
a 40 61 16
a 42 9 27
a 42 80 20
a 42 92 10
a 42 23 18
a 43 78 13
a 43 1 11
a 44 96 16
a 45 52 29
a 45 11 28
a 45 47 19
a 45 57 11
a 46 80 22
a 47 51 22
a 47 33 10
a 47 100 24
a 47 12 28
a 48 41 17
a 48 100 16
a 48 38 24
a 49 49 16
a 49 80 11
a 50 18 12
a 50 96 21
a 53 31 27
a 53 19 19
a 53 100 10
a 54 88 21
a 55 68 14
a 55 3 17
a 56 68 24
a 56 32 22
a 56 50 27
a 57 65 29
a 57 84 19
a 58 98 12
a 58 84 25
a 58 35 21
a 58 95 14
a 59 85 17
a 59 63 14
a 59 46 20
a 60 19 30
a 60 96 27
a 60 97 13
a 60 83 11
a 61 25 21
a 61 51 16
a 61 70 26
a 61 91 19
a 62 81 15
a 62 18 14
a 62 36 10
a 63 86 12
a 63 100 15
a 63 44 18
a 63 32 20
a 65 34 18
a 67 39 12
a 68 6 26
a 68 61 22
a 68 92 26
a 70 91 19
a 71 71 23
a 71 22 24
a 71 57 26
a 71 62 14
a 72 25 16
a 73 16 16
a 73 58 22
a 74 9 19
a 74 82 27
a 74 15 16
a 75 94 19
a 76 65 19
a 77 61 13
a 77 47 26
a 77 32 15
a 78 74 21
a 78 38 14
a 78 2 20
a 78 49 14
a 79 66 14
a 79 23 29
a 80 67 11
a 80 15 18
a 80 54 28
a 80 12 27
a 81 78 24
a 82 53 11
a 82 92 15
a 82 23 13
a 83 91 29
a 83 73 30
a 83 39 15
a 84 36 17
a 87 89 27
a 87 76 24
a 87 56 20
a 87 101 17
a 88 94 15
a 88 66 11
a 88 58 12
a 88 65 10
a 89 4 18
a 89 99 21
a 90 40 27
a 90 52 30
a 92 2 11
a 92 74 15
a 93 30 30
a 95 54 11
a 95 1 29
a 95 97 16
a 96 70 27
a 96 60 12
a 96 37 24
a 97 38 20
a 97 14 24
a 97 25 14
a 97 80 30
a 100 24 16
a 100 38 10
<BLANKLINE>
>>> dimacs_maker("testfile", 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> json_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.json","r")
>>> testfile_1=json.load(file)
>>> testfile_1["graph"]["nodes"][1]
{'id': '2'}
>>> testfile_1["graph"]["edges"][1]["source"]
'5'
>>> testfile_1["graph"]["edges"][1]["target"]
'4'
>>> testfile_1["graph"]["edges"][1]["weight"]
'148'
>>> json_to_yaml("testfile")
>>> file=open("testfile.yaml","r")
>>> testfile_1_yaml=yaml.load(file)
>>> testfile_1_yaml["graph"]["edges"][1]["source"]
'5'
>>> testfile_1_yaml["graph"]["edges"][1]["target"]
'4'
>>> testfile_1_yaml["graph"]["edges"][1]["weight"]
'148'
>>> json_to_pickle("testfile")
>>> testfile_1_p=pickle.load( open( "testfile.p", "rb" ) )
>>> testfile_1_p["graph"]["edges"][1]["source"]
'5'
>>> testfile_1_p["graph"]["edges"][1]["target"]
'4'
>>> testfile_1_p["graph"]["edges"][1]["weight"]
'148'
>>> random.seed(4)
>>> json_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.json","r")
>>> testfile_2=json.load(file)
>>> testfile_2["graph"]["nodes"][1]
{'id': '2'}
>>> testfile_2["graph"]["edges"][1]["source"]
'2'
>>> testfile_2["graph"]["edges"][1]["target"]
'16'
>>> testfile_2["graph"]["edges"][1]["weight"]
'5'
>>> json_to_yaml("testfile2")
>>> file=open("testfile2.yaml","r")
>>> testfile_2_yaml=yaml.load(file)
>>> testfile_2_yaml["graph"]["nodes"][1]
{'id': '2'}
>>> testfile_2_yaml["graph"]["edges"][1]["source"]
'2'
>>> testfile_2_yaml["graph"]["edges"][1]["target"]
'16'
>>> testfile_2_yaml["graph"]["edges"][1]["weight"]
'5'
>>> json_to_pickle("testfile2")
>>> testfile_2_p=pickle.load( open( "testfile2.p", "rb" ) )
>>> testfile_2_p["graph"]["edges"][1]["source"]
'2'
>>> testfile_2_p["graph"]["edges"][1]["target"]
'16'
>>> testfile_2_p["graph"]["edges"][1]["weight"]
'5'
>>> random.seed(20)
>>> json_maker("testfile3",10,30,100,0,4,2)
191
>>> file=open("testfile3.json","r")
>>> testfile_3=json.load(file)
>>> testfile_3["graph"]["nodes"][1]
{'id': '2'}
>>> testfile_3["graph"]["edges"][1]["source"]
'3'
>>> testfile_3["graph"]["edges"][1]["target"]
'74'
>>> testfile_3["graph"]["edges"][1]["weight"]
'15'
>>> json_to_yaml("testfile3")
>>> file=open("testfile3.yaml","r")
>>> testfile_3_yaml=yaml.load(file)
>>> testfile_3_yaml["graph"]["nodes"][1]
{'id': '2'}
>>> testfile_3_yaml["graph"]["edges"][1]["source"]
'3'
>>> testfile_3_yaml["graph"]["edges"][1]["target"]
'74'
>>> testfile_3_yaml["graph"]["edges"][1]["weight"]
'15'
>>> json_to_yaml("testfile24")
[Error] Bad Input File
>>> json_to_pickle("testfile24")
[Error] Bad Input File
>>> json_maker("testfile", 0, 200, 10, 0, 0)
Traceback (most recent call last):
        ...
TypeError: json_maker() missing 1 required positional argument: 'sign'
>>> json_to_pickle("testfile3")
>>> testfile_3_p=pickle.load( open( "testfile3.p", "rb" ) )
>>> testfile_3_p["graph"]["edges"][1]["source"]
'3'
>>> testfile_3_p["graph"]["edges"][1]["target"]
'74'
>>> testfile_3_p["graph"]["edges"][1]["weight"]
'15'
>>> random.seed(2)
>>> csv_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.csv","r")
>>> print(file.read())
4,3,-64
5,4,148
5,11,110
6,7,-139
6,8,-9
8,8,-97
9,9,143
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.csv","r")
>>> print(file.read())
1,10,46
2,16,5
2,3,25
2,18,-48
4,17,-17
5,27,16
6,31,41
7,26,-12
7,6,-18
8,3,-42
8,13,11
9,16,-5
10,27,0
10,30,-36
10,23,-48
10,17,26
11,20,-27
11,15,14
11,10,-2
14,21,-33
14,18,-44
14,11,43
15,3,-12
16,9,22
16,14,-40
16,18,20
19,9,7
20,30,18
20,15,2
21,23,18
21,24,-1
22,10,-9
22,25,-39
24,20,28
24,10,16
25,20,21
25,19,23
25,2,-10
26,26,-18
26,19,28
27,14,7
<BLANKLINE>
>>> random.seed(20)
>>> csv_maker("testfile3",10,30,100,0,4,2)
191
>>> file=open("testfile3.csv","r")
>>> print(file.read())
1,34,30
3,74,15
3,4,23
4,10,13
4,17,20
4,61,28
5,53,16
5,26,20
5,81,20
6,55,12
6,81,26
7,52,12
7,27,28
7,32,11
8,13,12
9,33,19
10,89,18
10,21,29
13,91,17
13,29,28
14,8,10
15,39,18
15,18,30
15,43,29
15,93,24
16,82,18
17,56,15
17,22,22
17,91,13
17,89,14
18,55,21
18,29,13
18,78,11
18,67,16
19,23,15
19,11,13
19,101,19
21,87,22
21,59,26
23,16,24
24,43,10
24,10,28
24,96,13
24,12,20
25,83,12
25,85,19
28,29,26
29,90,10
29,21,10
29,86,26
29,18,19
30,54,18
32,13,16
32,31,16
32,29,13
33,17,27
33,50,14
35,63,10
35,23,16
35,82,19
36,13,19
36,27,21
36,80,19
37,87,13
39,8,22
39,48,19
40,60,13
40,9,28
40,61,16
42,9,27
42,80,20
42,92,10
42,23,18
43,78,13
43,1,11
44,96,16
45,52,29
45,11,28
45,47,19
45,57,11
46,80,22
47,51,22
47,33,10
47,100,24
47,12,28
48,41,17
48,100,16
48,38,24
49,49,16
49,80,11
50,18,12
50,96,21
53,31,27
53,19,19
53,100,10
54,88,21
55,68,14
55,3,17
56,68,24
56,32,22
56,50,27
57,65,29
57,84,19
58,98,12
58,84,25
58,35,21
58,95,14
59,85,17
59,63,14
59,46,20
60,19,30
60,96,27
60,97,13
60,83,11
61,25,21
61,51,16
61,70,26
61,91,19
62,81,15
62,18,14
62,36,10
63,86,12
63,100,15
63,44,18
63,32,20
65,34,18
67,39,12
68,6,26
68,61,22
68,92,26
70,91,19
71,71,23
71,22,24
71,57,26
71,62,14
72,25,16
73,16,16
73,58,22
74,9,19
74,82,27
74,15,16
75,94,19
76,65,19
77,61,13
77,47,26
77,32,15
78,74,21
78,38,14
78,2,20
78,49,14
79,66,14
79,23,29
80,67,11
80,15,18
80,54,28
80,12,27
81,78,24
82,53,11
82,92,15
82,23,13
83,91,29
83,73,30
83,39,15
84,36,17
87,89,27
87,76,24
87,56,20
87,101,17
88,94,15
88,66,11
88,58,12
88,65,10
89,4,18
89,99,21
90,40,27
90,52,30
92,2,11
92,74,15
93,30,30
95,54,11
95,1,29
95,97,16
96,70,27
96,60,12
96,37,24
97,38,20
97,14,24
97,25,14
97,80,30
100,24,16
100,38,10
<BLANKLINE>
>>> csv_maker("testfile", 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> wel_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.wel","r")
>>> print(file.read())
4 3 -64
5 4 148
5 11 110
6 7 -139
6 8 -9
8 8 -97
9 9 143
<BLANKLINE>
>>> random.seed(4)
>>> wel_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.wel","r")
>>> print(file.read())
1 10 46
2 16 5
2 3 25
2 18 -48
4 17 -17
5 27 16
6 31 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> random.seed(20)
>>> wel_maker("testfile3",10,30,100,0,4,2)
191
>>> file=open("testfile3.wel","r")
>>> print(file.read())
1 34 30
3 74 15
3 4 23
4 10 13
4 17 20
4 61 28
5 53 16
5 26 20
5 81 20
6 55 12
6 81 26
7 52 12
7 27 28
7 32 11
8 13 12
9 33 19
10 89 18
10 21 29
13 91 17
13 29 28
14 8 10
15 39 18
15 18 30
15 43 29
15 93 24
16 82 18
17 56 15
17 22 22
17 91 13
17 89 14
18 55 21
18 29 13
18 78 11
18 67 16
19 23 15
19 11 13
19 101 19
21 87 22
21 59 26
23 16 24
24 43 10
24 10 28
24 96 13
24 12 20
25 83 12
25 85 19
28 29 26
29 90 10
29 21 10
29 86 26
29 18 19
30 54 18
32 13 16
32 31 16
32 29 13
33 17 27
33 50 14
35 63 10
35 23 16
35 82 19
36 13 19
36 27 21
36 80 19
37 87 13
39 8 22
39 48 19
40 60 13
40 9 28
40 61 16
42 9 27
42 80 20
42 92 10
42 23 18
43 78 13
43 1 11
44 96 16
45 52 29
45 11 28
45 47 19
45 57 11
46 80 22
47 51 22
47 33 10
47 100 24
47 12 28
48 41 17
48 100 16
48 38 24
49 49 16
49 80 11
50 18 12
50 96 21
53 31 27
53 19 19
53 100 10
54 88 21
55 68 14
55 3 17
56 68 24
56 32 22
56 50 27
57 65 29
57 84 19
58 98 12
58 84 25
58 35 21
58 95 14
59 85 17
59 63 14
59 46 20
60 19 30
60 96 27
60 97 13
60 83 11
61 25 21
61 51 16
61 70 26
61 91 19
62 81 15
62 18 14
62 36 10
63 86 12
63 100 15
63 44 18
63 32 20
65 34 18
67 39 12
68 6 26
68 61 22
68 92 26
70 91 19
71 71 23
71 22 24
71 57 26
71 62 14
72 25 16
73 16 16
73 58 22
74 9 19
74 82 27
74 15 16
75 94 19
76 65 19
77 61 13
77 47 26
77 32 15
78 74 21
78 38 14
78 2 20
78 49 14
79 66 14
79 23 29
80 67 11
80 15 18
80 54 28
80 12 27
81 78 24
82 53 11
82 92 15
82 23 13
83 91 29
83 73 30
83 39 15
84 36 17
87 89 27
87 76 24
87 56 20
87 101 17
88 94 15
88 66 11
88 58 12
88 65 10
89 4 18
89 99 21
90 40 27
90 52 30
92 2 11
92 74 15
93 30 30
95 54 11
95 1 29
95 97 16
96 70 27
96 60 12
96 37 24
97 38 20
97 14 24
97 25 14
97 80 30
100 24 16
100 38 10
<BLANKLINE>
>>> wel_maker("testfile", 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> lp_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.lp","r")
>>> print(file.read())
node(1).
node(2).
node(3).
node(4).
node(5).
node(6).
node(7).
node(8).
node(9).
node(10).
edge(4,3,-64).
edge(5,4,148).
edge(5,11,110).
edge(6,7,-139).
edge(6,8,-9).
edge(8,8,-97).
edge(9,9,143).
<BLANKLINE>
>>> random.seed(4)
>>> lp_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.lp","r")
>>> print(file.read())
node(1).
node(2).
node(3).
node(4).
node(5).
node(6).
node(7).
node(8).
node(9).
node(10).
node(11).
node(12).
node(13).
node(14).
node(15).
node(16).
node(17).
node(18).
node(19).
node(20).
node(21).
node(22).
node(23).
node(24).
node(25).
node(26).
node(27).
node(28).
node(29).
node(30).
edge(1,10,46).
edge(2,16,5).
edge(2,3,25).
edge(2,18,-48).
edge(4,17,-17).
edge(5,27,16).
edge(6,31,41).
edge(7,26,-12).
edge(7,6,-18).
edge(8,3,-42).
edge(8,13,11).
edge(9,16,-5).
edge(10,27,0).
edge(10,30,-36).
edge(10,23,-48).
edge(10,17,26).
edge(11,20,-27).
edge(11,15,14).
edge(11,10,-2).
edge(14,21,-33).
edge(14,18,-44).
edge(14,11,43).
edge(15,3,-12).
edge(16,9,22).
edge(16,14,-40).
edge(16,18,20).
edge(19,9,7).
edge(20,30,18).
edge(20,15,2).
edge(21,23,18).
edge(21,24,-1).
edge(22,10,-9).
edge(22,25,-39).
edge(24,20,28).
edge(24,10,16).
edge(25,20,21).
edge(25,19,23).
edge(25,2,-10).
edge(26,26,-18).
edge(26,19,28).
edge(27,14,7).
<BLANKLINE>
>>> input_dic=get_input(input_func=print_test)
>>> input_dic["sign"]
2
>>> input_dic['vertices']
2
>>> input_dic['min_edge']
2
>>> input_dic['min_weight']
2
>>> input_dic['output_format']
2
>>> input_dic['max_weight']
2
>>> input_dic['file_name']
'2'
>>> input_dic['max_edge']
2
>>> random.seed(2)
>>> tgf_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.tgf","r")
>>> print(file.read())
1
2
3
4
5
6
7
8
9
10
#
4 3 -64
5 4 148
5 11 110
6 7 -139
6 8 -9
8 8 -97
9 9 143
<BLANKLINE>
>>> random.seed(4)
>>> tgf_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.tgf","r")
>>> print(file.read())
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
#
1 10 46
2 16 5
2 3 25
2 18 -48
4 17 -17
5 27 16
6 31 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> random.seed(2)
>>> dl_maker("testfile", 0, 200, 10, 0, 2, 0)
7
>>> file=open("testfile.dl","r")
>>> print(file.read())
dl
format=edgelist1
n=10
data:
4 3 -64
5 4 148
5 11 110
6 7 -139
6 8 -9
8 8 -97
9 9 143
<BLANKLINE>
>>> random.seed(4)
>>> dl_maker("testfile2",0,50,30,0,4,0)
41
>>> file=open("testfile2.dl","r")
>>> print(file.read())
dl
format=edgelist1
n=30
data:
1 10 46
2 16 5
2 3 25
2 18 -48
4 17 -17
5 27 16
6 31 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> filesize("testfile.csv")
Graph File Size : 64.0 bytes
>>> filesize("testfile.dl")
Graph File Size : 99.0 bytes
>>> filesize("testfile.gr")
Graph File Size : 294.0 bytes
>>> filesize("testfile.json")
Graph File Size : 858.0 bytes
>>> filesize("testfile.lp")
Graph File Size : 214.0 bytes
>>> filesize("testfile.p")
Graph File Size : 421.0 bytes
>>> filesize("testfile.tgf")
Graph File Size : 98.0 bytes
>>> filesize("testfile.wel")
Graph File Size : 64.0 bytes
>>> filesize("testfile.yaml")
Graph File Size : 531.0 bytes
>>> filesize("testfile2.csv")
Graph File Size : 401.0 bytes
>>> filesize("testfile2.dl")
Graph File Size : 436.0 bytes
>>> filesize("testfile2.gr")
Graph File Size : 701.0 bytes
>>> filesize("testfile2.json")
Graph File Size : 3.9 KB
>>> filesize("testfile2.lp")
Graph File Size : 1009.0 bytes
>>> filesize("testfile2.p")
Graph File Size : 1.9 KB
>>> filesize("testfile2.tgf")
Graph File Size : 515.0 bytes
>>> filesize("testfile2.wel")
Graph File Size : 401.0 bytes
>>> filesize("testfile2.yaml")
Graph File Size : 2.6 KB
>>> filesize("testfile3.csv")
Graph File Size : 1.8 KB
>>> filesize("testfile3.gr")
Graph File Size : 2.4 KB
>>> filesize("testfile3.json")
Graph File Size : 16.8 KB
>>> filesize("testfile3.p")
Graph File Size : 10.8 KB
>>> filesize("testfile3.wel")
Graph File Size : 1.8 KB
>>> filesize("testfile3.yaml")
Graph File Size : 11.4 KB
>>> cov.stop()
>>> cov.save()

'''