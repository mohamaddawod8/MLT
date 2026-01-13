import pandas as pd

def run_cleaning(file_name='data_all.xltx'):
    df = pd.read_excel(file_name)
    mapping = {
        'account_id': 'Account_ID', 'activity_date': 'Date',
        'solution': 'Solution', 'types': 'Action',
        'opportunity_stage': 'Outcome', 'Country': 'Country'
    }
    df = df.rename(columns=mapping)
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date']).sort_values(by=['Account_ID', 'Date'])
    
    for col in ['Country', 'Solution', 'Action']:
        df[col] = df[col].fillna('Unknown').astype(str).str.strip()
    
    def simplify_outcome(stage):
        stage = str(stage).lower()
        if 'won' in stage or 'closed won' in stage: return 'Win'
        elif 'lost' in stage or 'disqualified' in stage or 'closed lost' in stage: return 'Loss'
        return 'In Progress'

    df['Outcome'] = df['Outcome'].apply(simplify_outcome)
    df.to_csv('../Data/cleaned_data.csv', index=False, encoding='utf-8-sig')

    return df
