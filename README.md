# K-means clustering

## Data
There are two classes of wife and husband salaries data.

### data size: 
1. Not stressed wife and husband salaries: 2x199
2. Stressed wife and husband salaries: 2x200

## Method
example: one dimension dataset [0,2,10,12]  <br>
if k=2
### 1. Randomly pick k numbers of data in the dataset
center_point_1 = 0  <br>
center_point_2 = 2

### 2. Classify all the data with the center points
class_1: 0  <br>
class_2: 2, 10, 12

### 3. Find the mean values of each class
mean_1: 0   <br>
mean_2: 8

### 4. Set the mean value to new center points
center_point_1 = 0  <br>
center_point_2 = 8

### 5. Redo 2~3 till the mean values are as same as the previous center points
class_1: 0, 2   <br>
class_2: 10, 12

mean_1: 1   <br>
mean_2: 11