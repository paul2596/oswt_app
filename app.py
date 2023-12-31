from flask import Flask, render_template, request, jsonify
import joblib
import time
import numpy as np
import os

app = Flask(__name__)

#get model directory path manually as azure isn't recognizin
model_dir = os.path.join(os.path.dirname(__file__), 'models')

print('Testing')
@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    print('service hit successfull')

    error_value = True

    data = request.json 
    input_data = data.get('data')
    test_type = data.get('testType')
    direction = data.get('direction')
    features = []
    Pitch_Deg_Mean = float(input_data.get('pitchangle')) 
    Anemo_T_Mean = float(input_data.get('windspeed'))
    WindVane_T_Mean = float(input_data.get('winddirection'))
    model = None
    if((Pitch_Deg_Mean !=0)
       & (Anemo_T_Mean !=0)
       & (WindVane_T_Mean !=0)):
        error_value = False
        print('entered initial loop')

        if(test_type=='temp_all_direction'):
            print('temp_all_direction')
            temp_T_Mean = float(input_data.get('temperature'))
            features = [Pitch_Deg_Mean, Anemo_T_Mean, WindVane_T_Mean, temp_T_Mean] 
            model_path = os.path.join(model_dir, 'XG_Boost_initial_features_temp_orig-data_model.sav')
            model = joblib.load(model_path)
        if(test_type=='t2m_d2m'):
            print('t2m_d2m')
            t2m = float(input_data.get('t2m'))
            d2m = float(input_data.get('d2m'))
    
            features = [Pitch_Deg_Mean, Anemo_T_Mean, WindVane_T_Mean, t2m, d2m] 
            if(direction=='west'):
                
                model_path = os.path.join(model_dir, 'XG_Boost_initial_features_t2m_d2m_orig-data_west-ocean_model.sav')
                model = joblib.load(model_path)
            elif(direction=='east'):
                model_path = os.path.join(model_dir, 'XG_Boost_initial_features_t2m_d2m_orig-data_east-sea_model.sav')
                model = joblib.load(model_path)
        if(test_type=='obhL'):
            obhL = float(input_data.get('obhL'))
            features = [Pitch_Deg_Mean, Anemo_T_Mean, WindVane_T_Mean, obhL] 
            if(direction=='west'):
                model_path = os.path.join(model_dir, 'XG_Boost_initial_features_obhL_orig-data-era5-30km-obhL_west-ocean_model.sav')
                model = joblib.load(model_path)
            elif(direction=='east'):
                model_path = os.path.join(model_dir, 'XG_Boost_initial_features_obhL_orig-data-era5-30km-obhL_east-sea_model.sav')
                model = joblib.load(model_path)

        prediction = model.predict([features])
        time.sleep(2.0)
        return jsonify({'prediction': str(prediction[0])})
    else:
        return jsonify({'error': error_value})

#log error   
@app.errorhandler(Exception)
def handle_error(e):
    return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

