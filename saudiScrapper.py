import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import urllib.request
except:
    install('urllib')
    import urllib.request


'''
import requests

r = requests.get(myurl)

test = [
  r,
  r.status_code,
  r.headers['content-type'],
  r.encoding
  # r.text
]

for i in test : print(i)
'''


# myUrlList = [
#     'ftp://ftp.ncdc.noaa.gov/pub/data/wwr/WWR_v01_global_array_1961-1970.txt',
#     'ftp://ftp.ncdc.noaa.gov/pub/data/wwr/WWR_v01_global_array_1971-1980.txt',
#     'ftp://ftp.ncdc.noaa.gov/pub/data/wwr/WWR_v01_global_array_1981-1990.txt',
#     'https://www1.ncdc.noaa.gov/pub/data/wwr/documents/Asia/WWR_1991-2000.txt'
# ]


myUrlList = [
    "file:///C:/Users/A/Desktop/Hosam/Data/WWR_v01_global_array_1961-1970.txt",
    "file:///C:/Users/A/Desktop/Hosam/Data/WWR_v01_global_array_1971-1980.txt",
    "file:///C:/Users/A/Desktop/Hosam/Data/WWR_v01_global_array_1981-1990.txt",
    "file:///C:/Users/A/Desktop/Hosam/Data/WWR_1991-2000.txt"
]

sData = []

for i in myUrlList:
    with urllib.request.urlopen(i) as req:
        # fullfile = req.read().decode(req.info().get_content_charset(), 'ignore')
        fullfile = req.read().decode('utf8', 'ignore')

    fulllist = fullfile.splitlines()

    for index, line in enumerate(fulllist):
        if 'SAUDI' in line:
            extracted = fulllist[index:index+72]
            sData.append(extracted)
            # print(fulllist[index:index+72])


# assert len(sData) == 44

print(len(sData))
# should be 44

# for x in sData:
#     print(x[0])

#  Now we have a list of lists, each inner list has a single station '72 Lines', first line includes country and station code

fData = []

for station in sData:
    st = []
    st.append(station[0])

    for ln in station[1:]:
        if ln[7] == '5' and ln[12] != '1' and ln[12] != '2':
            st.append(ln[:73])

    fData.append(st)

print(len(fData))
# should be 44


fData.sort(key=lambda item: item[0][43:55])


# make a backup:
with open('backup1.txt', 'w') as out1:
    out1.write(repr(fData))


# # Cleaning:
# for fStation in fData:

#     sttt = []
#     sttt.append(fStation[0])

#     for fLine in fStation[1:] :


# for onest in fData:
#     for vv in onest[1:]:
#         print(vv[73:])
