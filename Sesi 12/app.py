import pandas as pd

def update_Score(score):
    newScore = score + 20
    return newScore

def grade(score):
    return "A"

scores = pd.read_excel("data-score.xlsx","TI24E")
scores["New Score"] = scores["Score"].apply(update_Score)
scores["Grade"] = scores["New Score"].apply(grade)
scores.to_excel("sample-score.xlsx", index=False)
