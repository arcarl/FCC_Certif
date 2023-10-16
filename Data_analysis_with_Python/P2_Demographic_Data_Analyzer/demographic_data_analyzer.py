import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[df['education'] == 'Bachelors'])/len(df) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Dataframe split upon education
    df_educ = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    df_uneduc = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = len(df_educ[df_educ['salary'] == '>50K'])/len(df_educ) * 100
    lower_education_rich = len(df_uneduc[df_uneduc['salary'] == '>50K'])/len(df_uneduc) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    df_min_hours = df[df['hours-per-week'] == min_work_hours]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = len(df_min_hours[df_min_hours['salary'] == '>50K'])/len(df_min_hours) * 100

    # What country has the highest percentage of people that earn >50K?
    groupby_country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, '>50K']
    highest_earning_country = groupby_country_salary.idxmax()
    highest_earning_country_percentage = max(groupby_country_salary) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    df_rich = df[df['salary'] == '>50K']
    top_IN_occupation = df_rich[df_rich['native-country'] == 'India']['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
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
