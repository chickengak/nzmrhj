import joblib
import numpy as np
import pandas as pd

model_pkl = joblib.load('static/model.pkl')   # 모델 불러오기
scaler_X = joblib.load('static/scaler_X.pkl') 
scaler_y = joblib.load('static/scaler_y.pkl')  

def asdf():
    return 'my_res'

def model_pkl_predict(input_values:list):
    """
    input: list  (length: 12)
    output: int
    입력된 값으로 예측값을 리턴. scaler_X 와 scaler_y 필요함.
    """
    #standardized_input = np.append( scaler_X.transform(np.array(input_values[:11]).reshape(1, -1)) , [input_values[11]]) # input_values는 12개의 특성이고 마지막 데이터가 병원이라고 가정함.
    standardized_input = np.append( scaler_X.transform(pd.DataFrame([input_values[:11]],
                        columns=['area','trans_floor','com_year','interest','household','top_floor','subway_dist','subway_cnt','bus_cnt','parking_lot','school'])) , [input_values[11]])
    res = model_pkl.predict(pd.DataFrame(standardized_input.reshape(1,12),
                    columns=['area', 'trans_floor', 'com_year', 'interest', 'household', 'top_floor', 'subway_dist', 'subway_cnt', 'bus_cnt', 'parking_lot', 'school', 'hospital'])) # 예측 결과
    inv_standardized_res = scaler_y.inverse_transform(np.reshape(res, (-1, 1)))      # 역 표준화 된 예측 결과
    return round(np.exp(inv_standardized_res)[0][0])     # 반올림한 int로 반환. 어차피 만단위 결과니까.