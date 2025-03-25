import streamlit as st
import pickle
import numpy as np

# Modeli yükle
def load_model():
    try:
        with open('best_deep_learning_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Model yüklenirken hata: {e}")
        return None

def main():
    st.title('Teslimat Süresi Tahmini')
    
    # Girdi alanları
    distance = st.number_input('Mesafe (km)', min_value=0.0, step=0.1)
    age = st.slider('Teslimat Elemanı Yaşı', 18, 60, 25)
    vehicle_type = st.selectbox('Araç Tipi', ['motorcycle', 'scooter'])
    order_type = st.selectbox('Sipariş Türü', ['meal', 'snack', 'drink'])
    
    # Model yükleme
    model = load_model()
    
    if st.button('Tahmini Süreyi Hesapla'):
        if model:
            # Özellik mühendisliği
            features = [
                float(np.log1p(distance)),  # Log dönüşümlü mesafe
                float(1 if vehicle_type == 'scooter' else 0),  # Vehicle type
                float(1 if order_type == 'snack' else 0),  # Order type
                float(1 if age < 25 else 0),  # Yaş kategorisi
                float(1 if age >= 35 else 0)
            ]
            
            # Tahmin
            try:
                # NumPy array olarak dönüştür
                input_array = np.array([features], dtype=np.float32)
                prediction = model.predict(input_array)[0]
                st.success(f'Tahmini Teslimat Süresi: {prediction:.2f} dakika')
            except Exception as e:
                st.error(f"Tahmin sırasında hata: {e}")
        else:
            st.error('Model yüklenemedi')

if __name__ == '__main__':
    main()
    