#this file reads a csv of results from the parser  and allows to specify matching columns to do the calculations
import sys
import numpy as np


print("Starting ")


if len(sys.argv)!=6:
    print("Wrong number of parameters\n")
    print(str(len(sys.argv)))
    print("Usage:  python stats-agg.py $infile $rtt-column $RCODE $matching-column $matching-value")
else:

    values=[]

    infile=sys.argv[1]
    rtt_column=sys.argv[2]
    rcode=sys.argv[3]
    matching_column=sys.argv[4]
    matching_value=sys.argv[5]

    with open(infile , 'r') as f:
        lines=f.readlines()

        for l in lines:

            sp=l.split(",")
            #if matches rcode and if the column value matches
            if sp[7].strip()==rcode and sp[int(matching_column)].strip()==matching_value.strip():
                values.append(float(rtt_column.strip()))


    print("#n_measurements,avg_rtt,median_rtt,fistquartile,3rdquartile,90percentile")

    print(str(len(values)) +","+
          str(np.mean(values)) +","+
          str(np.percentile(values,50))  +","+
          str(np.percentile(values,75))  +","+
          str(np.percentile(values,90))
          )

    print("DONE")

