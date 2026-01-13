from src.data_cleaning import run_cleaning
from src.ml_model import get_feature_importance
from src.recommender import get_recommendations

def main():
    
    print("\n Cleaning and Ordering Excel Data...")
    df = run_cleaning('Data/data_all.xltx')
    print("Done")

    print("\nTraining Decision Tree Model...")
    weights = get_feature_importance(df)
    print(f"Done")
    
    country_in = 'US'
    solution_in = 'MRS'
    current_path = [] 
    
    print(f"\n  Generating Initial Recommendations for {country_in}...")
    c, s, cs, dynamic = get_recommendations(df, weights, country_in, solution_in, current_path)
    
    print(f"1. Top 4 actions by Country: {c}")
    print(f"2. Top 4 actions by Solution: {s}")
    print(f"3. Top 4 actions by Country & Solution: {cs}")
    print(f"4. Next Best Actions (Initial Touch): {dynamic}")
        
    print("\n User adds an action: 'Email'...")
    current_path.append('Email')
    print(" Recalculating weights using Last Touch adjustment...")
    _, _, _, dynamic_updated_1 = get_recommendations(df, weights, country_in, solution_in, current_path)
    print(f" Updated Next Best Actions after 'Email': {dynamic_updated_1}")
    
    print("\n User adds another action: 'Call'...")
    current_path.append('Call')
    print(" Re-adjusting weights for the entire sequence...")
    _, _, _, dynamic_updated_2 = get_recommendations(df, weights, country_in, solution_in, current_path)
    print(f" Updated Next Best Actions after sequence {current_path}: {dynamic_updated_2}")

    print("System Execution Completed Successfully ")

if __name__ == "__main__":
    main()