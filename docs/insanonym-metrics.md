# INSAnonym metrics

## Provided metrics

- [Date_Utility](#date_utility)
- [Hour_Utility](#hour_utility)
- [POI](#poi)
- [Distance_Utility](#distance_utility)
- [Meet_Utility](#meet_utility)
- [Tuile_Utility](#tuile_utility)

## Provided attacks

- [Naive_Attack](#naive_attack)

*Note: source code for provided metrics and attacks are available [here](https://github.com/danymat/INSAnonym-utils/tree/main/metrics)*

## Considerations

- Each metric takes 4 params:
  1. The anonymized dataframe
  2. The original dataframe
  3. Custom params
  4. the number of lines in original dataframe
 
## Date_Utility

### Summary

This metric consits in calculating the difference of days of each row between the original and anonymized dataframe.

### Scoring

- Each line takes 1 point
- 1/3 points are removed for each day difference
- The sum of the points is divided by the number of lines

## Hour_Utility

### Summary

This metric consits in calculating the difference of hours of each row between the original and anonymized dataframe.
We doesn't value the difference of days: 
- e.g an anonymized row with date=26/03/2020 11:20:21 and the original with date=20/03/2020 10:20:21 will count only 1 hour of difference (despite the fact that the days have changed).

### Score

- Each line takes 1 point
- Some fraction of a point is removed for the difference of hour (see hourdec array)
- The sum of the points is divided by the number of lines

```python
hourdec = [
  1, 0.9, 0.8, 0.6, 0.4, 0.2, 0, 0.1, 0.2, 0.3,
  0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, 0.2,
  0.4, 0.6, 0.8, 0.9
 ]
```

## POI

### Summary

A POI (Point Of Interest) corresponds to places where the user was more present:
- Home Place (22h / 6h)
- Work Place (9h / 16h) 
- Activity Place (weekend from 10h to 18h) 

We look the 3 most important POIs for each week in the dataset.

### Scoring

- A POI with 0 seconds is scored 0
- The same POI with the same time spent is scored 1
- For each POI If time in original dataframe is grater than the time in anonymized one:
  - time_POI_anonymFile / time_POI_oriFile
- Else :
  - time_POI_origFile / time_POI_anonymFile

## Distance_Utility

### Summary

This metric will compare the distance between the coordinates of the anonymized and original dataset.

### Scoring

The score for each line is created with the following function:

```python
def calcul_utility(diff):
    score = diff*(-1/dx) + 1
    if(score < 0):
        return 0
    return score
```

With `dx` being one of the following (currently at 0.1):

```
#################################
#         Global variables      #
# To know:                      #
# dx =1 means that you allow    #
# a maximum of 111.195km        #
# 0.0001 : cell at meter        #
# 0.001 : cell at street        #
# 0.01 : cell at district       #
# 0.1 : cell at city            #
# 1 : cell at region            #
# 10 : cell at country          #
#                               #
#################################
```

## Meet_Utility


## Tuile_Utility

## Naive_Attack

