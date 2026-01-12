import pandas as pd

def get_recommendations(df, weights, country, solution, current_path_list):
    t_country = df[df['Country'] == country]['Action'].value_counts().head(4).index.tolist()
    t_solution = df[df['Solution'] == solution]['Action'].value_counts().head(4).index.tolist()
    t_both = df[(df['Country'] == country) & (df['Solution'] == solution)]['Action'].value_counts().head(4).index.tolist()
    
    actions_list = df['Action'].unique().tolist()
    scores = {}
    is_first_touch = len(current_path_list) == 0

    for action in actions_list:
        action_frequency = df[(df['Country'] == country) & (df['Solution'] == solution) & (df['Action'] == action)].shape[0]
        base_weight = (weights.get('Action Type', 0) * action_frequency) + \
                      (weights.get('Country', 0) * 1) + \
                      (weights.get('Solution', 0) * 1)

        if is_first_touch:
            scores[action] = base_weight 
        else:
            last_touch = current_path_list[-1]
            if str(action).lower() == str(last_touch).lower():
                scores[action] = base_weight * 0.1
            else:
                scores[action] = base_weight

    dynamic_top = [a[0] for a in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:4]]
    return t_country, t_solution, t_both, dynamic_top