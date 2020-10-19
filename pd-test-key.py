import pandas as pd

tb1 = pd.DataFrame(
    {
        "weight":[80.0, 70.4,65.5,45.9,51.2],
        "height":[170, 180, 155, 143, 154],
        "type" : ["f","n","n","t","t"]


    }
)
print("몸무게 목록")
print(tb1["weight"])
print("몸무게와 키 목록")
print(tb1[["weight","height"]])
