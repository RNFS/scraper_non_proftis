cause_name = {
    "Animals": [
        "Animal Rights",
        "Welfare and Services, Wildlife Conservation",
        "Zoos",
        "Veterinary Services Aquariums",
    ],
    "Arts": [
        "Libraries",
        "Historical Societies and Landmark Preservation",
        "Museums",
        "Performing Arts",
        "Public Broadcasting and Media",
        "Service and Other",
    ],
    "Culture": [
        "Libraries",
        "Historical Societies and Landmark Preservation",
        "Museums",
        "Performing Arts",
        "Public Broadcasting and Media",
        "Service and Other",
    ],
    "Humanities": [
        "Libraries",
        "Historical Societies and Landmark Preservation",
        "Museums",
        "Performing Arts",
        "Public Broadcasting and Media",
        "Service and Other",
    ],
    "Community Development": [
        "United Ways",
        "Jewish Federations",
        "Community Foundations",
        "Community Improvement",
        "Housing and Neighborhood Development",
    ],
    "Education": [
        "Early Childhood Programs and Services",
        "Youth Education Programs and Services",
        "Adult Education Programs and Services",
        "Special Education",
        "Education Policy and Reform",
        "Scholarship and Financial Support",
        "College and University",
        "Voter Education and Registration",
    ],
    "Environment": [
        "Environmental Protection and Conservation",
        "Botanical Gardens, Parks, and Nature Centers",
        "Pollution",
    ],
    "Health": [
        "Diseases, Disorders, and Disciplines",
        "Patient and Family Support",
        "Treatment and Prevention Services",
        "Medical Research",
        "Addiction and Substance Abuse",
        "Medical Disciplines and Specialty Research",
        "Mental Health and Crisis Serices",
    ],
    "Human Services": [
        "Children's and Family Services",
        "Youth Development, Shelter, and Crisis Services",
        "Food Banks, Food Pantries, and Food Distribution",
        "Multipurpose Human Service Organizations",
        "Homeless Services",
        "Social Services",
        "General Human Services",
        "Agriculture",
        "Food and Nutrition",
        "Crime and Legal Related",
        "Public Safety",
        "Disaster Preparedness, and Relief",
        "Recreation and Sports",
        "Mutual",
        "Membership Benefit Organization",
    ],
    "International": [
        "Poverty",
        "Development and Relief Services" "International Peace",
        "Security, and Affairs",
        "Humanitarian Relief Supplies",
        "Human Rights",
        "Civil Rights and Liberties",
        "Research & Public Policy",
        "Non-Medical Science & Technology Research",
        "Social and Public Policy Research",
        "Research Institutes",
    ],
    "Religion": [
        "Religious Activities, General",
        "Christian",
        "Hindu",
        "Islamic",
        "Jewish",
        "Religious Media and Broadcasting",
    ],
    "Unknown": ["Unclassified"],
}

for x in cause_name:
    print(x)
    for d in cause_name[x]:
        print(d)
    print("#" * 30)