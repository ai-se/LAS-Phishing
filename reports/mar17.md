## Accomplished in March
 
From our Feb work ([past report](https://github.com/ai-se/LAS-Phishing/blob/master/reports/feb17.md)), we were only able to extract 7 out of 9 attributes which were important after doing feature selection during Jan work. We were not able to extract 
- SSLfinal_State - HTTP/HTTPS, Not complete as we don't have access to age of certified domains.
- web_traffic - Not done as we don't have access to Alexa website database.
[Phistank dataset](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/verified_online.csv) contains only positive examples no negative examples. Extracted data from phistank can be found [here](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/features.csv). Code could be found [here](https://github.com/ai-se/LAS-Phishing/blob/master/src/regex.py)

Now question is how much information do we lose because of those 2 features not being extracted.

### Results
- The results could be found in this [issue](https://github.com/ai-se/LAS-Phishing/issues/14). 
- We only lost about 5% and do not use NB as the classifier. We are still in the range of 90%.

### Admin Work:
- Have received access to IMPACT. Now looking at those datasets.
- Also have access to [cert dataset](http://www.cert.org/insider-threat/tools/index.cfm)

## Plan of work for April
- Remember we only extracted positive examples. In the extracted data we found about 11 target companies which have samples greater than 20. 
![file](https://github.com/ai-se/LAS-Phishing/raw/master/dataset/image.png)

- We will goto these 11 companies to randomly select our negative examples. We will try to get equal distribution of positive and negative examples.
- Once we will have created this dataset then we will setup for LACE2 experiment
