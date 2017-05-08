## Accomplished in April
 
### Datasets preprocessing and collection
From our March/April work ([past report](https://github.com/ai-se/LAS-Phishing/blob/master/reports/ap17.md)), we already extracted positive features.

Negative samples were extracted from 7 targetted websites such as **'AOL', 'Facebook', 'PayPal', 'Google', 'Apple' and 'Yahoo'** picked at random. The final [positive](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/phistank+features.csv) and [negative](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/phistank-features.csv) samples dataset is found [here](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/phistank.csv)

### Lace2 Experiments:
- Source - [UCI Training set](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/uci_training.csv) - 30% training data selected at random.
- 7 target companies in which small subset of UCI data is changed and shared. Final testing datasets based on these targets are [here](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/testing).
- According to LACE2, cliff algorithm selects the best rows to forward and morph parameters select how features are modified keeping its importance intact. The original LACE2 is written for continuous features. Those features are normalised first since phishing features are already between -1 to 1, we didn't need to normalise. So, the algorithm is modified and can be found [at](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/src/lace/runlace.py).
- For baseline we selected 30% from uci and tested on those 7 companies without modifying the uci features. Lets call it Baseline results.
- Now Lace2 selects cliff percentage 30, and morph parameters of 0.2 to 0.5 to modify. This modified dataset is [here](https://github.com/ai-se/LAS-Phishing/blob/master/dataset/training). And tested on those 7 companies. Lets call it Lace results.

### Results

- We report performance delta of Lace results over baseline results. 
- Positive the better for all measures except false alarm in which case negative the better.
- The results could be found in this [issue](https://github.com/ai-se/LAS-Phishing/issues/18). 
- Conclusion: Transfer learning could be done.

### Admin Work:

- Impact and cert dataset are not properly preprocessed and formatted. It will take longer time to make it in format of Lace2 format. And it also can not be divided as different targets.