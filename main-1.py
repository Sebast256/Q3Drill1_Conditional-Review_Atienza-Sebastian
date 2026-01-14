from pyscript import document

def calculate_average(events):

    if not events:
        return 0

score1 = float(document.getElementById("score1").value)
score2 = float(document.getElementById("score2").value)

average = (score1 + score2) / 2

if average >= 75:
    result = "Yes"
elif average <= 75:
    result = "Fail"
else:
    result = "No"

document.getElementById("average").innerText = str(round(average, 2)) 
document.getElementById("result").innerText = result  