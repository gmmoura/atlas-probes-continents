# atlas-probes-continents


   * [Ripe Atlas](https://atlas.ripe.net) are very often used in measurements studies and by operators
   * There are more than 12k active probes at the  moment, and RIPE makes the list of probes available [at this link](https://ftp.ripe.net/ripe/atlas/probes/archive/).
   * Each probe has a contry code, however, there is no current info about which *continents* or *region* the probe is located
   * This piece of software does just that: add this extra info to the Ripe list
   * It gets this info from [another Github Repository](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes)
   
   
 ## Usage
 
 ```bash 
 $ python run.py $DATE(YYYYMMDD) $OUTFILE
```

## DNS CHAOS Ripe Atlas Measuremnet parser


   * this code is located under dns-chaos-parser
   
