#see README.md

import sys
import requests
import json
import csv
import bz2


def read_iso_countries_list():

    url="https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv"
    r=requests.get(url)
    print("Download regions code list from :\n" + url)
    cr = csv.reader(r.content.decode("utf-8").split("\n") )
    countryCode_info=dict()
    for row in cr:
        if len(row)>2:
            countryCode_info[row[1]]=row
    return countryCode_info



def read_ripe_probe_list(date):

    url="https://ftp.ripe.net/ripe/atlas/probes/archive"
    year=date[0:4]
    month=date[4:6]
    day=date[6:8]
    url=url+"/"+year+"/"+month+"/" + date+".json.bz2"
    print("Downloading ripe database from " +url)
    r = requests.get(url)
    decompressed= bz2.decompress(r.content)

    decompressed=decompressed.decode("utf-8")

    j= json.loads(decompressed)
    outz=open(outfile,'w')

    tempList=j['objects']
    newDict=j
    #reset objects
    newDict['objects'] =[]
    newList=[]
    for item in tempList:


        tempCC=item['country_code']
        #print(tempCC)

        #some handling of valid fieldds
        if type(tempCC) is not None and tempCC!=""  and str(tempCC)!="None":
            #print(tempCC)
            tempStr=geo_data[tempCC]

            continent=tempStr[5]
            sub_region=tempStr[6]
            intermediate_region=tempStr[7]

            item['continent']=continent
            item['sub_region']=sub_region
            item['intermediate_region']=intermediate_region

            #update json

            newList.append(item)
        #update item
    newDict['objects']=newList

    json.dump(newDict,outz)

    outz.close()

    print("see if we can read the file")



#start

print("Starting run")


if len(sys.argv)!=3:
    print("Wrong number of parameters\n")
    print(str(len(sys.argv)))
    print("Usage:  python run.py $DATE(YYYYMMDD) $OUTFILE")
else:

    print("reading country code info")
    geo_data=read_iso_countries_list()
    d=sys.argv[1]
    outfile=sys.argv[2]

    print("reading ripe atlas json")
    ripe_data=read_ripe_probe_list(d)


