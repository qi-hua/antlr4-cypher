# Generated from CypherLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,99,792,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,2,105,7,105,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,
        3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,
        9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,
        16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,
        22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,
        37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,
        39,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,
        42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,
        44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,
        46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,
        49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,
        50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,
        52,1,52,1,52,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,55,1,
        55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,
        57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,
        59,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,
        62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,
        63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,1,66,1,67,1,67,1,
        67,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,70,1,
        70,1,70,1,70,1,70,1,70,1,71,1,71,1,71,1,71,1,71,1,72,1,72,1,72,1,
        72,1,72,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,73,1,
        74,1,74,1,74,1,75,1,75,1,75,1,75,1,76,1,76,1,76,1,76,1,76,1,76,1,
        76,1,76,1,77,1,77,1,77,1,77,1,77,1,77,1,77,1,78,1,78,1,78,1,78,1,
        78,1,79,1,79,1,79,1,79,1,79,1,80,1,80,1,80,1,80,1,80,1,81,1,81,1,
        81,1,81,1,81,1,82,1,82,1,82,1,82,1,83,1,83,1,83,1,83,1,83,1,83,1,
        83,1,83,1,83,1,83,1,84,1,84,1,84,1,84,1,84,1,84,1,84,1,85,1,85,1,
        85,1,86,1,86,1,86,1,86,1,87,1,87,1,87,1,87,1,87,1,88,4,88,626,8,
        88,11,88,12,88,627,1,89,1,89,5,89,632,8,89,10,89,12,89,635,9,89,
        1,89,1,89,1,90,1,90,1,90,3,90,642,8,90,1,90,1,90,1,91,1,91,1,91,
        5,91,649,8,91,10,91,12,91,652,9,91,1,91,1,91,1,92,3,92,657,8,92,
        1,92,1,92,1,92,1,92,3,92,663,8,92,1,93,1,93,1,93,1,93,1,93,1,93,
        3,93,671,8,93,1,93,3,93,674,8,93,1,93,3,93,677,8,93,1,93,1,93,1,
        93,3,93,682,8,93,1,93,3,93,685,8,93,3,93,687,8,93,1,94,4,94,690,
        8,94,11,94,12,94,691,1,94,1,94,1,95,1,95,1,95,1,95,5,95,700,8,95,
        10,95,12,95,703,9,95,1,95,1,95,1,95,1,95,1,95,1,96,1,96,1,96,1,96,
        5,96,714,8,96,10,96,12,96,717,9,96,1,96,1,96,1,97,1,97,1,97,1,97,
        1,98,1,98,1,98,1,98,3,98,729,8,98,1,98,3,98,732,8,98,1,98,1,98,1,
        98,4,98,737,8,98,11,98,12,98,738,1,98,1,98,1,98,1,98,1,98,3,98,746,
        8,98,1,99,1,99,3,99,750,8,99,1,99,1,99,1,100,1,100,1,100,1,100,1,
        100,1,100,5,100,760,8,100,10,100,12,100,763,9,100,1,100,3,100,766,
        8,100,1,101,1,101,1,102,1,102,1,102,1,103,1,103,5,103,775,8,103,
        10,103,12,103,778,9,103,1,103,3,103,781,8,103,1,104,1,104,3,104,
        785,8,104,1,105,1,105,1,105,1,105,3,105,791,8,105,2,633,701,0,106,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,
        49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,
        71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,
        93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,
        113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,
        66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,75,
        151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,167,84,169,
        85,171,86,173,87,175,88,177,89,179,90,181,91,183,92,185,93,187,94,
        189,95,191,96,193,97,195,98,197,0,199,0,201,0,203,0,205,0,207,0,
        209,0,211,99,1,0,41,2,0,67,67,99,99,2,0,65,65,97,97,2,0,76,76,108,
        108,2,0,89,89,121,121,2,0,73,73,105,105,2,0,69,69,101,101,2,0,68,
        68,100,100,2,0,70,70,102,102,2,0,84,84,116,116,2,0,82,82,114,114,
        2,0,88,88,120,120,2,0,79,79,111,111,2,0,85,85,117,117,2,0,78,78,
        110,110,2,0,83,83,115,115,2,0,71,71,103,103,2,0,66,66,98,98,2,0,
        72,72,104,104,2,0,77,77,109,109,2,0,80,80,112,112,2,0,86,86,118,
        118,2,0,75,75,107,107,2,0,87,87,119,119,2,0,81,81,113,113,4,0,10,
        10,13,13,39,39,92,92,4,0,10,10,13,13,34,34,92,92,4,0,68,68,70,70,
        100,100,102,102,3,0,9,10,12,13,32,32,2,0,10,10,13,13,13,0,34,34,
        39,39,66,66,70,70,78,78,82,82,84,84,92,92,98,98,102,102,110,110,
        114,114,116,116,1,0,48,51,1,0,48,55,2,0,43,43,45,45,3,0,48,57,65,
        70,97,102,1,0,49,57,2,0,48,57,95,95,1,0,48,57,3,0,65,90,95,95,97,
        122,2,0,0,127,55296,56319,1,0,55296,56319,1,0,56320,57343,817,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,
        0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,
        0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,
        0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,
        1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,
        0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,
        0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,
        129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,
        0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,
        1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,
        0,157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,
        0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,
        175,1,0,0,0,0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,
        0,0,0,185,1,0,0,0,0,187,1,0,0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,
        1,0,0,0,0,195,1,0,0,0,0,211,1,0,0,0,1,213,1,0,0,0,3,215,1,0,0,0,
        5,218,1,0,0,0,7,221,1,0,0,0,9,224,1,0,0,0,11,226,1,0,0,0,13,228,
        1,0,0,0,15,231,1,0,0,0,17,234,1,0,0,0,19,236,1,0,0,0,21,238,1,0,
        0,0,23,240,1,0,0,0,25,242,1,0,0,0,27,244,1,0,0,0,29,246,1,0,0,0,
        31,248,1,0,0,0,33,250,1,0,0,0,35,252,1,0,0,0,37,254,1,0,0,0,39,256,
        1,0,0,0,41,258,1,0,0,0,43,260,1,0,0,0,45,262,1,0,0,0,47,264,1,0,
        0,0,49,266,1,0,0,0,51,268,1,0,0,0,53,270,1,0,0,0,55,272,1,0,0,0,
        57,277,1,0,0,0,59,283,1,0,0,0,61,290,1,0,0,0,63,298,1,0,0,0,65,304,
        1,0,0,0,67,308,1,0,0,0,69,313,1,0,0,0,71,320,1,0,0,0,73,324,1,0,
        0,0,75,328,1,0,0,0,77,338,1,0,0,0,79,341,1,0,0,0,81,348,1,0,0,0,
        83,355,1,0,0,0,85,360,1,0,0,0,87,371,1,0,0,0,89,378,1,0,0,0,91,385,
        1,0,0,0,93,391,1,0,0,0,95,397,1,0,0,0,97,403,1,0,0,0,99,406,1,0,
        0,0,101,415,1,0,0,0,103,421,1,0,0,0,105,428,1,0,0,0,107,435,1,0,
        0,0,109,439,1,0,0,0,111,444,1,0,0,0,113,450,1,0,0,0,115,455,1,0,
        0,0,117,461,1,0,0,0,119,468,1,0,0,0,121,472,1,0,0,0,123,475,1,0,
        0,0,125,484,1,0,0,0,127,493,1,0,0,0,129,498,1,0,0,0,131,501,1,0,
        0,0,133,504,1,0,0,0,135,508,1,0,0,0,137,511,1,0,0,0,139,518,1,0,
        0,0,141,522,1,0,0,0,143,528,1,0,0,0,145,533,1,0,0,0,147,538,1,0,
        0,0,149,549,1,0,0,0,151,552,1,0,0,0,153,556,1,0,0,0,155,564,1,0,
        0,0,157,571,1,0,0,0,159,576,1,0,0,0,161,581,1,0,0,0,163,586,1,0,
        0,0,165,591,1,0,0,0,167,595,1,0,0,0,169,605,1,0,0,0,171,612,1,0,
        0,0,173,615,1,0,0,0,175,619,1,0,0,0,177,625,1,0,0,0,179,629,1,0,
        0,0,181,638,1,0,0,0,183,645,1,0,0,0,185,656,1,0,0,0,187,686,1,0,
        0,0,189,689,1,0,0,0,191,695,1,0,0,0,193,709,1,0,0,0,195,720,1,0,
        0,0,197,745,1,0,0,0,199,747,1,0,0,0,201,753,1,0,0,0,203,767,1,0,
        0,0,205,769,1,0,0,0,207,772,1,0,0,0,209,784,1,0,0,0,211,790,1,0,
        0,0,213,214,5,61,0,0,214,2,1,0,0,0,215,216,5,43,0,0,216,217,5,61,
        0,0,217,4,1,0,0,0,218,219,5,60,0,0,219,220,5,61,0,0,220,6,1,0,0,
        0,221,222,5,62,0,0,222,223,5,61,0,0,223,8,1,0,0,0,224,225,5,62,0,
        0,225,10,1,0,0,0,226,227,5,60,0,0,227,12,1,0,0,0,228,229,5,60,0,
        0,229,230,5,62,0,0,230,14,1,0,0,0,231,232,5,46,0,0,232,233,5,46,
        0,0,233,16,1,0,0,0,234,235,5,59,0,0,235,18,1,0,0,0,236,237,5,46,
        0,0,237,20,1,0,0,0,238,239,5,44,0,0,239,22,1,0,0,0,240,241,5,40,
        0,0,241,24,1,0,0,0,242,243,5,41,0,0,243,26,1,0,0,0,244,245,5,123,
        0,0,245,28,1,0,0,0,246,247,5,125,0,0,247,30,1,0,0,0,248,249,5,91,
        0,0,249,32,1,0,0,0,250,251,5,93,0,0,251,34,1,0,0,0,252,253,5,45,
        0,0,253,36,1,0,0,0,254,255,5,43,0,0,255,38,1,0,0,0,256,257,5,47,
        0,0,257,40,1,0,0,0,258,259,5,37,0,0,259,42,1,0,0,0,260,261,5,94,
        0,0,261,44,1,0,0,0,262,263,5,42,0,0,263,46,1,0,0,0,264,265,5,96,
        0,0,265,48,1,0,0,0,266,267,5,58,0,0,267,50,1,0,0,0,268,269,5,124,
        0,0,269,52,1,0,0,0,270,271,5,36,0,0,271,54,1,0,0,0,272,273,7,0,0,
        0,273,274,7,1,0,0,274,275,7,2,0,0,275,276,7,2,0,0,276,56,1,0,0,0,
        277,278,7,3,0,0,278,279,7,4,0,0,279,280,7,5,0,0,280,281,7,2,0,0,
        281,282,7,6,0,0,282,58,1,0,0,0,283,284,7,7,0,0,284,285,7,4,0,0,285,
        286,7,2,0,0,286,287,7,8,0,0,287,288,7,5,0,0,288,289,7,9,0,0,289,
        60,1,0,0,0,290,291,7,5,0,0,291,292,7,10,0,0,292,293,7,8,0,0,293,
        294,7,9,0,0,294,295,7,1,0,0,295,296,7,0,0,0,296,297,7,8,0,0,297,
        62,1,0,0,0,298,299,7,0,0,0,299,300,7,11,0,0,300,301,7,12,0,0,301,
        302,7,13,0,0,302,303,7,8,0,0,303,64,1,0,0,0,304,305,7,1,0,0,305,
        306,7,13,0,0,306,307,7,3,0,0,307,66,1,0,0,0,308,309,7,13,0,0,309,
        310,7,11,0,0,310,311,7,13,0,0,311,312,7,5,0,0,312,68,1,0,0,0,313,
        314,7,14,0,0,314,315,7,4,0,0,315,316,7,13,0,0,316,317,7,15,0,0,317,
        318,7,2,0,0,318,319,7,5,0,0,319,70,1,0,0,0,320,321,7,1,0,0,321,322,
        7,2,0,0,322,323,7,2,0,0,323,72,1,0,0,0,324,325,7,1,0,0,325,326,7,
        14,0,0,326,327,7,0,0,0,327,74,1,0,0,0,328,329,7,1,0,0,329,330,7,
        14,0,0,330,331,7,0,0,0,331,332,7,5,0,0,332,333,7,13,0,0,333,334,
        7,6,0,0,334,335,7,4,0,0,335,336,7,13,0,0,336,337,7,15,0,0,337,76,
        1,0,0,0,338,339,7,16,0,0,339,340,7,3,0,0,340,78,1,0,0,0,341,342,
        7,0,0,0,342,343,7,9,0,0,343,344,7,5,0,0,344,345,7,1,0,0,345,346,
        7,8,0,0,346,347,7,5,0,0,347,80,1,0,0,0,348,349,7,6,0,0,349,350,7,
        5,0,0,350,351,7,2,0,0,351,352,7,5,0,0,352,353,7,8,0,0,353,354,7,
        5,0,0,354,82,1,0,0,0,355,356,7,6,0,0,356,357,7,5,0,0,357,358,7,14,
        0,0,358,359,7,0,0,0,359,84,1,0,0,0,360,361,7,6,0,0,361,362,7,5,0,
        0,362,363,7,14,0,0,363,364,7,0,0,0,364,365,7,5,0,0,365,366,7,13,
        0,0,366,367,7,6,0,0,367,368,7,4,0,0,368,369,7,13,0,0,369,370,7,15,
        0,0,370,86,1,0,0,0,371,372,7,6,0,0,372,373,7,5,0,0,373,374,7,8,0,
        0,374,375,7,1,0,0,375,376,7,0,0,0,376,377,7,17,0,0,377,88,1,0,0,
        0,378,379,7,5,0,0,379,380,7,10,0,0,380,381,7,4,0,0,381,382,7,14,
        0,0,382,383,7,8,0,0,383,384,7,14,0,0,384,90,1,0,0,0,385,386,7,2,
        0,0,386,387,7,4,0,0,387,388,7,18,0,0,388,389,7,4,0,0,389,390,7,8,
        0,0,390,92,1,0,0,0,391,392,7,18,0,0,392,393,7,1,0,0,393,394,7,8,
        0,0,394,395,7,0,0,0,395,396,7,17,0,0,396,94,1,0,0,0,397,398,7,18,
        0,0,398,399,7,5,0,0,399,400,7,9,0,0,400,401,7,15,0,0,401,402,7,5,
        0,0,402,96,1,0,0,0,403,404,7,11,0,0,404,405,7,13,0,0,405,98,1,0,
        0,0,406,407,7,11,0,0,407,408,7,19,0,0,408,409,7,8,0,0,409,410,7,
        4,0,0,410,411,7,11,0,0,411,412,7,13,0,0,412,413,7,1,0,0,413,414,
        7,2,0,0,414,100,1,0,0,0,415,416,7,11,0,0,416,417,7,9,0,0,417,418,
        7,6,0,0,418,419,7,5,0,0,419,420,7,9,0,0,420,102,1,0,0,0,421,422,
        7,9,0,0,422,423,7,5,0,0,423,424,7,18,0,0,424,425,7,11,0,0,425,426,
        7,20,0,0,426,427,7,5,0,0,427,104,1,0,0,0,428,429,7,9,0,0,429,430,
        7,5,0,0,430,431,7,8,0,0,431,432,7,12,0,0,432,433,7,9,0,0,433,434,
        7,13,0,0,434,106,1,0,0,0,435,436,7,14,0,0,436,437,7,5,0,0,437,438,
        7,8,0,0,438,108,1,0,0,0,439,440,7,14,0,0,440,441,7,21,0,0,441,442,
        7,4,0,0,442,443,7,19,0,0,443,110,1,0,0,0,444,445,7,22,0,0,445,446,
        7,17,0,0,446,447,7,5,0,0,447,448,7,9,0,0,448,449,7,5,0,0,449,112,
        1,0,0,0,450,451,7,22,0,0,451,452,7,4,0,0,452,453,7,8,0,0,453,454,
        7,17,0,0,454,114,1,0,0,0,455,456,7,12,0,0,456,457,7,13,0,0,457,458,
        7,4,0,0,458,459,7,11,0,0,459,460,7,13,0,0,460,116,1,0,0,0,461,462,
        7,12,0,0,462,463,7,13,0,0,463,464,7,22,0,0,464,465,7,4,0,0,465,466,
        7,13,0,0,466,467,7,6,0,0,467,118,1,0,0,0,468,469,7,1,0,0,469,470,
        7,13,0,0,470,471,7,6,0,0,471,120,1,0,0,0,472,473,7,1,0,0,473,474,
        7,14,0,0,474,122,1,0,0,0,475,476,7,0,0,0,476,477,7,11,0,0,477,478,
        7,13,0,0,478,479,7,8,0,0,479,480,7,1,0,0,480,481,7,4,0,0,481,482,
        7,13,0,0,482,483,7,14,0,0,483,124,1,0,0,0,484,485,7,6,0,0,485,486,
        7,4,0,0,486,487,7,14,0,0,487,488,7,8,0,0,488,489,7,4,0,0,489,490,
        7,13,0,0,490,491,7,0,0,0,491,492,7,8,0,0,492,126,1,0,0,0,493,494,
        7,5,0,0,494,495,7,13,0,0,495,496,7,6,0,0,496,497,7,14,0,0,497,128,
        1,0,0,0,498,499,7,4,0,0,499,500,7,13,0,0,500,130,1,0,0,0,501,502,
        7,4,0,0,502,503,7,14,0,0,503,132,1,0,0,0,504,505,7,13,0,0,505,506,
        7,11,0,0,506,507,7,8,0,0,507,134,1,0,0,0,508,509,7,11,0,0,509,510,
        7,9,0,0,510,136,1,0,0,0,511,512,7,14,0,0,512,513,7,8,0,0,513,514,
        7,1,0,0,514,515,7,9,0,0,515,516,7,8,0,0,516,517,7,14,0,0,517,138,
        1,0,0,0,518,519,7,10,0,0,519,520,7,11,0,0,520,521,7,9,0,0,521,140,
        1,0,0,0,522,523,7,7,0,0,523,524,7,1,0,0,524,525,7,2,0,0,525,526,
        7,14,0,0,526,527,7,5,0,0,527,142,1,0,0,0,528,529,7,8,0,0,529,530,
        7,9,0,0,530,531,7,12,0,0,531,532,7,5,0,0,532,144,1,0,0,0,533,534,
        7,13,0,0,534,535,7,12,0,0,535,536,7,2,0,0,536,537,7,2,0,0,537,146,
        1,0,0,0,538,539,7,0,0,0,539,540,7,11,0,0,540,541,7,13,0,0,541,542,
        7,14,0,0,542,543,7,8,0,0,543,544,7,9,0,0,544,545,7,1,0,0,545,546,
        7,4,0,0,546,547,7,13,0,0,547,548,7,8,0,0,548,148,1,0,0,0,549,550,
        7,6,0,0,550,551,7,11,0,0,551,150,1,0,0,0,552,553,7,7,0,0,553,554,
        7,11,0,0,554,555,7,9,0,0,555,152,1,0,0,0,556,557,7,9,0,0,557,558,
        7,5,0,0,558,559,7,23,0,0,559,560,7,12,0,0,560,561,7,4,0,0,561,562,
        7,9,0,0,562,563,7,5,0,0,563,154,1,0,0,0,564,565,7,12,0,0,565,566,
        7,13,0,0,566,567,7,4,0,0,567,568,7,23,0,0,568,569,7,12,0,0,569,570,
        7,5,0,0,570,156,1,0,0,0,571,572,7,0,0,0,572,573,7,1,0,0,573,574,
        7,14,0,0,574,575,7,5,0,0,575,158,1,0,0,0,576,577,7,22,0,0,577,578,
        7,17,0,0,578,579,7,5,0,0,579,580,7,13,0,0,580,160,1,0,0,0,581,582,
        7,8,0,0,582,583,7,17,0,0,583,584,7,5,0,0,584,585,7,13,0,0,585,162,
        1,0,0,0,586,587,7,5,0,0,587,588,7,2,0,0,588,589,7,14,0,0,589,590,
        7,5,0,0,590,164,1,0,0,0,591,592,7,5,0,0,592,593,7,13,0,0,593,594,
        7,6,0,0,594,166,1,0,0,0,595,596,7,18,0,0,596,597,7,1,0,0,597,598,
        7,13,0,0,598,599,7,6,0,0,599,600,7,1,0,0,600,601,7,8,0,0,601,602,
        7,11,0,0,602,603,7,9,0,0,603,604,7,3,0,0,604,168,1,0,0,0,605,606,
        7,14,0,0,606,607,7,0,0,0,607,608,7,1,0,0,608,609,7,2,0,0,609,610,
        7,1,0,0,610,611,7,9,0,0,611,170,1,0,0,0,612,613,7,11,0,0,613,614,
        7,7,0,0,614,172,1,0,0,0,615,616,7,1,0,0,616,617,7,6,0,0,617,618,
        7,6,0,0,618,174,1,0,0,0,619,620,7,6,0,0,620,621,7,9,0,0,621,622,
        7,11,0,0,622,623,7,19,0,0,623,176,1,0,0,0,624,626,3,209,104,0,625,
        624,1,0,0,0,626,627,1,0,0,0,627,625,1,0,0,0,627,628,1,0,0,0,628,
        178,1,0,0,0,629,633,5,96,0,0,630,632,9,0,0,0,631,630,1,0,0,0,632,
        635,1,0,0,0,633,634,1,0,0,0,633,631,1,0,0,0,634,636,1,0,0,0,635,
        633,1,0,0,0,636,637,5,96,0,0,637,180,1,0,0,0,638,641,5,39,0,0,639,
        642,8,24,0,0,640,642,3,197,98,0,641,639,1,0,0,0,641,640,1,0,0,0,
        641,642,1,0,0,0,642,643,1,0,0,0,643,644,5,39,0,0,644,182,1,0,0,0,
        645,650,5,34,0,0,646,649,8,25,0,0,647,649,3,197,98,0,648,646,1,0,
        0,0,648,647,1,0,0,0,649,652,1,0,0,0,650,648,1,0,0,0,650,651,1,0,
        0,0,651,653,1,0,0,0,652,650,1,0,0,0,653,654,5,34,0,0,654,184,1,0,
        0,0,655,657,3,35,17,0,656,655,1,0,0,0,656,657,1,0,0,0,657,662,1,
        0,0,0,658,663,3,203,101,0,659,663,3,205,102,0,660,663,3,207,103,
        0,661,663,3,187,93,0,662,658,1,0,0,0,662,659,1,0,0,0,662,660,1,0,
        0,0,662,661,1,0,0,0,663,186,1,0,0,0,664,665,3,207,103,0,665,666,
        5,46,0,0,666,667,3,207,103,0,667,671,1,0,0,0,668,669,5,46,0,0,669,
        671,3,207,103,0,670,664,1,0,0,0,670,668,1,0,0,0,671,673,1,0,0,0,
        672,674,3,199,99,0,673,672,1,0,0,0,673,674,1,0,0,0,674,676,1,0,0,
        0,675,677,7,26,0,0,676,675,1,0,0,0,676,677,1,0,0,0,677,687,1,0,0,
        0,678,684,3,207,103,0,679,681,3,199,99,0,680,682,7,26,0,0,681,680,
        1,0,0,0,681,682,1,0,0,0,682,685,1,0,0,0,683,685,7,26,0,0,684,679,
        1,0,0,0,684,683,1,0,0,0,685,687,1,0,0,0,686,670,1,0,0,0,686,678,
        1,0,0,0,687,188,1,0,0,0,688,690,7,27,0,0,689,688,1,0,0,0,690,691,
        1,0,0,0,691,689,1,0,0,0,691,692,1,0,0,0,692,693,1,0,0,0,693,694,
        6,94,0,0,694,190,1,0,0,0,695,696,5,47,0,0,696,697,5,42,0,0,697,701,
        1,0,0,0,698,700,9,0,0,0,699,698,1,0,0,0,700,703,1,0,0,0,701,702,
        1,0,0,0,701,699,1,0,0,0,702,704,1,0,0,0,703,701,1,0,0,0,704,705,
        5,42,0,0,705,706,5,47,0,0,706,707,1,0,0,0,707,708,6,95,1,0,708,192,
        1,0,0,0,709,710,5,47,0,0,710,711,5,47,0,0,711,715,1,0,0,0,712,714,
        8,28,0,0,713,712,1,0,0,0,714,717,1,0,0,0,715,713,1,0,0,0,715,716,
        1,0,0,0,716,718,1,0,0,0,717,715,1,0,0,0,718,719,6,96,1,0,719,194,
        1,0,0,0,720,721,9,0,0,0,721,722,1,0,0,0,722,723,6,97,0,0,723,196,
        1,0,0,0,724,725,5,92,0,0,725,746,7,29,0,0,726,731,5,92,0,0,727,729,
        7,30,0,0,728,727,1,0,0,0,728,729,1,0,0,0,729,730,1,0,0,0,730,732,
        7,31,0,0,731,728,1,0,0,0,731,732,1,0,0,0,732,733,1,0,0,0,733,746,
        7,31,0,0,734,736,5,92,0,0,735,737,7,12,0,0,736,735,1,0,0,0,737,738,
        1,0,0,0,738,736,1,0,0,0,738,739,1,0,0,0,739,740,1,0,0,0,740,741,
        3,203,101,0,741,742,3,203,101,0,742,743,3,203,101,0,743,744,3,203,
        101,0,744,746,1,0,0,0,745,724,1,0,0,0,745,726,1,0,0,0,745,734,1,
        0,0,0,746,198,1,0,0,0,747,749,7,5,0,0,748,750,7,32,0,0,749,748,1,
        0,0,0,749,750,1,0,0,0,750,751,1,0,0,0,751,752,3,207,103,0,752,200,
        1,0,0,0,753,754,5,48,0,0,754,755,7,10,0,0,755,756,1,0,0,0,756,765,
        3,203,101,0,757,760,3,203,101,0,758,760,5,95,0,0,759,757,1,0,0,0,
        759,758,1,0,0,0,760,763,1,0,0,0,761,759,1,0,0,0,761,762,1,0,0,0,
        762,764,1,0,0,0,763,761,1,0,0,0,764,766,3,203,101,0,765,761,1,0,
        0,0,765,766,1,0,0,0,766,202,1,0,0,0,767,768,7,33,0,0,768,204,1,0,
        0,0,769,770,5,48,0,0,770,771,3,207,103,0,771,206,1,0,0,0,772,780,
        7,34,0,0,773,775,7,35,0,0,774,773,1,0,0,0,775,778,1,0,0,0,776,774,
        1,0,0,0,776,777,1,0,0,0,777,779,1,0,0,0,778,776,1,0,0,0,779,781,
        7,36,0,0,780,776,1,0,0,0,780,781,1,0,0,0,781,208,1,0,0,0,782,785,
        3,211,105,0,783,785,7,36,0,0,784,782,1,0,0,0,784,783,1,0,0,0,785,
        210,1,0,0,0,786,791,7,37,0,0,787,791,8,38,0,0,788,789,7,39,0,0,789,
        791,7,40,0,0,790,786,1,0,0,0,790,787,1,0,0,0,790,788,1,0,0,0,791,
        212,1,0,0,0,29,0,627,633,641,648,650,656,662,670,673,676,681,684,
        686,691,701,715,728,731,738,745,749,759,761,765,776,780,784,790,
        2,0,1,0,0,2,0
    ]

class CypherLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENTS = 2

    ASSIGN = 1
    ADD_ASSIGN = 2
    LE = 3
    GE = 4
    GT = 5
    LT = 6
    NOT_EQUAL = 7
    RANGE = 8
    SEMI = 9
    DOT = 10
    COMMA = 11
    LPAREN = 12
    RPAREN = 13
    LBRACE = 14
    RBRACE = 15
    LBRACK = 16
    RBRACK = 17
    SUB = 18
    PLUS = 19
    DIV = 20
    MOD = 21
    CARET = 22
    MULT = 23
    ESC = 24
    COLON = 25
    STICK = 26
    DOLLAR = 27
    CALL = 28
    YIELD = 29
    FILTER = 30
    EXTRACT = 31
    COUNT = 32
    ANY = 33
    NONE = 34
    SINGLE = 35
    ALL = 36
    ASC = 37
    ASCENDING = 38
    BY = 39
    CREATE = 40
    DELETE = 41
    DESC = 42
    DESCENDING = 43
    DETACH = 44
    EXISTS = 45
    LIMIT = 46
    MATCH = 47
    MERGE = 48
    ON = 49
    OPTIONAL = 50
    ORDER = 51
    REMOVE = 52
    RETURN = 53
    SET = 54
    SKIP_W = 55
    WHERE = 56
    WITH = 57
    UNION = 58
    UNWIND = 59
    AND = 60
    AS = 61
    CONTAINS = 62
    DISTINCT = 63
    ENDS = 64
    IN = 65
    IS = 66
    NOT = 67
    OR = 68
    STARTS = 69
    XOR = 70
    FALSE = 71
    TRUE = 72
    NULL_W = 73
    CONSTRAINT = 74
    DO = 75
    FOR = 76
    REQUIRE = 77
    UNIQUE = 78
    CASE = 79
    WHEN = 80
    THEN = 81
    ELSE = 82
    END = 83
    MANDATORY = 84
    SCALAR = 85
    OF = 86
    ADD = 87
    DROP = 88
    ID = 89
    ESC_LITERAL = 90
    CHAR_LITERAL = 91
    STRING_LITERAL = 92
    DIGIT = 93
    FLOAT = 94
    WS = 95
    COMMENT = 96
    LINE_COMMENT = 97
    ERRCHAR = 98
    Letter = 99

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"COMMENTS" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+='", "'<='", "'>='", "'>'", "'<'", "'<>'", "'..'", 
            "';'", "'.'", "','", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'-'", "'+'", "'/'", "'%'", "'^'", "'*'", "'`'", "':'", "'|'", 
            "'$'", "'CALL'", "'YIELD'", "'FILTER'", "'EXTRACT'", "'COUNT'", 
            "'ANY'", "'NONE'", "'SINGLE'", "'ALL'", "'ASC'", "'ASCENDING'", 
            "'BY'", "'CREATE'", "'DELETE'", "'DESC'", "'DESCENDING'", "'DETACH'", 
            "'EXISTS'", "'LIMIT'", "'MATCH'", "'MERGE'", "'ON'", "'OPTIONAL'", 
            "'ORDER'", "'REMOVE'", "'RETURN'", "'SET'", "'SKIP'", "'WHERE'", 
            "'WITH'", "'UNION'", "'UNWIND'", "'AND'", "'AS'", "'CONTAINS'", 
            "'DISTINCT'", "'ENDS'", "'IN'", "'IS'", "'NOT'", "'OR'", "'STARTS'", 
            "'XOR'", "'FALSE'", "'TRUE'", "'NULL'", "'CONSTRAINT'", "'DO'", 
            "'FOR'", "'REQUIRE'", "'UNIQUE'", "'CASE'", "'WHEN'", "'THEN'", 
            "'ELSE'", "'END'", "'MANDATORY'", "'SCALAR'", "'OF'", "'ADD'", 
            "'DROP'" ]

    symbolicNames = [ "<INVALID>",
            "ASSIGN", "ADD_ASSIGN", "LE", "GE", "GT", "LT", "NOT_EQUAL", 
            "RANGE", "SEMI", "DOT", "COMMA", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACK", "RBRACK", "SUB", "PLUS", "DIV", "MOD", "CARET", 
            "MULT", "ESC", "COLON", "STICK", "DOLLAR", "CALL", "YIELD", 
            "FILTER", "EXTRACT", "COUNT", "ANY", "NONE", "SINGLE", "ALL", 
            "ASC", "ASCENDING", "BY", "CREATE", "DELETE", "DESC", "DESCENDING", 
            "DETACH", "EXISTS", "LIMIT", "MATCH", "MERGE", "ON", "OPTIONAL", 
            "ORDER", "REMOVE", "RETURN", "SET", "SKIP_W", "WHERE", "WITH", 
            "UNION", "UNWIND", "AND", "AS", "CONTAINS", "DISTINCT", "ENDS", 
            "IN", "IS", "NOT", "OR", "STARTS", "XOR", "FALSE", "TRUE", "NULL_W", 
            "CONSTRAINT", "DO", "FOR", "REQUIRE", "UNIQUE", "CASE", "WHEN", 
            "THEN", "ELSE", "END", "MANDATORY", "SCALAR", "OF", "ADD", "DROP", 
            "ID", "ESC_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", "DIGIT", 
            "FLOAT", "WS", "COMMENT", "LINE_COMMENT", "ERRCHAR", "Letter" ]

    ruleNames = [ "ASSIGN", "ADD_ASSIGN", "LE", "GE", "GT", "LT", "NOT_EQUAL", 
                  "RANGE", "SEMI", "DOT", "COMMA", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "SUB", "PLUS", "DIV", "MOD", 
                  "CARET", "MULT", "ESC", "COLON", "STICK", "DOLLAR", "CALL", 
                  "YIELD", "FILTER", "EXTRACT", "COUNT", "ANY", "NONE", 
                  "SINGLE", "ALL", "ASC", "ASCENDING", "BY", "CREATE", "DELETE", 
                  "DESC", "DESCENDING", "DETACH", "EXISTS", "LIMIT", "MATCH", 
                  "MERGE", "ON", "OPTIONAL", "ORDER", "REMOVE", "RETURN", 
                  "SET", "SKIP_W", "WHERE", "WITH", "UNION", "UNWIND", "AND", 
                  "AS", "CONTAINS", "DISTINCT", "ENDS", "IN", "IS", "NOT", 
                  "OR", "STARTS", "XOR", "FALSE", "TRUE", "NULL_W", "CONSTRAINT", 
                  "DO", "FOR", "REQUIRE", "UNIQUE", "CASE", "WHEN", "THEN", 
                  "ELSE", "END", "MANDATORY", "SCALAR", "OF", "ADD", "DROP", 
                  "ID", "ESC_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", 
                  "DIGIT", "FLOAT", "WS", "COMMENT", "LINE_COMMENT", "ERRCHAR", 
                  "EscapeSequence", "ExponentPart", "HexDigits", "HexDigit", 
                  "OctalDigit", "Digits", "LetterOrDigit", "Letter" ]

    grammarFileName = "CypherLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

