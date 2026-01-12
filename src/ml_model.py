from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import json

def get_feature_importance(df):
    le = LabelEncoder()
    temp_df = df.copy()
    for col in ['Country', 'Solution', 'Action', 'Outcome']:
        temp_df[col] = le.fit_transform(df[col])

    X = temp_df[['Country', 'Solution', 'Action']]
    y = temp_df['Outcome']
    
    dt = DecisionTreeClassifier(max_depth=5, random_state=42)
    dt.fit(X, y)
    
    importance = dict(zip(['Country', 'Solution', 'Action Type'], dt.feature_importances_))
    with open('../Data/model_weights.json', 'w') as f:
        json.dump(importance, f)
    return importance