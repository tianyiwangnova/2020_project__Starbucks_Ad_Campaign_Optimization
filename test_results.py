import pandas as pd
import numpy as np

def score(df, promo_pred_col = 'Promotion'):
    n_treat       = df.loc[df[promo_pred_col] == 'Yes',:].shape[0]
    n_control     = df.loc[df[promo_pred_col] == 'No',:].shape[0]
    n_treat_purch = df.loc[df[promo_pred_col] == 'Yes', 'purchase'].sum()
    n_ctrl_purch  = df.loc[df[promo_pred_col] == 'No', 'purchase'].sum()
    irr = n_treat_purch / n_treat - n_ctrl_purch / n_control
    nir = 10 * n_treat_purch - 0.15 * n_treat - 10 * n_ctrl_purch
    return (irr, nir)
    

def test_results(promotion_strategy):
    test_data = pd.read_csv('Test.csv')
    df = test_data[['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']]
    promos = promotion_strategy(df)
    score_df = test_data.iloc[np.where(promos == 'Yes')]    
    irr, nir = score(score_df)
    print("Nice job!  See how well your strategy worked on our test data below!")
    print()
    print('Your irr with this strategy is {:0.4f}.'.format(irr))
    print()
    print('Your nir with this strategy is {:0.2f}.'.format(nir))
    
    print("We came up with a model with an irr of {} and an nir of {} on the test set.\n\n How did you do?".format(0.0188, 189.45))
    return irr, nir

def test_results_distributions(promotion_strategy, numbers_run=10):
    print("Run the model for {} times".format(numbers_run))
    test_data = pd.read_csv('Test.csv')
    df = test_data[['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']]
    irrs = []
    nirs = []
    for i in range(numbers_run):
        promos = promotion_strategy(df)
        score_df = test_data.iloc[np.where(promos == 'Yes')]    
        irr, nir = score(score_df)
        irrs.append(irr)
        nirs.append(nir)
    print("Distributions of irr and nir:")
    plt.figure(figsize=(12,5))
    plt.subplot(1, 2, 1)
    plt.hist(irrs)
    a1=plt.title('irr')
    plt.subplot(1, 2, 2)
    plt.hist(nirs)
    a1=plt.title('nir')






