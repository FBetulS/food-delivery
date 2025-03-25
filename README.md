# Food Delivery Time Prediction

## 🔗 Kaynaklar
- Veri Seti: [Food Delivery Time Prediction Dataset](https://statso.io/food-delivery-time-prediction-case-study/)
- Hugging face: [Food Delivery Time Prediction Space](https://huggingface.co/spaces/btulftma/fooddelivery) (sorun yaşadım.)
 
## 📖 Proje Özeti
Yemek teslim süresi tahmini, gıda hizmetleri sektöründe müşteri memnuniyetini artırmak için kritik bir görevdir. Bu projede, restoran ile teslimat noktası arasındaki mesafeyi ve geçmiş teslimat sürelerini kullanarak, gerçek zamanlı teslimat sürelerini tahmin etmeyi amaçlıyoruz.

## 🛠️ Gerekli Kütüphaneler
Proje için aşağıdaki Python kütüphanelerine ihtiyaç vardır:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `warnings`
- `scikit-learn`
- `xgboost`
- `keras`
- `plotly`

## 📊 Veri Seti
Veri setimiz `deliverytime.txt` dosyasından alınmaktadır. Bu veri seti, aşağıdaki sütunları içermektedir:
- **ID**: Her bir teslimat kaydına atanmış benzersiz kimlik numarası.
- **Delivery_person_ID**: Teslimatı gerçekleştiren kişinin benzersiz kimlik numarası.
- **Delivery_person_Age**: Teslimatı gerçekleştiren kişinin yaşı.
- **Delivery_person_Ratings**: Teslimatı gerçekleştiren kişinin müşteri puanı (1-5 arası).
- **Restaurant_latitude**: Restoranın coğrafi enlem değeri.
- **Restaurant_longitude**: Restoranın coğrafi boylam değeri.
- **Delivery_location_latitude**: Teslimat noktasının coğrafi enlem değeri.
- **Delivery_location_longitude**: Teslimat noktasının coğrafi boylam değeri.
- **Type_of_order**: Siparişin türü (örneğin, atıştırmalık, içecek).
- **Type_of_vehicle**: Teslimat için kullanılan aracın türü (örneğin, motosiklet, scooter).
- **Time_taken(min)**: Teslimatın tamamlanması için geçen süre (dakika cinsinden).

## 📏 Mesafe Hesaplama
Haversine formülü, iki coğrafi nokta arasındaki mesafeyi hesaplamak için kullanılır. Bu mesafe, teslimat süresini tahmin etmek için kullanılacaktır.

## 📈 Veri Görselleştirme
Farklı görselleştirme yöntemleri kullanarak veri setini analiz ediyoruz. Önemli grafikler arasında:
1. Mesafe ve Teslimat Süresi İlişkisi
2. Yaş ve Teslimat Süresi İlişkisi
3. Teslimat Süresi ve Puanlar Arasındaki İlişki
4. Araç Türüne Göre Teslimat Süresi Dağılımı

## 🔧 Özellik Mühendisliği
Veri setinde bazı yeni kategoriler oluşturulmuş ve gereksiz sütunlar kaldırılmıştır. Kategorik değişkenler one-hot encoding ile dönüştürülmüştür.

## ⚙️ Modelleme
Farklı modeller kullanılarak teslimat süresi tahmini yapılmıştır:
- **Random Forest**
- **XGBoost**
- **Derin Öğrenme Modeli**

### Model Değerlendirme Sonuçları
- **Random Forest Model**: MSE: 57.87, MAE: 5.93, R²: 0.34
- **XGBoost Model**: MSE: 52.42, MAE: 5.70, R²: 0.40
- **Derin Öğrenme Model**: MSE: 51.79, MAE: 5.66, R²: 0.41

## 🏆 Sonuç
Yapılan modelleme çalışmaları sonucunda, en iyi performansı Derin Öğrenme modeli göstermiştir. Bu model, teslimat sürelerini tahmin etme konusunda diğer modellerden daha düşük hata oranlarına sahip olmuştur.


## 📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
