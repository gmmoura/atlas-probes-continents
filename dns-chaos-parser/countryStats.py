#this file reads a csv of results from the parser  and allows to specify matching columns to do the calculations
import sys
import numpy as np


print("Starting ")


if len(sys.argv)!=4:
    print("Wrong number of parameters\n")
    print(str(len(sys.argv)))
    print("Usage:  python countryStats $infile $rtt-column $RCODE ")
else:

    values=[]

    infile=sys.argv[1]
    rtt_column=sys.argv[2]
    rcode=sys.argv[3]

    ccDict=dict()

    with open(infile , 'r') as f:
        lines=f.readlines()

        for l in lines:

            sp=l.split(",")
            #if matches rcode and if the column value matches
            if len(sp)==11:
                if sp[7].strip()==rcode:
                    tempCountry=sp[8].strip()
                    tempRTT=float(sp[4].strip())

                    if tempCountry not in ccDict:
                        tempArray=[]
                        tempArray.append(tempRTT)
                        ccDict[tempCountry]=tempArray
                    else:
                        tempArray=ccDict[tempCountry]
                        tempArray.append(tempRTT)
                        ccDict[tempCountry]=tempArray


    print("#country, nMesurements,25p,50p,75p,max,90p")
    for k,values in ccDict.items():
        country=k
        print(
             country
              +","+
              str(np.mean(values))
              + "," + str(np.percentile(values, 25))
              + "," + str(np.percentile(values, 50))
              + "," + str(np.percentile(values, 75))
              + "," + str(np.max(values))
              + "," + str(np.percentile(values, 90))
              )
              #   +","+  str(np.max(values)) + "," + str(np.percentile(values,90)) )



