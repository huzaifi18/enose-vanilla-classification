def normalize_data_with_Baseline(dataframe, atribute_names): # koreksi baseline, filename: '_A_*.csv'
    """correcting the baseline

    Args:
        dataframe (DataFrame): a single dataframe
        atribute_names (list): list of attribute names

    Returns:
        DataFrame: dataframe with corrected baseline
    """
    baseline = []
    baseline_df = dataframe[(dataframe['time(s)'] < 10)]
    for cols in atribute_names:
        baseline.append(baseline_df[cols].mean())
    
    for cols_df, cols_baseline, in zip(atribute_names, baseline):
        dataframe[cols_df] = dataframe[cols_df] - cols_baseline
    return dataframe

def extract_FeaturesCubic(CSV_files, label, return_dataset=False):
    """extract max, mean, median, and gradients from given CSV files

    Args:
        CSV_files (list): csv files
        label (str): label
        return_dataset (bool, optional): wheter get formated dataset. Defaults to False.

    Returns:
        DataFrame: if return_dataset is True
        array: if return_dataset is False
    """
    maxi = np.empty((0, 10))
    mean = np.empty((0, 10))
    median = np.empty((0, 10))
    grad = np.empty((0, 10))
    for csv_file in CSV_files:
        df = pd.read_csv(csv_file)
        df.drop(columns=["time(s)","Temp","Humid"], inplace=True)
        _max_list = []
        _mean_list = []
        _median_list = []
        _grad_list = []
        for cols, _ in df.iteritems():        
            _max_list.append(df[cols].max())
            _mean_list.append(df[cols].mean())
            _median_list.append(df[cols].median())
            _grad_list.append(get_MaxGradient(df, cols))
        maxi = np.vstack((maxi, np.array(_max_list).T))
        mean = np.vstack((mean, np.array(_mean_list).T))
        median = np.vstack((median, np.array(_median_list).T))
        grad = np.vstack((grad, np.array(_grad_list).T))
    
    if return_dataset:
        mean_df = pd.DataFrame(mean, columns=["mu1", "mu2", "mu3", "mu4", "mu5", "mu6", "mu7", "mu8", "mu9", "mu10"])
        max_df = pd.DataFrame(maxi, columns=["max1", "max2", "max3", "max4", "max5", "max6", "mu7", "max8", "max9", "max10"])
        median_df = pd.DataFrame(median, columns=["med1", "med2", "med3", "med4", "med5", "med6", "med7", "med8", "med9", "med10"])
        grad_df = pd.DataFrame(grad, columns=["grad1", "grad2", "grad3", "grad4", "grad5", "grad6", "grad7", "grad8", "grad9", "grad10"])
        dataset = pd.concat([mean_df, max_df, median_df, grad_df], axis=1)
        dataset["label"] = label
        return dataset
        
    else:        
        all_arrays = [maxi, mean, median, grad]
        all_arrays = np.transpose(all_arrays, (1, 2, 0))
        return all_arrays