## Accomplished in September
 
### LACE2 Tuning Experiments
From our August work ([past report](https://github.com/ai-se/LAS-Phishing/blob/master/reports/aug17.md)), we tried tuning the LACE2 and were waiting on the results. While getting the results, we found problem with our LACE2 implementation.

### Current Experiments:
- The problem with LACE2 implementation was that the original Paper ( [Fayola](http://menzies.us/pdf/15lace2.pdf) ) assumed the feature variables to be continuous in nature. But our data contains binary feature set, just 0s and 1s.
- The above problem was solved by morphing and mutating the feature set in a random manner, but keeping the regions same. So, if a feature is 0, then it is randomly morphed between 0 to 0.5. And if the feature is 1, it is randomly morphed from 0.5 to 1.
- Similarly there are couple of more changes from the original paper. We tried fixing them up

## Plan of work for October:
- We are testing the above modified implementation on the original baseline results as well as on the tuned experiments. We will also provide how much computationally costly it will be, and whether it makes sense to have a good tade off between the performance and the runtime cost.
