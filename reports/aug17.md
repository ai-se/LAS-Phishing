## Accomplished in August
 
### LACE2 Experiments and Results
From our May work ([past report](https://github.com/ai-se/LAS-Phishing/blob/master/reports/may17.md)), we performed LACE2 with training done using [UCI Training set](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/uci_training.csv) and tested on 7 Targetted companies ([here](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/testing)).

We saw from the [results](https://github.com/ai-se/LAS-Phishing/issues/18), transfer learning could be done.

### Current Experiments:
- The last results didn't show us big performance improvement for many learners for multiple evaluation criteria.
- One way to solve, is to tune the parameters of LACE2 algorithm which is Cliff percentage and Morph parameters.
- We wrote the algorithm to tune these parameters of LACE2 with a search based optimizer called Differential Evolution (DE).

## Plan of work for September:
- We will be testing the above algorithm on our datasets and will report the performance score it achieved due to tuning. We will also provide how much computationally costly it will be, and whether it makes sense to have a good tade off between the performance and the runtime cost.
