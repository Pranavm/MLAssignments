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
|1|10|10|"Information Gain"|76.35|  
|1|10|10|"Variance Impurity"|76.95|  
|1|10|20|"Information Gain"|76.6|  
|1|10|20|"Variance Impurity"|75.6|  
|1|20|10|"Information Gain"|76.6|  
|1|20|10|"Variance Impurity"|75.95|  
|1|30|30|"Information Gain"|75.2|  
|1|30|30|"Variance Impurity"|75.35|  
|1|50|25|"Information Gain"|76.85|  
|1|50|25|"Variance Impurity"|77.0|  
|1|60|40|"Information Gain"|76.05|  
|1|60|40|"Variance Impurity"|76.65|  
|1|60|70|"Information Gain"|76.85|  
|1|60|70|"Variance Impurity"|76.35|  
|1|75|75|"Information Gain"|77.0|  
|1|75|75|"Variance Impurity"|75.3|  
|1|80|80|"Information Gain"|75.2|  
|1|80|80|"Variance Impurity"|76.35|  
|1|100|100|"Information Gain"|77.35|  
|1|100|100|"Variance Impurity"|77.25|  
|2|10|10|"Information Gain"|73.17|  
|2|10|10|"Variance Impurity"|72.67|
|2|10|20|"Information Gain"|72.33|  
|2|10|20|"Variance Impurity"|74.17|  
|2|20|10|"Information Gain"|74.0|  
|2|20|10|"Variance Impurity"|73.0|  
|2|30|30|"Information Gain"|74.0|  
|2|30|30|"Variance Impurity"|72.5|  
|2|50|25|"Information Gain"|72.5|  
|2|50|25|"Variance Impurity"|73.33|  
|2|60|40|"Information Gain"|74.33|  
|2|60|40|"Variance Impurity"|74.5|  
|2|60|70|"Information Gain"|71.67|  
|2|60|70|"Variance Impurity"|71.5|  
|2|75|75|"Information Gain"|71.5|  
|2|75|75|"Variance Impurity"|73.67|  
|2|80|80|"Information Gain"|71.5|  
|2|80|80|"Variance Impurity"|73.17|  
|2|100|100|"Information Gain"|72.67|  
|2|100|100|"Variance Impurity"|73.83|  
