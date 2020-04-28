

def get_state(string):
    if " AL " in string:
        print("HIT")
    elif ' AK ' in string:
        return 'AK'
    elif ' AZ ' in string:
        return 'AZ'
    elif ' AR ' in string:
        return 'AR'
    elif ' CA ' in string:
        return 'CA'
    elif ' CO ' in string:
        return 'CO'
    elif ' CT ' in string:
        return 'CT'
    elif ' DC ' in string:
        return 'DC'
    elif ' DE ' in string:
        return 'DE'
    elif ' FL ' in string:
        return 'FL'
    elif ' GA ' in string:
        return 'GA'
    elif ' HI ' in string:
        return 'HI'
    elif ' ID ' in string:
        return 'ID'
    elif ' IL ' in string:
        return 'IL'
    elif ' IN ' in string:
        return 'IN'
    elif ' IA ' in string:
        return 'IA'
    elif ' KS ' in string:
        return 'KS'
    elif ' KY ' in string:
        return 'KY'
    elif ' LA ' in string:
        return 'LA'
    elif ' ME ' in string:
        return 'ME'
    elif ' MD ' in string:
        return 'MD'
    elif ' MA ' in string:
        return 'MA'
    elif ' MI ' in string:
        return 'MI'
    elif ' MN ' in string:
        return 'MN'
    elif ' MS ' in string:
        return 'MS'
    elif ' MO ' in string:
        return 'MO'
    elif ' MT ' in string:
        return 'MT'
    elif ' NE ' in string:
        return 'NE'
    elif ' NV ' in string:
        return 'NV'
    elif ' NH ' in string:
        return 'NH'
    elif ' NJ ' in string:
        return 'NJ'
    elif ' NM ' in string:
        return 'NM'
    elif ' NY ' in string:
        return 'NY'
    elif ' NC ' in string:
        return 'NC'
    elif ' ND ' in string:
        return 'ND'
    elif ' OH ' in string:
        return 'OH'
    elif ' OK ' in string:
        return 'OK'
    elif ' OR ' in string:
        return 'OR'
    elif ' PA ' in string:
        return 'PA'
    elif ' RI ' in string:
        return 'RI'
    elif ' SC ' in string:
        return 'SC'
    elif ' SD ' in string:
        return 'SD'
    elif ' TN ' in string:
        return 'TN'
    elif ' TX ' in string:
        return 'TX'
    elif ' UT ' in string:
        return 'UT'
    elif ' VT ' in string:
        return 'VT'
    elif ' VA ' in string:
        return 'VA'
    elif ' WA ' in string:
        return 'WA'
    elif ' WV ' in string:
        return 'WV'
    elif ' WI ' in string:
        return 'WI'
    elif ' WY ' in string:
        return 'WY'
    else:
        return "State Unknown"


print(get_state("Address VA 33333"))
