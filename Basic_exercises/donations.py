donations = {
    'jadi': 20,
    'sara': 800,
    'far': 12,
    'hasan': 9
    } 
def donation_analysis(don):
    max_person = ''
    total = 0
    count = 0
    max_donation = -1
    for name, value in don.items():
        total += value
        count += 1
        if value > max_donation:
            max_person = name
            max_donation = value
    
    average = int(total / count)
    return average, total, max_person

avg, total, max_person = donation_analysis(donations)

print(f"total donations : {total}")
print(f"average donations is {avg}")
print(f"thanks to {max_person}")
