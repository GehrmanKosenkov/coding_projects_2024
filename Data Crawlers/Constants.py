

# The 'dates' list contains mappings of date labels as they appear in a crawled Excel file to their corresponding ISO 8601 formatted date strings. The date labels in the keys are in a mixed 
# format with Turkish and English month names followed by the year, while the values are the last day of the corresponding month in the YYYY-MM-DD format. This conversion is useful for:
# 1. Clarity: The ISO 8601 date format (YYYY-MM-DD) is more standardized and easier to work with in data processing and database operations.
# 2. Data Retrieval: Allows for easy and accurate retrieval of lines of data associated with each date from the Excel file.
# 3. Database Insertion: Simplifies the process of inserting dates into databases, as the ISO format is widely accepted and used in most database systems.

dates = [
    {"Temmuz/July 2023": "2023-07-31"},
    {"Ağustos/August 2023": "2023-08-31"},
    {"Eylül/September 2023": "2023-09-30"},
    {"Ekim/October 2023": "2023-10-31"},
    {"Kasım/November 2023": "2023-11-30"},
    {"Aralık/December 2023": "2023-12-31"},
    {"Ocak/January 2024": "2024-01-31"},
    {"Şubat/February 2024": "2024-02-28"},
    {"Mart/March 2024": "2024-03-31"},
    {"Nisan/April 2024": "2024-04-30"},
    {"Mayıs/May 2024": "2024-05-31"},
    {"Haziran/June 2024": "2024-06-30"}
]

# The 'countries' list contains mappings of country names as they appear in the crawled Excel file to their corresponding country codes used in the database. 
# The country names in the keys are in a mixed format with Turkish and English names followed by their ISO 3166-1 alpha-2 codes, while the values are the corresponding country codes 
# from the database. This conversion is necessary for:
# 1. Consistency: Ensures that the country names from the Excel file match the standardized country codes in the database, maintaining consistency in the data representation.
# 2. Data Retrieval: Allows for accurate retrieval of lines of data associated with each country from the Excel file.
# 3. Database Insertion: Simplifies the process of inserting data into the database, as the country codes are standardized 
# 4. Despite the method being bulky, it is necessary to handle the varied country names and codes properly for seamless data integration between the Excel file and the database

