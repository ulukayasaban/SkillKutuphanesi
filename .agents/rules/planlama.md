# Planlama ve Mimari Standartlar

Bir `/plan` veya geliştirme planı hazırlanırken yalnızca adımları sıralamakla kalma; aşağıdaki analizleri zorunlu olarak rapora ekle:
1. **Veri ve Çakışma Analizi:** Çoklu dosya, hassas JSON kayıtları veya eşzamanlı işlem varsa olası yarış durumu (race condition) ve veri kaybı risklerini değerlendir.
2. **Yürütme Yolu Önerisi (Swarm vs. Tekil Akış):** Görevin doğasına göre işin çoklu ajanla (Swarm/paralel) mı yoksa adım adım tek akışta (sequential) mı yapılmasının daha güvenli ve tutarlı olacağını gerekçelendir.
3. **Maliyet ve Kota Dengesi:** Seçilen yolun token sarfiyatı ve kota koruma (K2 kuralı) açısından etkisini değerlendirerek kullanıcıya net tavsiye sun.
