def survive(blood_type, donated_blood):
    compatability = {
        "O": ["O"],
        "A": ["A" , "O"],
        "B": ["B", "O"],
        "AB": ["AB", "A", "B", "O"]
    }
    
    patient_abo = blood_type[:-1]
    patient_rh = blood_type[-1]
    
    for donor in donated_blood:
        donor_abo = donor[:-1]
        donor_rh = donor[-1]
        
        if donor_abo not in compatability[patient_abo]:
            continue
            
        if patient_rh == "-" and donor_rh == "+":
            continue
            
        return True
    return False