countries = [
    {"Ukrayna/UA": 184},
    {"Rusya/RU": 150},
    {"Moldova/MD": 119},
    {"Romanya/RO": 149},
    {"Avusturya/AT": 14},
    {"Azerbaycan/AZ": 15},
    {"Bahamas/BS": 16},
    {"Bahreyn/BH": 17},
    {"Bangladeş/BD": 18},
    {"Barbados/BB": 19},
    {"Belarus/BY": 20},
    {"Belçika/BE": 21},
    {"Belize/BZ": 22},
    {"Benin/BJ": 23},
    {"Bermuda/BM": 24},
    {"Butan/BT": 25},
    {"Bolivya/BO": 26},
    {"Bosna Hersek/BOS": 27},
    {"Botsvana/BW": 28},
    {"Brezilya/BR": 29},
    {"Bulgaristan/BG": 30},
    {"Burkina Faso/BF": 31},
    {"Burundi/BI": 32},
    {"Kamboçya/KH": 33},
    {"Kamerun/CM": 34},
    {"Cayman Adaları/KY": 35},
    {"Orta Afrika Cumhuriyeti/CF": 36},
    {"Çad/TD": 37},
    {"Şili/CL": 38},
    {"Çin/CN": 39},
    {"Kolombiya/CO": 40},
    {"Komorlar/KM": 41},
    {"Kongo DC/CD": 42},
    {"Kosta Rika/CR": 43},
    {"Hırvatistan/HR": 44},
    {"Küba/CU": 45},
    {"Kıbrıs/CY": 46},
    {"Çek Cumhuriyeti/CZ": 47},
    {"Danimarka/DK": 48},
    {"Cibuti/DJ": 49},
    {"Dominika/DM": 50},
    {"Dominik Cumhuriyeti/DO": 51},
    {"Ekvador/EC": 52},
    {"Mısır/EG": 53},
    {"El Salvador/SV": 54},
    {"Ekvator Ginesi/GQ": 55},
    {"Eritre/ER": 56},
    {"Estonya/EE": 57},
    {"Etiyopya/ET": 58},
    {"Faroe Adaları/FO": 59},
    {"Fiji/FJ": 60},
    {"Finlandiya/FI": 61},
    {"Fransa/FR": 62},
    {"Gabon/GA": 63},
    {"Gambiya/GM": 64},
    {"Gürcistan/GEOR": 65},
    {"Almanya/DE": 66},
    {"Gana/GH": 67},
    {"Cebelitarık/GI": 68},
    {"Yunanistan/GR": 69},
    {"Grönland/GL": 70},
    {"Grenada/GD": 71},
    {"Guam/GU": 72},
    {"Guatemala/GT": 73},
    {"Guyana/GY": 74},
    {"Haiti/HT": 75},
    {"Honduras/HN": 76},
    {"Hong Kong SAR/HK": 77},
    {"Macaristan/HU": 78},
    {"İzlanda/IS": 79},
    {"Hindistan/IN": 80},
    {"Endonezya/ID": 81},
    {"İran/IR": 82},
    {"Irak/IQ": 83},
    {"İrlanda/IE": 84},
    {"İsrail/IL": 85},
    {"İtalya/IT": 86},
    {"Jamaika/JM": 87},
    {"Japonya/JP": 88},
    {"Ürdün/JO": 89},
    {"Kazakistan/KZ": 90},
    {"Kenya/KE": 91},
    {"Kiribati/KI": 92},
    {"Güney Kore/KR": 93},
    {"Kosova/XK": 94},
    {"Kuveyt/KW": 95},
    {"Kırgızistan/KG": 96},
    {"Laos/LA": 97},
    {"Letonya/LV": 98},
    {"Lübnan/LB": 99},
    {"Lesotho/LS": 100},
    {"Liberya/LR": 101},
    {"Libya/LY": 102},
    {"Lihtenştayn/LI": 103},
    {"Litvanya/LT": 104},
    {"Lüksemburg/LU": 105},
    {"Macao SAR/MO": 106},
    {"Madagaskar/MG": 107},
    {"Malavi/MW": 108},
    {"Malezya/MY": 109},
    {"Maldivler/MV": 110},
    {"Mali/ML": 111},
    {"Malta/MT": 112},
    {"Marshall Adaları/MH": 113},
    {"Moritanya/MR": 114},
    {"Mauritius/MU": 115},
    {"Meksika/MX": 116},
    {"Moldova/MD": 117},
    {"Monako/MC": 118},
    {"Mongolistan/MN": 119},
    {"Karadağ/ME": 120},
    {"Fas/MA": 121},
    {"Mozambik/MZ": 122},
    {"Myanmar/MM": 123},
    {"Namibya/NA": 124},
    {"Nauru/NR": 125},
    {"Nepal/NP": 126},
    {"Hollanda/NL": 127},
    {"Yeni Kaledonya/NC": 128},
    {"Yeni Zelanda/NZ": 129},
    {"Nikaragua/NI": 130},
    {"Nijer/NE": 131},
    {"Nijerya/NG": 132},
    {"Norveç/NO": 133},
    {"Umman/OM": 134},
    {"Pakistan/PK": 135},
    {"Palau/PW": 136},
    {"Panama/PA": 137},
    {"Papua Yeni Gine/PG": 138},
    {"Paraguay/PY": 139},
    {"Peru/PE": 140},
    {"Filipinler/PH": 141},
    {"Polonya/PL": 142},
    {"Portekiz/PT": 143},
    {"Porto Riko/PR": 144},
    {"Katar/QA": 145},
    {"Romanya/RO": 146},
    {"Ruanda/RW": 148},
    {"Saint Kitts ve Nevis/KN": 149},
    {"Saint Lucia/LC": 150},
    {"Saint Vincent ve Grenadinler/VC": 151},
    {"Saint Pierre ve Miquelon/PM": 152},
    {"Samoa/WS": 153},
    {"San Marino/SM": 154},
    {"Sao Tome ve Principe/ST": 155},
    {"Suudi Arabistan/SA": 156},
    {"Senegal/SN": 157},
    {"Sırbistan/SER": 158},
    {"Seyşeller/SC": 159},
    {"Sierra Leone/SL": 160},
    {"Singapur/SG": 161},
    {"Slovakya/SK": 162},
    {"Slovenya/SI": 163},
    {"Solomon Adaları/SB": 164},
    {"Somali/SO": 165},
    {"Güney Afrika/ZA": 166},
    {"İspanya/ES": 167},
    {"Sri Lanka/LK": 168},
    {"Sudan/SD": 169},
    {"Surinam/SR": 170},
    {"Svaziland/SZ": 171},
    {"İsveç/SE": 172},
    {"İsviçre/CH": 173},
    {"Suriye/SY": 174},
    {"Tayvan/TW": 175},
    {"Tacikistan/TJ": 176},
    {"Tanzanya/TZ": 177},
    {"Tayland/TH": 178},
    {"Togo/TG": 179},
    {"Tonga/TO": 180},
    {"Trinidad ve Tobago/TT": 181},
    {"Tunus/TN": 182},
    {"Türkiye/TR": 183},
    {"Türkmenistan/TM": 184},
    {"Tuvalu/TV": 185},
    {"Uganda/UG": 186},
    {"Birleşik Arap Emirlikleri/AE": 188},
    {"Uruguay/UY": 189},
    {"Özbekistan/UZ": 190},
    {"Vanuatu/VU": 191},
    {"Venezuela/VE": 192},
    {"Vietnam/VN": 193},
    {"Virgin Adaları, Britanya/VG": 194},
    {"Virgin Adaları, Amerika/VI": 195},
    {"Yemen/YE": 196},
    {"Zambiya/ZM": 197},
    {"Zimbabve/ZW": 198},
    {"Avrupa 28/EU-28": 199},
    {"Avrupa 27/EU-27": 200},
    {"Birleşik Krallık/UK": 201},
    {"Küresel Süt Ticareti/GDT": 202},
    {"Fransa - ATLA/ATLA": 203},
    {"Beneluks/BE-NE-LU": 204},
    {"Küresel/Global": 205},
    {"Doğu AB/East-EU": 206},
    {"LATAM/LATAM": 207},
    {"Okyanusya/Oceania": 208},
    {"ABD CLS raporu/US CLS report": 209},
    {"ABD - NDP/United States - NDP": 210},
    {"Cape Verde/CV": 211},
    {"Brunei/BN": 212},
    {"Cook Adaları/CK": 213},
    {"Fildişi Sahili/CI": 214},
    {"Fransız Polinezyası/PF": 215},
    {"Gine/GN": 216},
    {"Gine-Bissau/GW": 217},
    {"Kuzey Kore/KP": 218},
    {"Mayotte/YT": 219},
    {"Mikronezya/FS": 220},
    {"Saint Kitts ve Nevis/KN": 221},
    {"Saint Lucia/LC": 222},
    {"Saint Vincent ve Grenadinler/VC": 223},
    {"Saint Pierre ve Miquelon/PM": 224},
    {"Samoa/WS": 225},
    {"Swaziland/SZ": 226},
    {"Doğu Timor/TL": 227},
    {"Wallis ve Futuna Adaları/WF": 228},
    {"Belirsiz/Unspecified": 229},
    {"Avrupa Ekonomik Alanı/EEA": 230},
    {"Britanya Hint Okyanusu Toprakları/IO": 231},
    {"Fransız Güney Toprakları/TF": 232},
    {"Asya/Asia": 233},
    {"Mercosur/Mercosur": 234},
    {"Orta Doğu/Middle East": 235},
    {"Kuzey Afrika/North Africa": 236},
    {"Kuzey Amerika/North America": 237},
    {"Güney Amerika/South America": 238},
    {"Orta Amerika/Central America": 239},
    {"Kuzeydoğu Asya/Northeast Asia": 240},
    {"Merkez Güney Asya/Central South Asia": 241},
    {"Güneydoğu Asya/Southeast Asia": 242},
    {"EAEB/EAEU": 243},
    {"Sahra Altı Afrika/Sub-saharan Africa": 244},
    {"Dünya/World": 245},
    {"ABD (Ortabatı)/United States (Midwest)": 246},
    {"ABD (Kuzeydoğu)/United States (Northeast)": 247},
    {"ABD (Güney)/United States (South)": 248},
    {"ABD (Batı)/United States (West)": 249},
    {"Batı AB/West-EU": 250}
]


products_matched = {
    "Sunseed": 263,
    "Sunoil": 859,
    "Sunmeal": 846,
    "Soybean": 244,
    "Soyoil": 93,
    "Soymeal": 92,
    "Rapeseed": 282,
    "Rapeoil": 288,
    "Rapemeal": 828
}

dates_23_24 = {
    'SEP': '2023-09-30',
    'OCT': '2023-10-31',
    'NOV': '2023-11-30',
    'DEC': '2023-12-31',
    'JAN': '2024-01-31',
    'FEB': '2024-02-28',
    'MAR': '2024-03-31',
    'APR': '2024-04-30',
    'MAY': '2024-05-31',
    'JUN': '2024-06-30',
    'JUL': '2024-07-31',
    'AUG': '2024-08-31'
}

dates_22_23 = {
    'SEP': '2022-09-30',
    'OCT': '2022-10-31',
    'NOV': '2022-11-30',
    'DEC': '2022-12-31',
    'JAN': '2023-01-31',
    'FEB': '2023-02-28',
    'MAR': '2023-03-31',
    'APR': '2023-04-30',
    'MAY': '2023-05-31',
    'JUN': '2023-06-30',
    'JUL': '2023-07-31',
    'AUG': '2023-08-31'
}