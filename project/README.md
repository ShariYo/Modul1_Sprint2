
# Top 50 Spotify Tracks of 2020

This project for analyzing top 50 spotify tracks of 2020. Mainly it is just about exploratory analsysis. Project consists of one main table which is downloaded, observed, cleaned and used for exploratory analysis. By analyzing given table, the answers will be submitted of the questions, asked on the project's requirements.


## Data source

Given data source can be found at Kaggle with the link provided below:

```bash
  https://www.kaggle.com/datasets/atillacolak/top-50-spotify-tracks-2020
```
    
## Main functions/libraries used for data analysis:
- pandas(pd) - library for pandas functions;
- numpy(np) - library for numpy functions;
- pre-installed python functions;
- pd.read_csv() - to read a given data source;
- .duplicated().any() - check if there are any duplicates;
- .isna().any() - check if there are any NaN values;
- .describe() - to get brief information about dataframe values (mean, count, std., min, max, etc.);
- .unique() - get all unique values;
- np.argmax(), np.argmin() - return indices of the max/min values along axis;
- .groupby() - group data by a given column name;
- .corr() - get correlation of a given data. 
