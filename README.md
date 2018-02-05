### How to run the code

Copy the ID3.py file.

From the commad promt the run the command

```
python ID3.py L K trainingSetFilePath validationSetFilePath testSetFilePath toPrint
```

The arguments represent the following

L, K 					- The parameters for the post pruning algorithm
trainingSetFilePath 	- The path to the csv file containing training data
validationSetFilePath 	- The path to the csv file containing the validation set
testSetFilePath 		- The path to the csv file containing the test set
toPrint					- Whether to print the decision tree or not

### The accuracy on the data sets provided  
#### On Data Set 1  
##### Using Information Gain Heuristic  
Accuracy on the test set = 75.85  
##### Using Variance Impurity Heuristic  
Accuracy on the test set = 75.35  
#### On Data Set 2  
##### Using Information Gain Heuristic  
Accuracy on the test set = 72.33333333333333  
##### Using Variance Impurity Heuristic  
Accuracy on the test set = 72.5  

#### After post pruning
| DataSet | L | K | Heuristic | Accuracy |  
| ------- | --- | --- | -------- | ------- |  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
|1|10|10|"Information Gain"|73.16|  
|1|10|10|"Variance Impurity"|73.16|  
