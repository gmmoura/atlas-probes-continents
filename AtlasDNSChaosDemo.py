#this code parse and outputs some features from ripe into csv, enriched with the regions and continents and subregions

import sys
import json


from ripe.atlas.sagan import DnsResult
import json
from  f4570above import f4570above
import sys


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

                    answers.append(str(x.prb_id)+","+
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







if len(sys.argv)!=4:
    print("Wrong number of parameters\n")
    print(str(len(sys.argv)))
    print("Usage:  python AtlasDNSChaosDemo.py $AtlasJSONFILE $probesMetadata $output.csv ")
else:

    measurements=sys.argv[0]
    probesMetadata=sys.argv[1]
    output=sys.argv[2]

    listtoPrint=json_parser(measurements)
    print('wait here')



