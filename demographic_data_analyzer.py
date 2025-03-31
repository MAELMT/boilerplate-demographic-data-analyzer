import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lire les données depuis le fichier
    df = pd.read_csv("adult.data.csv")

    # 1. Nombre de personnes par race
    race_count = df["race"].value_counts()

    # 2. Âge moyen des hommes
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Pourcentage de personnes ayant un Bachelor's
    percentage_bachelors = round((df["education"].value_counts(normalize=True)["Bachelors"]) * 100, 1)

    # 4. Pourcentage de personnes avec un diplôme avancé qui gagnent >50K
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_rich = round(
        (higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0]) * 100, 1
    )

    # 5. Pourcentage sans diplôme avancé qui gagnent >50K
    lower_education_rich = round(
        (lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # 6. Nombre minimum d'heures de travail par semaine
    min_work_hours = df["hours-per-week"].min()

    # 7. Pourcentage de personnes qui travaillent le minimum d'heures et gagnent >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # 8. Pays avec le plus fort pourcentage de >50K
    country_percentage = (df[df["salary"] == ">50K"]["native-country"].value_counts() /
                          df["native-country"].value_counts()) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9. Profession la plus fréquente en Inde parmi les >50K
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

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
