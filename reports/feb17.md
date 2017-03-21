## Accomplished in February
 
From our January work ([past report] (https://github.com/ai-se/LAS-Phishing/blob/master/reports/jan17.md)), we found out that only 9 out 30 attributes are important and we achieved the same results as with using 30 attributes ([Results] (https://github.com/ai-se/LAS-Phishing/issues/2)) on [UCI dataset] (https://archive.ics.uci.edu/ml/datasets/Phishing+Websites). The other dataset which we found is from phistank and can be seen [here] (http://www.phishtank.com/developer_info.php). Some statistics based on this dataset can be seen in below diagram.

![image](https://cloud.githubusercontent.com/assets/29195/23268398/9a9f740e-f9bb-11e6-89db-eacd39b38608.png)

![image](https://cloud.githubusercontent.com/assets/3458568/23269061/5e8027d2-f9bd-11e6-9010-631ca02b846a.png)

### Stats
- From Figure1, Url column contains the phishing website and target column represents where this website was target.
- Most of these websites are from other sources but from the 2nd diagram, it is seen that there are about 3,000 websites which have been targeted on good sources. **This is bad**.

### The 9 important attributes are:
Description of these attributes can be find out [at] (https://github.com/ai-se/LAS-Phishing/blob/master/dataset/Phishing%20Websites%20Features.docx). Code could be found [at] (https://github.com/ai-se/LAS-Phishing/blob/master/src/regex.py).

<!--| Attributes | Implementation | 
| --- | :-: |
| Prefix_Suffix | Parsed using regex |-->

- Prefix_Suffix - Parsed using regex
```
(https?://)?\w*.?\w*\-\w*.?\w*/?
```
- having_Sub\_Domain - Mix of regex and webcrawling
- SSLfinal_State - HTTP/HTTPS, Not complete as we don't have access to age of certified domains.
- Request_URL -Mix of regex and webcrawling
- URL_of\_Anchor - Mix of regex and webcrawling
- Links_in\_tags - Mix of regex and webcrawling
- SFH (server form handler) - Regex
- web_traffic - Not done as we don't have access to Alexa website database.
- Google_Index - Web crawled to find whether a url is indexed or not.
 
## Plan of work for March

Data to be extracted and then test on UCI model. Setup for LACE2.
