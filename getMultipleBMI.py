height_weight_list = [('Jhon',170,86),
                      ('Sarah', 166, 55),
                      ('Amy',158, 45)]

bmi_list=[]

for (name, height, weight) in height_weight_list :
    bmi = weight/(height / 100*height/100)
    bmi_list.append((name, bmi))

for (name, bmi) in bmi_list :
    print(name, " BMI : %4.1f " %bmi, end = " ")

    if bmi<18.5:
        print("LightWeight")
    elif bmi< 23:
        print("Normal")
    elif bmi< 25:
        print("OverWeight")
    elif bmi< 30:
        print("Obese")
    else :
        print("Extremely Obese")
