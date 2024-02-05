import joblib
import numpy as np
import pandas as pd

model_pkl = joblib.load('static/model.pkl')   # 모델 불러오기
scaler = joblib.load('static/scaler.pkl')

def model_pkl_predict(input_values:list):
    """
    input: list  (length: 12)
    output: int
    입력된 값으로 예측값을 리턴. scaler_X 와 scaler_y 필요함.
    """
    numeric_features = ['area', 'trans_floor', 'apt_age', 'interest', 'top_floor', 'bus_cnt', 'parking_lot', 'school', 'household']
    standardized_input = np.append( scaler.transform(pd.DataFrame([input_values[:9]], columns = numeric_features)) , [input_values[9:]])
    res = model_pkl.predict(pd.DataFrame(standardized_input.reshape(1,12),
                    columns=['area', 'trans_floor', 'apt_age', 'interest', 'top_floor', 'bus_cnt', 'parking_lot', 'school', 'household', 'gangnam_3gu', 'ent_type_계단식', 'ent_type_복도식'])) # 예측 결과
    print(res)
    return round(np.exp(res[0]))     # 반올림한 int로 반환. 어차피 만단위 결과니까.
