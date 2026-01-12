from data_cleaning import run_cleaning
from ml_model import get_feature_importance
from recommender import get_recommendations

def main():
    print(">>> System Execution Started <<<")
    
    print("\n[Step 1/4] Processing: Cleaning and Ordering Excel Data...")
    df = run_cleaning('../Data/data_all.xltx')
    print("Done: Data is cleaned and chronologically sorted.")

    print("\n[Step 2/4] Processing: Training Decision Tree Model...")
    weights = get_feature_importance(df)
    print(f"Done: Smart weights extracted from model: {weights}")
    
    country_in = 'US'
    solution_in = 'MRS'
    current_path = [] 
    
    print(f"\n[Step 3/4] Processing: Generating Initial Recommendations for {country_in}...")
    c, s, cs, dynamic = get_recommendations(df, weights, country_in, solution_in, current_path)
    
    print("\n" + "="*50)
    print(f"FINAL FOR: {country_in} | {solution_in}")
    print(f"1. Top 4 actions by Country: {c}")
    print(f"2. Top 4 actions by Solution: {s}")
    print(f"3. Top 4 actions by Country & Solution: {cs}")
    print(f"4. Next Best Actions (Initial Touch): {dynamic}")
    print("="*50)
    
    print("\n[Step 4/4] Simulating User Interaction...")
    
    print("\n User adds an action: 'Email'...")
    current_path.append('Email')
    print("Processing: Recalculating weights using Last Touch adjustment...")
    _, _, _, dynamic_updated_1 = get_recommendations(df, weights, country_in, solution_in, current_path)
    print(f"--> Updated Next Best Actions after 'Email': {dynamic_updated_1}")
    
    print("\n User adds another action: 'Call'...")
    current_path.append('Call')
    print("Processing: Re-adjusting weights for the entire sequence...")
    _, _, _, dynamic_updated_2 = get_recommendations(df, weights, country_in, solution_in, current_path)
    print(f"--> Updated Next Best Actions after sequence {current_path}: {dynamic_updated_2}")

    print("\n" + "="*50)
    print("System Execution Completed Successfully ")
    print("="*50)

if __name__ == "__main__":
    main()