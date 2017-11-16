import pandas as pd

result = pd.read_csv("result.csv")
ans = []
ans_p = []
for i in range(result.shape[0]):
    a = result.iloc[i]["TARGET"]
    if  a< 0.5:
        ans.append(0)
    else:
        ans.append(1)
    ans_p.append("%.4f" %a)
result_final = pd.DataFrame(result["EID"])
result_final["FORTARGET"] = ans
result_final["PROB"] = ans_p
result_final.to_csv("result_final.csv")
