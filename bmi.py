def calculate_bmi(height,weight):
    print("Height= "+str(height))
    print("Weight= "+str(weight))
    bmi=weight/(height*height)
    print(f"BMI value is {bmi:2f}")
    if(bmi<18.5):
        return -1
    elif (18.5<=bmi<=25.0):
        return 0
    elif(bmi>25.0):
        return 1
if name=="_main_":
    main()
calculate_bmi(weight=57.90,height=1.63)