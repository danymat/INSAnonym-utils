# User guide

## Introduction

INSAnonym is a competition platform for anonymization.
This competition aims to test the participants in the process of anonymization and re-dentification.
In this document, we will try to guide the user between the different competition stages, and to explain the rules.

## Stages

1. Dataset Download 
2. Anonymization
3. Reidentification


# Dataset Download

The file downloaded is a zip file (127Mo).
When unzipping, you'll have a csv file (1.7Go), containing 4 columns.
This is a sample from the file:

```csv
1	2015-03-04 00:35:54	0.6862299652880149	0.5607438893732356
1	2015-03-04 00:35:55	0.17177522268016	0.19712564088036866
1	2015-03-04 00:35:56	0.5727169413410496	0.6295753633636196
1	2015-03-04 00:35:58	0.8924030365448349	0.29995126223315627
1	2015-03-04 00:35:59	0.8801684311745377	0.3656178115984039
1	2015-03-04 00:36:01	0.712761220611243	0.3604362165391204
```

The columns are:

```python
[ 'id', 'date', 'latitude', 'longitude' ]
```

## Anonymization

In this stage, the teams will try to anonymize the dataset.

### Rules 

The process must follow some rules:

- We work by user id and week. 
A week conforms to the the week number in the calendar year.
The id must be changed in such a way that, for a id in a week, the user does not change.

For example, for a user, this is a correspondance table :

```csv
id  0   1   2   ... 10  11  12
32  7   12  1   ... DEL DEL AAAC2
```

- It is forbidden top change the number of lines and columns. Your submission is automatically randomized in the server.

- With the previous point in mind, in order to delete lines, you can replace the id with `DEL` in the line.

- The date can be modified but:
    - The modified date has to be in the same week.
    - The format must be the same. Generally, the format must be the same for all columns.

- GPS coordinates can be modified at wish
- The file uploaded must be a zip file.

### Considerations

- Each team can only process at most 1 file at the time. If your file is still being processed, you have to wait the process from finishing, in order to upload a second file.
- Each team can publish at most 3 files

When a file is being processed, various alculus are being done. With that in mind, when a process is taken from the processing queue, you can expect it to finish in 5 minutes.

A submission made easy to re-identify will give more points to the opponents. We then created a "naive attack" to help you realize quickly if your submission is easy to guess.

The documentations for the attack file and all metrics can be found [here](https://github.com/danymat/INSAnonym-utils/blob/main/docs/insanonym-metrics.md).

If you are pleased with the scores from your submission, you can then publish it.


## Reidentification

In this stage, the teams will try to reidentify opponent's submissions.

An attack file must be a binding between the id, and for each week, a guess of one or more identifiers.

- The file must be a `json` file.
- You can submit at most 10 attack files per submission.
- If you think an id has been deleted for the week, you can specify `"DEL"` in one of your guesses.
- If a user is not present in the given week in original file (e.g the id 7 is not present at week 12), the server will automatically skip this week for the id (No score will be given for this user at the given week.)

Below is an example of an attack file.

```json
{
   "17850":{
          "2015-0":[
             "AAAAA1",
             "AAAAA2",
             "AAAAA3"
          ],
          "2015-1":[
             "AAAAA1"
          ],
          "2015-2":[
             "AAAAA1"
          ],
          "2015-3":[
             "AAAAA2"
          ]
   },
   "12583":{
          "2015-1":[
             "CCCCCC1"
          ],
          "2015-2": [],
          "2015-3":[
             "CCCCCC2"
          ],
          "2015-4":[
             "CCCCCC3"
          ]
   }
}
```

### Scoring

Each team can propose multiple guesses in each week for an identifier, but if doing so, if there's a correct guess, it'll be divided by the number of guesses.

The score is created from the following rules:

- A correct guess counts to `1/N` points, `N` being the number of guesses
- A wrong guess counts to `0` points
- The final score is equal to your points divided by all possible points

## Ranking

Each team will have a General score, a Defense score and an Attack score.

### Specification for scoring

With `S` being the uploads the team did publish.
Each team can submit multiple attacks for each `S` submissions.

The score for each submission `S` is made with the following:
 
 ```
 ScoreD(S) = Utility * (1-MAXgrp(attack score))
 ```

- `Utility` the score created with from the server's utility scores.
- `MAXgrp(attack score)` the maximum attack score over S from all other teams

The defense score for a group is the best score from its submission `S` as the following:

```
ScoreG = MAXS(ScoreD(S))
```

The final attack score of a team is the sum of their worst attack in each opponent team. 

The score is then a number in `[0:N-1]` with `N` the number of teams in the competition.
