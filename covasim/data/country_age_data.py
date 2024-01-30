'''
Define country age pyramids.

This is the following file:

https://github.com/neherlab/covid19_scenarios/blob/master/src/assets/data/country_age_distribution.json

expressed as a Python file.
'''

data = {
 'Afghanistan': {'0-9': 11088731,
  '10-19': 9821561,
  '20-29': 7035871,
  '30-39': 4534646,
  '40-49': 2963460,
  '50-59': 1840199,
  '60-69': 1057497,
  '70-79': 480455,
  '80+': 105925},
 'Albania': {'0-9': 333832,
  '10-19': 361777,
  '20-29': 472678,
  '30-39': 390771,
  '40-49': 323020,
  '50-59': 386091,
  '60-69': 330244,
  '70-79': 194668,
  '80+': 84716},
 'Algeria': {'0-9': 9677492,
  '10-19': 6731745,
  '20-29': 6573711,
  '30-39': 7275234,
  '40-49': 5448620,
  '50-59': 3800054,
  '60-69': 2530543,
  '70-79': 1237832,
  '80+': 575811},
 'Angola': {'0-9': 10899167,
  '10-19': 7881777,
  '20-29': 5306039,
  '30-39': 3699729,
  '40-49': 2412736,
  '50-59': 1464604,
  '60-69': 785896,
  '70-79': 331730,
  '80+': 84594},
 'Antigua and Barbuda': {'0-9': 14582,
  '10-19': 13868,
  '20-29': 14895,
  '30-39': 14095,
  '40-49': 13860,
  '50-59': 12832,
  '60-69': 8042,
  '70-79': 4101,
  '80+': 1654},
 'Argentina': {'0-9': 7446465,
  '10-19': 7136712,
  '20-29': 6997584,
  '30-39': 6441412,
  '40-49': 5727746,
  '50-59': 4424939,
  '60-69': 3528743,
  '70-79': 2300637,
  '80+': 1191536},
 'Armenia': {'0-9': 418860,
  '10-19': 368930,
  '20-29': 408926,
  '30-39': 503954,
  '40-49': 353090,
  '50-59': 362654,
  '60-69': 328401,
  '70-79': 126744,
  '80+': 91684},
 'Aruba': {'0-9': 11758,
  '10-19': 14010,
  '20-29': 14980,
  '30-39': 11241,
  '40-49': 14271,
  '50-59': 17207,
  '60-69': 13753,
  '70-79': 6956,
  '80+': 2590},
 'Australia': {'0-9': 3308972,
  '10-19': 3130480,
  '20-29': 3375453,
  '30-39': 3718346,
  '40-49': 3306061,
  '50-59': 3107734,
  '60-69': 2651187,
  '70-79': 1846377,
  '80+': 1055274},
 'Austria': {'0-9': 874182,
  '10-19': 876207,
  '20-29': 1115378,
  '30-39': 1243414,
  '40-49': 1178265,
  '50-59': 1407001,
  '60-69': 1033318,
  '70-79': 790436,
  '80+': 488197},
 'Azerbaijan': {'0-9': 1686038,
  '10-19': 1335455,
  '20-29': 1608982,
  '30-39': 1766690,
  '40-49': 1280804,
  '50-59': 1281076,
  '60-69': 804312,
  '70-79': 242762,
  '80+': 133058},
 'Bahamas': {'0-9': 53654,
  '10-19': 63795,
  '20-29': 66571,
  '30-39': 55456,
  '40-49': 56498,
  '50-59': 49219,
  '60-69': 29427,
  '70-79': 13644,
  '80+': 4980},
 'Bahrain': {'0-9': 218134,
  '10-19': 181855,
  '20-29': 306667,
  '30-39': 507735,
  '40-49': 256720,
  '50-59': 140231,
  '60-69': 66573,
  '70-79': 17815,
  '80+': 5845},
 'Bangladesh': {'0-9': 28972611,
  '10-19': 30674421,
  '20-29': 29765032,
  '30-39': 26511633,
  '40-49': 20651269,
  '50-59': 15005706,
  '60-69': 7296839,
  '70-79': 4095813,
  '80+': 1716059},
 'Barbados': {'0-9': 30617,
  '10-19': 36514,
  '20-29': 37578,
  '30-39': 37124,
  '40-49': 39068,
  '50-59': 39936,
  '60-69': 33573,
  '70-79': 20154,
  '80+': 12811},
 'Belarus': {'0-9': 1143840,
  '10-19': 928884,
  '20-29': 1077804,
  '30-39': 1530347,
  '40-49': 1285399,
  '50-59': 1345792,
  '60-69': 1243251,
  '70-79': 525562,
  '80+': 368444},
 'Belgium': {'0-9': 1302703,
  '10-19': 1312253,
  '20-29': 1386087,
  '30-39': 1504000,
  '40-49': 1518439,
  '50-59': 1598741,
  '60-69': 1369875,
  '70-79': 939415,
  '80+': 658110},
 'Belize': {'0-9': 78107,
  '10-19': 77850,
  '20-29': 75822,
  '30-39': 59711,
  '40-49': 43959,
  '50-59': 31811,
  '60-69': 17817,
  '70-79': 8310,
  '80+': 4240},
 'Benin': {'0-9': 3596952,
  '10-19': 2779488,
  '20-29': 2061769,
  '30-39': 1436440,
  '40-49': 981831,
  '50-59': 650680,
  '60-69': 379184,
  '70-79': 184835,
  '80+': 52021},
 'Bhutan': {'0-9': 125825,
  '10-19': 135992,
  '20-29': 153315,
  '30-39': 138679,
  '40-49': 89605,
  '50-59': 59011,
  '60-69': 36910,
  '70-79': 22235,
  '80+': 10036},
 'Bolivia (Plurinational State of)': {'0-9': 2364587,
  '10-19': 2297693,
  '20-29': 2039536,
  '30-39': 1639098,
  '40-49': 1238341,
  '50-59': 883592,
  '60-69': 615318,
  '70-79': 391940,
  '80+': 202916},
 'Bosnia and Herzegovina': {'0-9': 295215,
  '10-19': 346276,
  '20-29': 403273,
  '30-39': 458386,
  '40-49': 447738,
  '50-59': 500181,
  '60-69': 463795,
  '70-79': 242499,
  '80+': 123456},
 'Botswana': {'0-9': 539004,
  '10-19': 472033,
  '20-29': 402508,
  '30-39': 365289,
  '40-49': 261017,
  '50-59': 146580,
  '60-69': 104252,
  '70-79': 48560,
  '80+': 12384},
 'Brazil': {'0-9': 29076912,
  '10-19': 31160447,
  '20-29': 34104644,
  '30-39': 34476764,
  '40-49': 29462008,
  '50-59': 24421199,
  '60-69': 16896864,
  '70-79': 8801551,
  '80+': 4159028},
 'Brunei Darussalam': {'0-9': 66355,
  '10-19': 65082,
  '20-29': 69697,
  '30-39': 76569,
  '40-49': 68004,
  '50-59': 50218,
  '60-69': 28512,
  '70-79': 9570,
  '80+': 3471},
 'Bulgaria': {'0-9': 649382,
  '10-19': 685881,
  '20-29': 689917,
  '30-39': 957591,
  '40-49': 1061986,
  '50-59': 944703,
  '60-69': 922593,
  '70-79': 710368,
  '80+': 326024},
 'Burkina Faso': {'0-9': 6552186,
  '10-19': 5029543,
  '20-29': 3508067,
  '30-39': 2428031,
  '40-49': 1587132,
  '50-59': 977489,
  '60-69': 538877,
  '70-79': 234236,
  '80+': 47712},
 'Burundi': {'0-9': 3872449,
  '10-19': 2725292,
  '20-29': 2029583,
  '30-39': 1539545,
  '40-49': 747634,
  '50-59': 491973,
  '60-69': 339630,
  '70-79': 112127,
  '80+': 32551},
 'Cabo Verde': {'0-9': 105077,
  '10-19': 99937,
  '20-29': 97847,
  '30-39': 98288,
  '40-49': 64905,
  '50-59': 47913,
  '60-69': 26368,
  '70-79': 9054,
  '80+': 6598},
 'Cambodia': {'0-9': 3530588,
  '10-19': 3100069,
  '20-29': 3117605,
  '30-39': 2889268,
  '40-49': 1429088,
  '50-59': 1387484,
  '60-69': 816774,
  '70-79': 352443,
  '80+': 95646},
 'Cameroon': {'0-9': 7846025,
  '10-19': 6176460,
  '20-29': 4551789,
  '30-39': 3399844,
  '40-49': 2141843,
  '50-59': 1288476,
  '60-69': 733298,
  '70-79': 332733,
  '80+': 75395},
 'Canada': {'0-9': 3970918,
  '10-19': 3971318,
  '20-29': 5096615,
  '30-39': 5278663,
  '40-49': 4846667,
  '50-59': 5182430,
  '60-69': 4712746,
  '70-79': 3018677,
  '80+': 1664120},
 'Central African Republic': {'0-9': 1435610,
  '10-19': 1264610,
  '20-29': 839989,
  '30-39': 501334,
  '40-49': 339531,
  '50-59': 232597,
  '60-69': 139061,
  '70-79': 61505,
  '80+': 15530},
 'Chad': {'0-9': 5452555,
  '10-19': 4038729,
  '20-29': 2781016,
  '30-39': 1769644,
  '40-49': 1082834,
  '50-59': 654647,
  '60-69': 417351,
  '70-79': 180661,
  '80+': 48427},
 'Channel Islands': {'0-9': 17565,
  '10-19': 17778,
  '20-29': 21767,
  '30-39': 23888,
  '40-49': 24915,
  '50-59': 26180,
  '60-69': 20014,
  '70-79': 13295,
  '80+': 8461},
 'Chile': {'0-9': 2428078,
  '10-19': 2493875,
  '20-29': 2995538,
  '30-39': 2945403,
  '40-49': 2578406,
  '50-59': 2352271,
  '60-69': 1791785,
  '70-79': 993127,
  '80+': 537718},
 'China': {'0-9': 170667621,
  '10-19': 166604608,
  '20-29': 185147173,
  '30-39': 228830425,
  '40-49': 216111764,
  '50-59': 222185873,
  '60-69': 151663904,
  '70-79': 71494306,
  '80+': 26618102},
 'China, Hong Kong Special Administrative Region': {'0-9': 664195,
  '10-19': 552658,
  '20-29': 867629,
  '30-39': 1122165,
  '40-49': 1129131,
  '50-59': 1207906,
  '60-69': 1048879,
  '70-79': 525082,
  '80+': 379336},
 'China, Macao Special Administrative Region': {'0-9': 68816,
  '10-19': 46834,
  '20-29': 88333,
  '30-39': 129800,
  '40-49': 93400,
  '50-59': 99614,
  '60-69': 78993,
  '70-79': 29881,
  '80+': 13664},
 'Colombia': {'0-9': 7414157,
  '10-19': 8119877,
  '20-29': 8847062,
  '30-39': 7810299,
  '40-49': 6450787,
  '50-59': 5543982,
  '60-69': 3771360,
  '70-79': 1979762,
  '80+': 945605},
 'Comoros': {'0-9': 237638,
  '10-19': 191272,
  '20-29': 150847,
  '30-39': 117375,
  '40-49': 77037,
  '50-59': 50890,
  '60-69': 29657,
  '70-79': 11660,
  '80+': 3225},
 'Congo': {'0-9': 1592333,
  '10-19': 1257962,
  '20-29': 874259,
  '30-39': 680079,
  '40-49': 535815,
  '50-59': 327893,
  '60-69': 164736,
  '70-79': 69397,
  '80+': 15613},
 'Costa Rica': {'0-9': 705597,
  '10-19': 718839,
  '20-29': 824456,
  '30-39': 825655,
  '40-49': 650563,
  '50-59': 602394,
  '60-69': 423012,
  '70-79': 230865,
  '80+': 112737},
 'Croatia': {'0-9': 385776,
  '10-19': 408108,
  '20-29': 472201,
  '30-39': 539290,
  '40-49': 557001,
  '50-59': 581382,
  '60-69': 565376,
  '70-79': 361956,
  '80+': 234177},
 'Cuba': {'0-9': 1199375,
  '10-19': 1246736,
  '20-29': 1421019,
  '30-39': 1523032,
  '40-49': 1561981,
  '50-59': 1967294,
  '60-69': 1174022,
  '70-79': 804207,
  '80+': 428950},
 'Curaçao': {'0-9': 19332,
  '10-19': 21569,
  '20-29': 19539,
  '30-39': 18724,
  '40-49': 20279,
  '50-59': 24425,
  '60-69': 20705,
  '70-79': 13003,
  '80+': 6517},
 'Cyprus': {'0-9': 132391,
  '10-19': 141658,
  '20-29': 191801,
  '30-39': 188388,
  '40-49': 166627,
  '50-59': 147538,
  '60-69': 120401,
  '70-79': 78681,
  '80+': 39873},
 'Czechia': {'0-9': 1113645,
  '10-19': 1061333,
  '20-29': 1105336,
  '30-39': 1478211,
  '40-49': 1798356,
  '50-59': 1351269,
  '60-69': 1324617,
  '70-79': 1031099,
  '80+': 445115},
 'Côte d’Ivoire': {'0-9': 7750285,
  '10-19': 6104859,
  '20-29': 4660993,
  '30-39': 3172218,
  '40-49': 2117549,
  '50-59': 1337227,
  '60-69': 822065,
  '70-79': 341744,
  '80+': 71333},
 "Democratic People's Republic of Korea": {'0-9': 3430376,
  '10-19': 3561227,
  '20-29': 3925716,
  '30-39': 3641896,
  '40-49': 3714317,
  '50-59': 3622786,
  '60-69': 2134680,
  '70-79': 1303957,
  '80+': 443861},
 'Democratic Republic of the Congo': {'0-9': 29487305,
  '10-19': 21000019,
  '20-29': 14169239,
  '30-39': 9762333,
  '40-49': 6605529,
  '50-59': 4347003,
  '60-69': 2585842,
  '70-79': 1268687,
  '80+': 335446},
 'Denmark': {'0-9': 606028,
  '10-19': 675946,
  '20-29': 775962,
  '30-39': 672290,
  '40-49': 738209,
  '50-59': 810126,
  '60-69': 654530,
  '70-79': 586139,
  '80+': 272972},
 'Djibouti': {'0-9': 197110,
  '10-19': 179320,
  '20-29': 177326,
  '30-39': 162418,
  '40-49': 120923,
  '50-59': 78074,
  '60-69': 44336,
  '70-79': 22330,
  '80+': 6163},
 'Dominican Republic': {'0-9': 1999349,
  '10-19': 1935877,
  '20-29': 1854317,
  '30-39': 1564383,
  '40-49': 1274489,
  '50-59': 1014335,
  '60-69': 682138,
  '70-79': 341500,
  '80+': 181522},
 'Ecuador': {'0-9': 3277730,
  '10-19': 3115981,
  '20-29': 3036186,
  '30-39': 2592840,
  '40-49': 2088240,
  '50-59': 1591141,
  '60-69': 1087740,
  '70-79': 570125,
  '80+': 283071},
 'Egypt': {'0-9': 25028540,
  '10-19': 18385431,
  '20-29': 16511130,
  '30-39': 15198348,
  '40-49': 10948603,
  '50-59': 7844894,
  '60-69': 5122656,
  '70-79': 2530981,
  '80+': 763821},
 'El Salvador': {'0-9': 1146823,
  '10-19': 1165823,
  '20-29': 1215815,
  '30-39': 882443,
  '40-49': 725144,
  '50-59': 568072,
  '60-69': 406296,
  '70-79': 248393,
  '80+': 127396},
 'Equatorial Guinea': {'0-9': 371662,
  '10-19': 265295,
  '20-29': 286389,
  '30-39': 248982,
  '40-49': 115361,
  '50-59': 62216,
  '60-69': 34879,
  '70-79': 14719,
  '80+': 3482},
 'Eritrea': {'0-9': 971768,
  '10-19': 860627,
  '20-29': 572233,
  '30-39': 460764,
  '40-49': 280838,
  '50-59': 171949,
  '60-69': 128327,
  '70-79': 77079,
  '80+': 22836},
 'Estonia': {'0-9': 143661,
  '10-19': 137487,
  '20-29': 145554,
  '30-39': 193631,
  '40-49': 184936,
  '50-59': 165282,
  '60-69': 169473,
  '70-79': 107430,
  '80+': 79081},
 'Eswatini': {'0-9': 286620,
  '10-19': 277020,
  '20-29': 212889,
  '30-39': 161329,
  '40-49': 104399,
  '50-59': 51716,
  '60-69': 36524,
  '70-79': 22581,
  '80+': 7086},
 'Ethiopia': {'0-9': 32037548,
  '10-19': 26828994,
  '20-29': 21439043,
  '30-39': 13792878,
  '40-49': 9038652,
  '50-59': 5704067,
  '60-69': 3624557,
  '70-79': 1929368,
  '80+': 568479},
 'Fiji': {'0-9': 177143,
  '10-19': 158135,
  '20-29': 141943,
  '30-39': 134953,
  '40-49': 106524,
  '50-59': 91436,
  '60-69': 57120,
  '70-79': 23633,
  '80+': 5558},
 'Finland': {'0-9': 568681,
  '10-19': 606659,
  '20-29': 672353,
  '30-39': 706581,
  '40-49': 659560,
  '50-59': 720555,
  '60-69': 712327,
  '70-79': 582988,
  '80+': 311016},
 'France': {'0-9': 7527473,
  '10-19': 7883476,
  '20-29': 7371030,
  '30-39': 8011050,
  '40-49': 8325670,
  '50-59': 8635055,
  '60-69': 7764785,
  '70-79': 5727704,
  '80+': 4027268},
 'French Guiana': {'0-9': 66122,
  '10-19': 57555,
  '20-29': 46109,
  '30-39': 38719,
  '40-49': 36992,
  '50-59': 26711,
  '60-69': 17226,
  '70-79': 7221,
  '80+': 2027},
 'French Polynesia': {'0-9': 39637,
  '10-19': 44133,
  '20-29': 40379,
  '30-39': 43366,
  '40-49': 39589,
  '50-59': 35650,
  '60-69': 23042,
  '70-79': 10823,
  '80+': 4289},
 'Gabon': {'0-9': 600005,
  '10-19': 422773,
  '20-29': 367412,
  '30-39': 350071,
  '40-49': 232167,
  '50-59': 134150,
  '60-69': 71303,
  '70-79': 36691,
  '80+': 11162},
 'Gambia': {'0-9': 762307,
  '10-19': 556857,
  '20-29': 429180,
  '30-39': 283130,
  '40-49': 174068,
  '50-59': 115915,
  '60-69': 59281,
  '70-79': 30007,
  '80+': 5923},
 'Georgia': {'0-9': 553163,
  '10-19': 471056,
  '20-29': 500696,
  '30-39': 565077,
  '40-49': 517944,
  '50-59': 523623,
  '60-69': 459856,
  '70-79': 248784,
  '80+': 148968},
 'Germany': {'0-9': 7880902,
  '10-19': 7930616,
  '20-29': 9377359,
  '30-39': 10872019,
  '40-49': 10243351,
  '50-59': 13488393,
  '60-69': 10644140,
  '70-79': 7471414,
  '80+': 5875748},
 'Ghana': {'0-9': 8057871,
  '10-19': 6616719,
  '20-29': 5398591,
  '30-39': 4190417,
  '40-49': 3031249,
  '50-59': 2134980,
  '60-69': 1091069,
  '70-79': 456786,
  '80+': 95258},
 'Greece': {'0-9': 881128,
  '10-19': 1068855,
  '20-29': 1057214,
  '30-39': 1336517,
  '40-49': 1574408,
  '50-59': 1505692,
  '60-69': 1257161,
  '70-79': 956084,
  '80+': 785994},
 'Grenada': {'0-9': 18132,
  '10-19': 16137,
  '20-29': 18288,
  '30-39': 18211,
  '40-49': 12874,
  '50-59': 12146,
  '60-69': 9573,
  '70-79': 4789,
  '80+': 2373},
 'Guadeloupe': {'0-9': 44992,
  '10-19': 58514,
  '20-29': 46875,
  '30-39': 33762,
  '40-49': 49307,
  '50-59': 62202,
  '60-69': 50569,
  '70-79': 32942,
  '80+': 20961},
 'Guam': {'0-9': 26981,
  '10-19': 27159,
  '20-29': 27031,
  '30-39': 21837,
  '40-49': 19935,
  '50-59': 20162,
  '60-69': 14330,
  '70-79': 7777,
  '80+': 3563},
 'Guatemala': {'0-9': 4047466,
  '10-19': 3871605,
  '20-29': 3413158,
  '30-39': 2532063,
  '40-49': 1701991,
  '50-59': 1053821,
  '60-69': 718853,
  '70-79': 382505,
  '80+': 194106},
 'Guinea': {'0-9': 3965625,
  '10-19': 3199454,
  '20-29': 2365739,
  '30-39': 1470866,
  '40-49': 898439,
  '50-59': 614523,
  '60-69': 408149,
  '70-79': 171250,
  '80+': 38750},
 'Guinea-Bissau': {'0-9': 582349,
  '10-19': 450031,
  '20-29': 342383,
  '30-39': 254507,
  '40-49': 156574,
  '50-59': 92190,
  '60-69': 60417,
  '70-79': 24637,
  '80+': 4913},
 'Guyana': {'0-9': 147626,
  '10-19': 145351,
  '20-29': 145302,
  '30-39': 93113,
  '40-49': 90525,
  '50-59': 79336,
  '60-69': 51355,
  '70-79': 22936,
  '80+': 11008},
 'Haiti': {'0-9': 2500777,
  '10-19': 2346528,
  '20-29': 2044459,
  '30-39': 1731657,
  '40-49': 1106487,
  '50-59': 789624,
  '60-69': 523931,
  '70-79': 260217,
  '80+': 98848},
 'Honduras': {'0-9': 2005992,
  '10-19': 2064637,
  '20-29': 1905416,
  '30-39': 1470935,
  '40-49': 1047736,
  '50-59': 680012,
  '60-69': 420079,
  '70-79': 205312,
  '80+': 104488},
 'Hungary': {'0-9': 908567,
  '10-19': 969206,
  '20-29': 1151691,
  '30-39': 1257140,
  '40-49': 1588213,
  '50-59': 1201387,
  '60-69': 1306434,
  '70-79': 846578,
  '80+': 431135},
 'Iceland': {'0-9': 43070,
  '10-19': 44710,
  '20-29': 47796,
  '30-39': 46869,
  '40-49': 42966,
  '50-59': 42112,
  '60-69': 37536,
  '70-79': 23413,
  '80+': 12771},
 'India': {'0-9': 234861633,
  '10-19': 252201517,
  '20-29': 239902073,
  '30-39': 215636276,
  '40-49': 169660176,
  '50-59': 128132229,
  '60-69': 87150813,
  '70-79': 39175398,
  '80+': 13284270},
 'Indonesia': {'0-9': 47956444,
  '10-19': 46303002,
  '20-29': 43571426,
  '30-39': 41166623,
  '40-49': 37846723,
  '50-59': 29155099,
  '60-69': 17531210,
  '70-79': 7574475,
  '80+': 2418613},
 'Iran (Islamic Republic of)': {'0-9': 14565855,
  '10-19': 11747928,
  '20-29': 12342906,
  '30-39': 16739444,
  '40-49': 11655616,
  '50-59': 8295330,
  '60-69': 5396906,
  '70-79': 2354607,
  '80+': 894357},
 'Iraq': {'0-9': 10610228,
  '10-19': 8710756,
  '20-29': 7165589,
  '30-39': 5403684,
  '40-49': 3936617,
  '50-59': 2341151,
  '60-69': 1292393,
  '70-79': 573718,
  '80+': 188357},
 'Ireland': {'0-9': 671943,
  '10-19': 668746,
  '20-29': 567336,
  '30-39': 695926,
  '40-49': 763226,
  '50-59': 600934,
  '60-69': 480783,
  '70-79': 330663,
  '80+': 158229},
 'Israel': {'0-9': 1671094,
  '10-19': 1405063,
  '20-29': 1196974,
  '30-39': 1122245,
  '40-49': 1040178,
  '50-59': 795495,
  '60-69': 703645,
  '70-79': 459660,
  '80+': 261181},
 'Italy': {'0-9': 4994996,
  '10-19': 5733447,
  '20-29': 6103437,
  '30-39': 6998434,
  '40-49': 9022004,
  '50-59': 9567192,
  '60-69': 7484860,
  '70-79': 6028907,
  '80+': 4528548},
 'Jamaica': {'0-9': 464791,
  '10-19': 466600,
  '20-29': 515497,
  '30-39': 443384,
  '40-49': 357431,
  '50-59': 320532,
  '60-69': 214542,
  '70-79': 119523,
  '80+': 58867},
 'Japan': {'0-9': 10179968,
  '10-19': 11267171,
  '20-29': 12147325,
  '30-39': 14455415,
  '40-49': 18473078,
  '50-59': 16541516,
  '60-69': 15875236,
  '70-79': 16185375,
  '80+': 11351377},
 'Jordan': {'0-9': 2212563,
  '10-19': 2179854,
  '20-29': 1802535,
  '30-39': 1490607,
  '40-49': 1141344,
  '50-59': 755593,
  '60-69': 366276,
  '70-79': 190748,
  '80+': 63614},
 'Kazakhstan': {'0-9': 3868009,
  '10-19': 2720923,
  '20-29': 2573190,
  '30-39': 2993496,
  '40-49': 2286423,
  '50-59': 2039442,
  '60-69': 1438908,
  '70-79': 552508,
  '80+': 303808},
 'Kenya': {'0-9': 14013908,
  '10-19': 12746880,
  '20-29': 9594275,
  '30-39': 7470149,
  '40-49': 4903045,
  '50-59': 2805603,
  '60-69': 1518824,
  '70-79': 574335,
  '80+': 144277},
 'Kiribati': {'0-9': 29464,
  '10-19': 23634,
  '20-29': 20524,
  '30-39': 16606,
  '40-49': 11169,
  '50-59': 9988,
  '60-69': 5143,
  '70-79': 2331,
  '80+': 590},
 'Kosovo': {'0-9': 294038,
  '10-19': 306895,
  '20-29': 299672,
  '30-39': 237846,
  '40-49': 228757,
  '50-59': 189740,
  '60-69': 127956,
  '70-79': 71350,
  '80+': 32684},
 'Kuwait': {'0-9': 608328,
  '10-19': 533225,
  '20-29': 444882,
  '30-39': 878557,
  '40-49': 965368,
  '50-59': 561299,
  '60-69': 220263,
  '70-79': 48552,
  '80+': 10095},
 'Kyrgyzstan': {'0-9': 1529449,
  '10-19': 1100700,
  '20-29': 1082940,
  '30-39': 1014707,
  '40-49': 686437,
  '50-59': 581436,
  '60-69': 363825,
  '70-79': 111215,
  '80+': 53484},
 "Lao People's Democratic Republic": {'0-9': 1566742,
  '10-19': 1466251,
  '20-29': 1362624,
  '30-39': 1086530,
  '40-49': 772683,
  '50-59': 526580,
  '60-69': 317973,
  '70-79': 136165,
  '80+': 40012},
 'Latvia': {'0-9': 207770,
  '10-19': 188723,
  '20-29': 188221,
  '30-39': 263219,
  '40-49': 253889,
  '50-59': 264241,
  '60-69': 250143,
  '70-79': 162705,
  '80+': 107287},
 'Lebanon': {'0-9': 1152160,
  '10-19': 1134997,
  '20-29': 1176573,
  '30-39': 1009647,
  '40-49': 862746,
  '50-59': 724776,
  '60-69': 447766,
  '70-79': 211573,
  '80+': 105207},
 'Lesotho': {'0-9': 478747,
  '10-19': 428822,
  '20-29': 395193,
  '30-39': 327280,
  '40-49': 210253,
  '50-59': 140769,
  '60-69': 96810,
  '70-79': 48309,
  '80+': 16066},
 'Liberia': {'0-9': 1418817,
  '10-19': 1175027,
  '20-29': 840855,
  '30-39': 629808,
  '40-49': 444196,
  '50-59': 283827,
  '60-69': 168470,
  '70-79': 76455,
  '80+': 20226},
 'Libya': {'0-9': 1285422,
  '10-19': 1185747,
  '20-29': 1095417,
  '30-39': 1163468,
  '40-49': 1049198,
  '50-59': 617153,
  '60-69': 284261,
  '70-79': 138926,
  '80+': 51700},
 'Lithuania': {'0-9': 300673,
  '10-19': 242840,
  '20-29': 316879,
  '30-39': 337567,
  '40-49': 355907,
  '50-59': 420559,
  '60-69': 352811,
  '70-79': 223282,
  '80+': 171771},
 'Luxembourg': {'0-9': 65905,
  '10-19': 65903,
  '20-29': 85535,
  '30-39': 98316,
  '40-49': 94599,
  '50-59': 90857,
  '60-69': 62121,
  '70-79': 37874,
  '80+': 24867},
 'Madagascar': {'0-9': 7762934,
  '10-19': 6342928,
  '20-29': 4898736,
  '30-39': 3370908,
  '40-49': 2387857,
  '50-59': 1539765,
  '60-69': 915207,
  '70-79': 359863,
  '80+': 112819},
 'Malawi': {'0-9': 5662517,
  '10-19': 4738054,
  '20-29': 3377519,
  '30-39': 2286024,
  '40-49': 1436743,
  '50-59': 846147,
  '60-69': 480251,
  '70-79': 244240,
  '80+': 58457},
 'Malaysia': {'0-9': 5143191,
  '10-19': 5115769,
  '20-29': 5770367,
  '30-39': 5651218,
  '40-49': 3990530,
  '50-59': 3146037,
  '60-69': 2151364,
  '70-79': 1025182,
  '80+': 372341},
 'Maldives': {'0-9': 72820,
  '10-19': 59438,
  '20-29': 139684,
  '30-39': 137607,
  '40-49': 64647,
  '50-59': 35317,
  '60-69': 18164,
  '70-79': 8467,
  '80+': 4400},
 'Mali': {'0-9': 6760318,
  '10-19': 5009462,
  '20-29': 3203821,
  '30-39': 2160455,
  '40-49': 1485960,
  '50-59': 849115,
  '60-69': 501293,
  '70-79': 231083,
  '80+': 49326},
 'Malta': {'0-9': 43103,
  '10-19': 40926,
  '20-29': 55214,
  '30-39': 65354,
  '40-49': 59448,
  '50-59': 53214,
  '60-69': 57678,
  '70-79': 45166,
  '80+': 21440},
 'Martinique': {'0-9': 35951,
  '10-19': 47121,
  '20-29': 41372,
  '30-39': 34103,
  '40-49': 44188,
  '50-59': 62795,
  '60-69': 52466,
  '70-79': 33674,
  '80+': 23595},
 'Mauritania': {'0-9': 1307828,
  '10-19': 1007554,
  '20-29': 787903,
  '30-39': 619780,
  '40-49': 422633,
  '50-59': 267150,
  '60-69': 151072,
  '70-79': 67185,
  '80+': 18553},
 'Mauritius': {'0-9': 132887,
  '10-19': 175164,
  '20-29': 196809,
  '30-39': 175108,
  '40-49': 182089,
  '50-59': 175349,
  '60-69': 137990,
  '70-79': 69212,
  '80+': 27160},
 'Mayotte': {'0-9': 71475,
  '10-19': 64566,
  '20-29': 43626,
  '30-39': 32985,
  '40-49': 27349,
  '50-59': 16167,
  '60-69': 9373,
  '70-79': 4999,
  '80+': 2275},
 'Mexico': {'0-9': 22169248,
  '10-19': 22350465,
  '20-29': 21735593,
  '30-39': 18880028,
  '40-49': 16547760,
  '50-59': 12757973,
  '60-69': 8264954,
  '70-79': 4188714,
  '80+': 2038018},
 'Micronesia (Federated States of)': {'0-9': 24050,
  '10-19': 23299,
  '20-29': 22347,
  '30-39': 15087,
  '40-49': 11429,
  '50-59': 9786,
  '60-69': 6733,
  '70-79': 1930,
  '80+': 362},
 'Mongolia': {'0-9': 737476,
  '10-19': 500441,
  '20-29': 500018,
  '30-39': 564279,
  '40-49': 423046,
  '50-59': 314050,
  '60-69': 158364,
  '70-79': 59891,
  '80+': 20725},
 'Montenegro': {'0-9': 73945,
  '10-19': 78536,
  '20-29': 84197,
  '30-39': 88348,
  '40-49': 83921,
  '50-59': 80322,
  '60-69': 76947,
  '70-79': 40438,
  '80+': 21412},
 'Morocco': {'0-9': 6752613,
  '10-19': 6097197,
  '20-29': 5883282,
  '30-39': 5606357,
  '40-49': 4452433,
  '50-59': 3743784,
  '60-69': 2735019,
  '70-79': 1197076,
  '80+': 442799},
 'Mozambique': {'0-9': 9717781,
  '10-19': 7595457,
  '20-29': 5294496,
  '30-39': 3588739,
  '40-49': 2289290,
  '50-59': 1400167,
  '60-69': 843662,
  '70-79': 420844,
  '80+': 104999},
 'Myanmar': {'0-9': 9021262,
  '10-19': 9916644,
  '20-29': 9163079,
  '30-39': 8073003,
  '40-49': 7219972,
  '50-59': 5573219,
  '60-69': 3603964,
  '70-79': 1423032,
  '80+': 415625},
 'Namibia': {'0-9': 654524,
  '10-19': 526434,
  '20-29': 472709,
  '30-39': 356845,
  '40-49': 237555,
  '50-59': 150335,
  '60-69': 87459,
  '70-79': 41131,
  '80+': 13913},
 'Nepal': {'0-9': 5462982,
  '10-19': 6120130,
  '20-29': 5886374,
  '30-39': 3792740,
  '40-49': 3045655,
  '50-59': 2307701,
  '60-69': 1488078,
  '70-79': 811531,
  '80+': 221617},
 'Netherlands': {'0-9': 1752759,
  '10-19': 1953692,
  '20-29': 2097478,
  '30-39': 2097533,
  '40-49': 2151439,
  '50-59': 2524073,
  '60-69': 2129499,
  '70-79': 1591523,
  '80+': 836876},
 'New Caledonia': {'0-9': 41312,
  '10-19': 43203,
  '20-29': 43195,
  '30-39': 41492,
  '40-49': 40824,
  '50-59': 34952,
  '60-69': 22796,
  '70-79': 13302,
  '80+': 4422},
 'New Zealand': {'0-9': 615286,
  '10-19': 624953,
  '20-29': 671233,
  '30-39': 619065,
  '40-49': 591875,
  '50-59': 628690,
  '60-69': 522312,
  '70-79': 361834,
  '80+': 186985},
 'Nicaragua': {'0-9': 1317147,
  '10-19': 1240161,
  '20-29': 1165998,
  '30-39': 1055451,
  '40-49': 763037,
  '50-59': 507320,
  '60-69': 348753,
  '70-79': 150503,
  '80+': 76184},
 'Niger': {'0-9': 8758024,
  '10-19': 5901126,
  '20-29': 3717358,
  '30-39': 2259019,
  '40-49': 1528697,
  '50-59': 1046847,
  '60-69': 644750,
  '70-79': 295959,
  '80+': 54863},
 'Nigeria': {'0-9': 63852440,
  '10-19': 47703190,
  '20-29': 33177419,
  '30-39': 24368050,
  '40-49': 17037463,
  '50-59': 10700169,
  '60-69': 6258527,
  '70-79': 2623704,
  '80+': 418627},
 'Norway': {'0-9': 614323,
  '10-19': 643032,
  '20-29': 726383,
  '30-39': 738722,
  '40-49': 724932,
  '50-59': 712508,
  '60-69': 586156,
  '70-79': 446446,
  '80+': 228739},
 'Oman': {'0-9': 832571,
  '10-19': 530302,
  '20-29': 1085546,
  '30-39': 1439821,
  '40-49': 684970,
  '50-59': 315603,
  '60-69': 142788,
  '70-79': 53058,
  '80+': 21967},
 'Pakistan': {'0-9': 53462231,
  '10-19': 45427436,
  '20-29': 39930365,
  '30-39': 30816025,
  '40-49': 21248749,
  '50-59': 15122610,
  '60-69': 8902414,
  '70-79': 4558931,
  '80+': 1423578},
 'Panama': {'0-9': 773776,
  '10-19': 726611,
  '20-29': 678255,
  '30-39': 618598,
  '40-49': 556394,
  '50-59': 432978,
  '60-69': 282630,
  '70-79': 157808,
  '80+': 87717},
 'Papua New Guinea': {'0-9': 2150349,
  '10-19': 1917879,
  '20-29': 1554186,
  '30-39': 1220537,
  '40-49': 938383,
  '50-59': 629120,
  '60-69': 372086,
  '70-79': 136653,
  '80+': 27831},
 'Paraguay': {'0-9': 1383914,
  '10-19': 1336278,
  '20-29': 1321044,
  '30-39': 1109127,
  '40-49': 727641,
  '50-59': 548361,
  '60-69': 402162,
  '70-79': 213726,
  '80+': 90284},
 'Peru': {'0-9': 5445401,
  '10-19': 5134606,
  '20-29': 5375787,
  '30-39': 5231161,
  '40-49': 4346665,
  '50-59': 3313880,
  '60-69': 2276639,
  '70-79': 1255406,
  '80+': 592307},
 'Philippines': {'0-9': 22014291,
  '10-19': 21369694,
  '20-29': 19584112,
  '30-39': 15501925,
  '40-49': 12311228,
  '50-59': 9366918,
  '60-69': 5878871,
  '70-79': 2639622,
  '80+': 914417},
 'Poland': {'0-9': 3784870,
  '10-19': 3709138,
  '20-29': 4431561,
  '30-39': 6004923,
  '40-49': 5535441,
  '50-59': 4563170,
  '60-69': 5174147,
  '70-79': 2900526,
  '80+': 1742835},
 'Portugal': {'0-9': 841075,
  '10-19': 1015167,
  '20-29': 1073698,
  '30-39': 1215310,
  '40-49': 1575910,
  '50-59': 1481008,
  '60-69': 1293823,
  '70-79': 1018315,
  '80+': 682403},
 'Puerto Rico': {'0-9': 240324,
  '10-19': 394671,
  '20-29': 288754,
  '30-39': 331516,
  '40-49': 399245,
  '50-59': 414187,
  '60-69': 361026,
  '70-79': 273683,
  '80+': 157447},
 'Qatar': {'0-9': 270534,
  '10-19': 228399,
  '20-29': 717369,
  '30-39': 846180,
  '40-49': 461797,
  '50-59': 254159,
  '60-69': 81798,
  '70-79': 16725,
  '80+': 4092},
 'Republic of Korea': {'0-9': 4153813,
  '10-19': 4753259,
  '20-29': 6716295,
  '30-39': 7079840,
  '40-49': 8218845,
  '50-59': 8476698,
  '60-69': 6453706,
  '70-79': 3560645,
  '80+': 1856084},
 'Republic of Moldova': {'0-9': 424059,
  '10-19': 419285,
  '20-29': 570832,
  '30-39': 773875,
  '40-49': 562809,
  '50-59': 521014,
  '60-69': 488289,
  '70-79': 184990,
  '80+': 88810},
 'Romania': {'0-9': 1905045,
  '10-19': 2075305,
  '20-29': 2086267,
  '30-39': 2585899,
  '40-49': 3026469,
  '50-59': 2569160,
  '60-69': 2535949,
  '70-79': 1530270,
  '80+': 923327},
 'Russian Federation': {'0-9': 18622607,
  '10-19': 15256035,
  '20-29': 15607785,
  '30-39': 24468554,
  '40-49': 20375320,
  '50-59': 18897667,
  '60-69': 18501370,
  '70-79': 8549716,
  '80+': 5655408},
 'Rwanda': {'0-9': 3561022,
  '10-19': 2905796,
  '20-29': 2211046,
  '30-39': 1812553,
  '40-49': 1070096,
  '50-59': 728451,
  '60-69': 445152,
  '70-79': 174816,
  '80+': 43285},
 'Réunion': {'0-9': 132395,
  '10-19': 138862,
  '20-29': 118273,
  '30-39': 99451,
  '40-49': 117324,
  '50-59': 125415,
  '60-69': 90557,
  '70-79': 47535,
  '80+': 25500},
 'Saint Lucia': {'0-9': 21813,
  '10-19': 24336,
  '20-29': 32816,
  '30-39': 28448,
  '40-49': 25516,
  '50-59': 23375,
  '60-69': 14556,
  '70-79': 8355,
  '80+': 4412},
 'Saint Vincent and the Grenadines': {'0-9': 15945,
  '10-19': 17425,
  '20-29': 17503,
  '30-39': 15712,
  '40-49': 14485,
  '50-59': 13587,
  '60-69': 9176,
  '70-79': 4503,
  '80+': 2604},
 'Samoa': {'0-9': 51121,
  '10-19': 42003,
  '20-29': 31297,
  '30-39': 22010,
  '40-49': 19559,
  '50-59': 16472,
  '60-69': 9961,
  '70-79': 4578,
  '80+': 1413},
 'Sao Tome and Principe': {'0-9': 62410,
  '10-19': 54109,
  '20-29': 33623,
  '30-39': 26630,
  '40-49': 18680,
  '50-59': 12781,
  '60-69': 7083,
  '70-79': 2763,
  '80+': 1080},
 'Saudi Arabia': {'0-9': 5956215,
  '10-19': 4860281,
  '20-29': 5354763,
  '30-39': 6980363,
  '40-49': 6408790,
  '50-59': 3216573,
  '60-69': 1373521,
  '70-79': 493856,
  '80+': 169509},
 'Senegal': {'0-9': 5032581,
  '10-19': 3863701,
  '20-29': 2823536,
  '30-39': 2051292,
  '40-49': 1331829,
  '50-59': 834697,
  '60-69': 505761,
  '70-79': 239181,
  '80+': 61349},
 'Serbia': {'0-9': 855818,
  '10-19': 999733,
  '20-29': 1102466,
  '30-39': 1214888,
  '40-49': 1229894,
  '50-59': 1121507,
  '60-69': 1142469,
  '70-79': 729682,
  '80+': 340914},
 'Seychelles': {'0-9': 15935,
  '10-19': 13867,
  '20-29': 13431,
  '30-39': 14488,
  '40-49': 14873,
  '50-59': 12978,
  '60-69': 7911,
  '70-79': 3205,
  '80+': 1659},
 'Sierra Leone': {'0-9': 2225885,
  '10-19': 1867195,
  '20-29': 1405514,
  '30-39': 1017051,
  '40-49': 672892,
  '50-59': 419133,
  '60-69': 234027,
  '70-79': 108809,
  '80+': 26477},
 'Singapore': {'0-9': 479039,
  '10-19': 505791,
  '20-29': 833056,
  '30-39': 896616,
  '40-49': 964875,
  '50-59': 946223,
  '60-69': 799325,
  '70-79': 289630,
  '80+': 135787},
 'Slovakia': {'0-9': 566590,
  '10-19': 545493,
  '20-29': 655787,
  '30-39': 847604,
  '40-49': 861400,
  '50-59': 709218,
  '60-69': 695209,
  '70-79': 398709,
  '80+': 179632},
 'Slovenia': {'0-9': 210171,
  '10-19': 196378,
  '20-29': 205492,
  '30-39': 283648,
  '40-49': 305327,
  '50-59': 301204,
  '60-69': 284942,
  '70-79': 177497,
  '80+': 114279},
 'Solomon Islands': {'0-9': 196169,
  '10-19': 148827,
  '20-29': 111830,
  '30-39': 82051,
  '40-49': 68670,
  '50-59': 40695,
  '60-69': 22979,
  '70-79': 11993,
  '80+': 3670},
 'Somalia': {'0-9': 5215365,
  '10-19': 3937588,
  '20-29': 2693878,
  '30-39': 1534402,
  '40-49': 1053897,
  '50-59': 733973,
  '60-69': 462792,
  '70-79': 210106,
  '80+': 51221},
 'South Africa': {'0-9': 11585606,
  '10-19': 10409174,
  '20-29': 10141490,
  '30-39': 10155325,
  '40-49': 7043274,
  '50-59': 4911530,
  '60-69': 3164440,
  '70-79': 1476055,
  '80+': 421796},
 'South Sudan': {'0-9': 3245684,
  '10-19': 2581903,
  '20-29': 1962948,
  '30-39': 1334152,
  '40-49': 896838,
  '50-59': 595522,
  '60-69': 344938,
  '70-79': 182625,
  '80+': 49115},
 'Spain': {'0-9': 4234486,
  '10-19': 4736076,
  '20-29': 4617599,
  '30-39': 5901992,
  '40-49': 7938499,
  '50-59': 7046327,
  '60-69': 5340654,
  '70-79': 4015304,
  '80+': 2923841},
 'Sri Lanka': {'0-9': 3350035,
  '10-19': 3386220,
  '20-29': 2901858,
  '30-39': 2820020,
  '40-49': 2881105,
  '50-59': 2554817,
  '60-69': 2013196,
  '70-79': 1146337,
  '80+': 359661},
 'State of Palestine': {'0-9': 1364529,
  '10-19': 1109494,
  '20-29': 965726,
  '30-39': 664295,
  '40-49': 448138,
  '50-59': 297319,
  '60-69': 151853,
  '70-79': 77833,
  '80+': 22227},
 'Sudan': {'0-9': 12128803,
  '10-19': 10123658,
  '20-29': 7627155,
  '30-39': 5203245,
  '40-49': 3727317,
  '50-59': 2552951,
  '60-69': 1535958,
  '70-79': 733051,
  '80+': 217121},
 'Suriname': {'0-9': 104833,
  '10-19': 102229,
  '20-29': 95774,
  '30-39': 82789,
  '40-49': 72724,
  '50-59': 64826,
  '60-69': 36928,
  '70-79': 18682,
  '80+': 7847},
 'Sweden': {'0-9': 1193952,
  '10-19': 1127126,
  '20-29': 1276929,
  '30-39': 1320296,
  '40-49': 1264123,
  '50-59': 1296645,
  '60-69': 1093869,
  '70-79': 994243,
  '80+': 532082},
 'Switzerland': {'0-9': 884945,
  '10-19': 834866,
  '20-29': 1039727,
  '30-39': 1219227,
  '40-49': 1166590,
  '50-59': 1320623,
  '60-69': 977436,
  '70-79': 751994,
  '80+': 459214},
 'Syrian Arab Republic': {'0-9': 3635906,
  '10-19': 3325125,
  '20-29': 3099981,
  '30-39': 2907195,
  '40-49': 1928900,
  '50-59': 1285347,
  '60-69': 822366,
  '70-79': 355547,
  '80+': 140291},
 'Taiwan Province of China': {'0-9': 2052885,
  '10-19': 2188808,
  '20-29': 3120353,
  '30-39': 3548586,
  '40-49': 3787845,
  '50-59': 3659220,
  '60-69': 3101016,
  '70-79': 1488802,
  '80+': 869260},
 'Tajikistan': {'0-9': 2577608,
  '10-19': 1788370,
  '20-29': 1648520,
  '30-39': 1390332,
  '40-49': 882400,
  '50-59': 700892,
  '60-69': 387890,
  '70-79': 117606,
  '80+': 44027},
 'Thailand': {'0-9': 7439833,
  '10-19': 8492312,
  '20-29': 9630311,
  '30-39': 9229726,
  '40-49': 10914254,
  '50-59': 10681391,
  '60-69': 7624358,
  '70-79': 3866567,
  '80+': 1921226},
 'The former Yugoslav Republic of Macedonia': {'0-9': 227550,
  '10-19': 233451,
  '20-29': 282982,
  '30-39': 325975,
  '40-49': 299904,
  '50-59': 282831,
  '60-69': 244647,
  '70-79': 133880,
  '80+': 52154},
 'Timor-Leste': {'0-9': 331877,
  '10-19': 306717,
  '20-29': 244908,
  '30-39': 159027,
  '40-49': 100789,
  '50-59': 88473,
  '60-69': 50144,
  '70-79': 28916,
  '80+': 7594},
 'Togo': {'0-9': 2340180,
  '10-19': 1914993,
  '20-29': 1375262,
  '30-39': 1064553,
  '40-49': 744517,
  '50-59': 450710,
  '60-69': 255935,
  '70-79': 111491,
  '80+': 21083},
 'Tonga': {'0-9': 24640,
  '10-19': 23525,
  '20-29': 17138,
  '30-39': 12181,
  '40-49': 10289,
  '50-59': 8701,
  '60-69': 5304,
  '70-79': 2791,
  '80+': 1126},
 'Trinidad and Tobago': {'0-9': 184450,
  '10-19': 185807,
  '20-29': 183001,
  '30-39': 242864,
  '40-49': 191443,
  '50-59': 175059,
  '60-69': 135895,
  '70-79': 73653,
  '80+': 27316},
 'Tunisia': {'0-9': 2017758,
  '10-19': 1639937,
  '20-29': 1725345,
  '30-39': 1914066,
  '40-49': 1572474,
  '50-59': 1361507,
  '60-69': 962594,
  '70-79': 424105,
  '80+': 200832},
 'Turkey': {'0-9': 13419270,
  '10-19': 13595150,
  '20-29': 13174164,
  '30-39': 12774732,
  '40-49': 11446581,
  '50-59': 8908423,
  '60-69': 6192391,
  '70-79': 3353577,
  '80+': 1474778},
 'Turkmenistan': {'0-9': 1332932,
  '10-19': 1008742,
  '20-29': 1009792,
  '30-39': 957887,
  '40-49': 697821,
  '50-59': 535461,
  '60-69': 334447,
  '70-79': 103460,
  '80+': 50658},
 'Uganda': {'0-9': 14855951,
  '10-19': 11449426,
  '20-29': 7872675,
  '30-39': 5101102,
  '40-49': 3133402,
  '50-59': 1852437,
  '60-69': 974327,
  '70-79': 411999,
  '80+': 89688},
 'Ukraine': {'0-9': 4589511,
  '10-19': 4383518,
  '20-29': 4898491,
  '30-39': 7208959,
  '40-49': 6406401,
  '50-59': 5906740,
  '60-69': 5539857,
  '70-79': 2983432,
  '80+': 1816853},
 'United Arab Emirates': {'0-9': 1011712,
  '10-19': 842993,
  '20-29': 2149345,
  '30-39': 3169316,
  '40-49': 1608106,
  '50-59': 797911,
  '60-69': 242705,
  '70-79': 55883,
  '80+': 12431},
 'United Kingdom of Great Britain and Northern Ireland': {'0-9': 8044056,
  '10-19': 7642475,
  '20-29': 8558707,
  '30-39': 9295025,
  '40-49': 8604251,
  '50-59': 9173467,
  '60-69': 7286778,
  '70-79': 5830636,
  '80+': 3450616},
 'United Republic of Tanzania': {'0-9': 18362315,
  '10-19': 14089046,
  '20-29': 9846249,
  '30-39': 7161926,
  '40-49': 4820729,
  '50-59': 2926636,
  '60-69': 1622801,
  '70-79': 741234,
  '80+': 163282},
 'United States Virgin Islands': {'0-9': 12866,
  '10-19': 14018,
  '20-29': 12732,
  '30-39': 9733,
  '40-49': 11766,
  '50-59': 14450,
  '60-69': 14020,
  '70-79': 10901,
  '80+': 3939},
 'United States of America': {'0-9': 39721484,
  '10-19': 42332393,
  '20-29': 46094077,
  '30-39': 44668271,
  '40-49': 40348398,
  '50-59': 42120077,
  '60-69': 38488173,
  '70-79': 24082598,
  '80+': 13147180},
 'Uruguay': {'0-9': 473071,
  '10-19': 478929,
  '20-29': 511559,
  '30-39': 461146,
  '40-49': 455021,
  '50-59': 391074,
  '60-69': 327921,
  '70-79': 220267,
  '80+': 154741},
 'Uzbekistan': {'0-9': 6713724,
  '10-19': 5460857,
  '20-29': 5946988,
  '30-39': 5577195,
  '40-49': 3930502,
  '50-59': 3068759,
  '60-69': 1939630,
  '70-79': 572151,
  '80+': 259397},
 'Vanuatu': {'0-9': 80884,
  '10-19': 66925,
  '20-29': 50769,
  '30-39': 41001,
  '40-49': 29192,
  '50-59': 20541,
  '60-69': 11438,
  '70-79': 4837,
  '80+': 1558},
 'Venezuela (Bolivarian Republic of)': {'0-9': 5094601,
  '10-19': 5158570,
  '20-29': 4130338,
  '30-39': 4027919,
  '40-49': 3564976,
  '50-59': 3014982,
  '60-69': 2042554,
  '70-79': 989858,
  '80+': 412141},
 'Viet Nam': {'0-9': 15478572,
  '10-19': 13599041,
  '20-29': 15389495,
  '30-39': 16200926,
  '40-49': 13572964,
  '50-59': 11109965,
  '60-69': 7342685,
  '70-79': 2778470,
  '80+': 1866461},
 'Western Sahara': {'0-9': 112592,
  '10-19': 98369,
  '20-29': 104987,
  '30-39': 108717,
  '40-49': 82796,
  '50-59': 51955,
  '60-69': 28373,
  '70-79': 7614,
  '80+': 1936},
 'Yemen': {'0-9': 8033406,
  '10-19': 6750274,
  '20-29': 5732747,
  '30-39': 4140438,
  '40-49': 2362805,
  '50-59': 1422834,
  '60-69': 879448,
  '70-79': 403471,
  '80+': 100540},
 'Zambia': {'0-9': 5663541,
  '10-19': 4550182,
  '20-29': 3180383,
  '30-39': 2185196,
  '40-49': 1413887,
  '50-59': 761262,
  '60-69': 403835,
  '70-79': 179963,
  '80+': 45706},
 'Zimbabwe': {'0-9': 4308157,
  '10-19': 3559952,
  '20-29': 2482990,
  '30-39': 1867477,
  '40-49': 1257821,
  '50-59': 698090,
  '60-69': 425415,
  '70-79': 200359,
  '80+': 62663}
  }