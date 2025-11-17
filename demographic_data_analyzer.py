import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    def safe_str(col):
        return df[col].astype(str).str.strip()

    df['sex_clean'] = safe_str('sex')
    df['education_clean'] = safe_str('education').str.upper()
    df['country_clean'] = safe_str('native-country')
    df['occupation_clean'] = safe_str('occupation')

    df['rich'] = df['salary'].astype(str).str.strip().str.contains(r'>\s*50', case=False, regex=True, na=False)

    race_count = df['race'].value_counts()

    # EXACT MATCH "Male" (not contains)
    men_mask = df['sex_clean'] == 'Male'
    average_age_men = round(df.loc[men_mask, 'age'].mean(), 1)

    percentage_bachelors = round((df['education_clean'] == 'BACHELORS').mean() * 100, 1)

    higher_eds = {'BACHELORS', 'MASTERS', 'DOCTORATE'}
    higher_mask = df['education_clean'].isin(higher_eds)

    higher_education_rich = round(df.loc[higher_mask, 'rich'].mean() * 100, 1)
    lower_education_rich = round(df.loc[~higher_mask, 'rich'].mean() * 100, 1)

    min_work_hours = int(df['hours-per-week'].min())
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(min_workers['rich'].mean() * 100, 1)

    country_rich_pct = df.groupby('native-country')['rich'].mean() * 100
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    india_rich = df[(df['native-country'].astype(str).str.strip() == 'India') & (df['rich'])]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax() if len(india_rich) > 0 else None

    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return result
