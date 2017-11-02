## Accomplished in October
 
### Previous Work:
From our September work ([past report](https://github.com/ai-se/LAS-Phishing/blob/master/reports/sep17.md)), we fixed the issues in LACE2.

### Current Experiments:
- We didn't get much improvement when we tuned the LACE2. We did not observe big changes even after fixing the LACE2 implementation. This may be due to nature of data and its attributes.
- But when performed mutaion to keep the regions of each feature uniform. We performed mutation from 0 to 0.5 when we find a feature of 0, but we mutated between 0.5 to 1, when feature is found to be 1.
- Surprisingly, we observed that this morphed data performs better than the baseline when considered SVM classifier with RBF kernel.
- Results can be seen [here](https://github.com/ai-se/LAS-Phishing/issues/23).

## Plan of work for November:
- Preparing the poster for the presentation at LAS symposium.
- Delievering a final report, code, and readme on how to run the code.
