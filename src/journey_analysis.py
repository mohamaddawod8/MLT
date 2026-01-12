import pandas as pd

def run_analysis(df):
    print("--- Step 2: Building Chronological Journeys ---")
    def build_path(group):
        return " -> ".join(group['Action'].astype(str))

    journeys = df.groupby(['Account_ID', 'Country', 'Solution', 'Outcome']).apply(
        build_path, include_groups=False
    ).reset_index()
    journeys.columns = ['Account_ID', 'Country', 'Solution', 'Outcome', 'Full_Path']
    
    top_5 = journeys.groupby(['Country', 'Solution'])['Full_Path'].value_counts().groupby(level=[0,1]).head(5)
    top_5.to_csv('../Data/top_5_chronological_paths.csv')
    return journeys