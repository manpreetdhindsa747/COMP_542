# Manpreet Dhindsa
# Ahmed Bin Sultan Bahyal

#region Dictionary Definitions
Workclass = {
    "Private": 1,
    "Self-emp-not-inc": 2,
    "Self-emp-inc": 3,
    "Federal-gov": 4,
    "Local-gov": 5,
    "State-gov": 6,
    "Without-pay": 7,
    "Never-worked": 8,
}

Education = {
    "Bachelors": 1,
    "Some-college": 2,
    "11th": 3,
    "HS-grad": 4,
    "Prof-school": 5,
    "Assoc-acdm": 6,
    "Assoc-voc": 7,
    "9th": 8,
    "7th-8th": 9,
    "12th": 10,
    "Masters": 11,
    "1st-4th": 12,
    "10th": 13,
    "Doctorate": 14,
    "5th-6th": 15,
    "Preschool": 16,
}

MaritalStatus = {
    "Married-civ-spouse": 1,
    "Divorced": 2,
    "Never-married": 3,
    "Separated": 4,
    "Widowed": 5,
    "Married-spouse-absent": 6,
    "Married-AF-spouse": 7,
}

Occupation = {
    "Tech-support": 1,
    "Craft-repair": 2,
    "Other-service": 3,
    "Sales": 4,
    "Exec-managerial": 5,
    "Prof-specialty": 6,
    "Handlers-cleaners": 7,
    "Machine-op-inspct": 8,
    "Adm-clerical": 9,
    "Farming-fishing": 10,
    "Transport-moving": 11,
    "Priv-house-serv": 12,
    "Protective-serv": 13,
    "Armed-Forces": 14,
}

Relationship = {
    "Wife": 1,
    "Own-child": 2,
    "Husband": 3,
    "Not-in-family": 4,
    "Other-relative": 5,
    "Unmarried": 6,
}

Race = {
    "White": 1,
    "Asian-Pac-Islander": 2,
    "Amer-Indian-Eskimo": 3,
    "Other": 4,
    "Black": 5,
}

NativeCountry = {
    "United-States": 1,
    "Cambodia": 2,
    "England": 3,
    "Puerto-Rico": 4,
    "Canada": 5,
    "Germany": 6,
    "Outlying-US(Guam-USVI-etc)": 7,
    "India": 8,
    "Japan": 9,
    "Greece": 10,
    "South": 11,
    "China": 12,
    "Cuba": 13,
    "Iran": 14,
    "Honduras": 15,
    "Philippines": 16,
    "Italy": 17,
    "Poland": 18,
    "Jamaica": 19,
    "Vietnam": 20,
    "Mexico": 21,
    "Portugal": 22,
    "Ireland": 23,
    "France": 24,
    "Dominican-Republic": 25,
    "Laos": 26,
    "Ecuador": 27,
    "Taiwan": 28,
    "Haiti": 29,
    "Columbia": 30,
    "Hungary": 31,
    "Guatemala": 32,
    "Nicaragua": 33,
    "Scotland": 34,
    "Thailand": 35,
    "Yugoslavia": 36,
    "El-Salvador": 37,
    "Trinadad&Tobago": 38,
    "Peru": 39,
    "Hong": 40,
    "Holand-Netherlands": 41,
}

Target = {
    "<=50K": 1,
    ">50K": 2
}
#endregion 

#region Person Class Definition
class Person:
    def __init__(self, data):
        self.age = data[0]
        self.workclass = data[1]
        self.fnlwgt = data[2]
        self.education = data[3]
        self.education_num = data[4]
        self.marital_status = data[5]
        self.occupation = data[6]
        self.relationship = data[7]
        self.race = data[8]
        self.sex = data[9]
        self.capital_gain = data[10]
        self.capital_loss = data[11]
        self.hours_per_week = data[12]
        self.native_country = data[13]

    def __repr__(self):
        return (f"age={self.age}\n"
                f"workclass='{self.workclass}'\n"
                f"fnlwgt={self.fnlwgt}\n"
                f"education='{self.education}'\n"
                f"education_num={self.education_num}\n"
                f"marital_status='{self.marital_status}'\n"
                f"occupation='{self.occupation}'\n"
                f"relationship='{self.relationship}'\n"
                f"race='{self.race}'\n"
                f"sex='{self.sex}'\n"
                f"capital_gain={self.capital_gain}\n"
                f"capital_loss={self.capital_loss}\n"
                f"hours_per_week={self.hours_per_week}\n"
                f"native_country='{self.native_country}'")
#endregion

def read_Data():
    People = [] # List of Person Classes
    with open("dataset/adult.data", "r") as file:
        for line in file:
            cleaned_line = [item.strip() for item in line.split(",")]
            person = Person(cleaned_line)
            People.append(person)
    return People

def main():
    People = read_Data() # List of Person Class, each index represents an instance
    print(People[0])

if __name__ == "__main__":
    main()
