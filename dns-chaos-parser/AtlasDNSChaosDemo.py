#this code parse and outputs some features from ripe into csv, enriched with the regions and continents and subregions


import json
from  f4570above import f4570above
import sys
import requests
import gzip


def json_parser(f):
    answers = []

    try:
        measurements = json.loads(f)

        for m in measurements:

            try:
                fw = m["fw"]

                typeMeasurement = m["type"]

                if (int(str(fw)) >= 4570 and str(typeMeasurement == "dns")):
                    x = f4570above(m)

                    temp = x.answers

                    # print(len(temp))
                    targetServer = ""
                    for k in temp:
                        targetServer = k.RDATA

                    answers.append(
                        str(x.From) + "," + str(x.dst_addr) + "," + str(x.proto) + "," + str(targetServer) + "," + str(
                            x.rt) + "," + str(x.prb_id) + "," + str(x.timestamp) + "," + str(x.rcode))


            except:
                print("ERROR: EMPTY measurement")
                answers=[]
                answers.append("ERROR: EMPTY measurement")
                #return answers
        #if everything goes well
       # return answers
    except:
        print("ERROR parsing json")
        print("Unexpected error:", sys.exc_info())
        answers=[]
        answers.append("ERROR parsing json")


    return answers



def read_probe_data(f):
    f = gzip.open(f, 'rb')
    metadata = f.read()
    metadata=metadata.decode("utf-8")
    f.close()

    appendDict=dict()

    items=json.loads(metadata)

    for k in items['objects']:
        prid=k['id']
        trailler=k['country_code']+","+k['continent']+","+k['sub_region']
        appendDict[str(prid)]=trailler

    return appendDict





if len(sys.argv)!=4:
    print("Wrong number of parameters\n")
    print(str(len(sys.argv)))
    print("Usage:  python AtlasDNSChaosDemo.py $AtlasMeasurement $probesMetadata.gz $output.csv ")
else:

    url=sys.argv[1]
    probeFile=sys.argv[2]
    output=sys.argv[3]

    outz=open(output, 'w')


    print("Downloading ripe database from " +url)
    r = requests.get(url)

    measurements=json_parser(r.content.decode("utf-8"))

    print("readin probe metadata")
    probeDict=read_probe_data(probeFile)

    #now, with all the data in hands, we gotta for each measurmenet to add the trailler

    for k in measurements:
        #print("w")
        probeID=k.split(",")[5]
        trailler="NA"
        try:
            trailler=probeDict[probeID.strip()]
        except:
            print("Probe not found: " + str(probeID))
        outz.write(k+","+trailler+"\n")

    outz.close()

    print('END')



