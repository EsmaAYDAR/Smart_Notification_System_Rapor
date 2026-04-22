# Smart Notification System
Nesne yönelimli programlama (OOP) prensipleri kullanılarak geliştirilmiş; modüler yapı, kalıtım ve çok biçimlilik içeren gelişmiş bir bildirim yönetim sistemi.

# Proje Tanımı ve Amaç
Bu proje, nesne yönelimli programlama (Object-Oriented Programming - OOP) yaklaşımı kullanılarak farklı kanallar (Email, SMS, Push) üzerinden bildirim gönderimini simüle etmek amacıyla geliştirilmiştir. Projenin temel odağı, yazılım dünyasındaki karmaşık sistemlerin nasıl daha modüler, sürdürülebilir ve esnek bir yapıya kavuşturulabileceğini göstermektir.

Geleneksel yöntemlerde her bildirim türü için ayrı ayrı kod yazmak yerine, bu projede ortak bir temel sınıf üzerinden türetilen yapılar kullanılmıştır. Bu sayede sistem bileşenleri birbirinden bağımsız olarak geliştirilebilir ve tek bir merkezden (polymorphism yardımıyla) yönetilebilir hale getirilmiştir.

# Projenin Temel Hedefleri:
Bildirim yönetim süreçlerini nesne tabanlı modellemek.

Modüler kod yapısı sayesinde "tak-çıkar" (pluggable) bir sistem oluşturmak.

Polymorphism ve Inheritance gibi ileri düzey OOP kavramlarını gerçek hayata uygun bir senaryoda uygulamak.

Hata yönetimi mekanizmaları ile sistem güvenilirliğini artırmak.

# Teknik Değerlendirme ve Rapor
Hocamızın belirttiği kritik soruların teknik açıklamaları ve projedeki uygulama karşılıkları aşağıdadır:

1. Polymorphism Nedir ve Inheritance’tan Farkı Nedir?
Inheritance (Kalıtım): Bir sınıfın (Base Class), sahip olduğu özellikleri ve metodları başka bir sınıfa (Sub-Class) aktarmasıdır. Bu projede EmailNotification sınıfının Notification sınıfından mesaj ve tarih özelliklerini miras alması bir inheritance örneğidir. "Nedir?" (is-a) ilişkisini temsil eder.

Polymorphism (Çok Biçimlilik): Aynı isimdeki bir metodun (send()), farklı nesneler üzerinde farklı çıktılar üretme yeteneğidir.

Fark: Inheritance bir yapı kurar (kod paylaşımı sağlar), Polymorphism ise bu yapı üzerindeki davranışı yönetir. Polymorphism sayesinde yönetici fonksiyonumuz, gelen nesnenin türünden bağımsız olarak sadece send() komutunu verir ve her bildirim türü kendi tarzında çalışır.

2. __str__ Gibi Özel Metodlar Neden Kullanılır?
Python'da "Dunder" (Double Underscore) metodları, nesnelerin dilin yerleşik fonksiyonlarıyla uyumlu çalışmasını sağlar.

Kullanım Nedeni: Eğer __str__ kullanmazsak, bir nesneyi yazdırmak istediğimizde anlamsız bir bellek adresi görürüz. Bu metod sayesinde nesneyi yazdırdığımızda kullanıcıya anlamlı bir mesaj sunarız.

Projedeki Rolü: __str__ ile bildirimin içeriğini ve zamanını şık bir formatta gösterirken, __len__ ile bildirim mesajının uzunluğunu doğrudan nesne üzerinden ölçebiliyoruz.

3. Modüler Kodun Avantajları
Kodun notifications.py ve utils.py gibi ayrı dosyalara bölünmesi şu avantajları sağlar:

Bakım Kolaylığı: Bir hata oluştuğunda sadece ilgili modül kontrol edilir, sistemin geneli etkilenmez.

Yeniden Kullanılabilirlik: Yazılan bildirim modülü, başka bir projeye sadece dosya kopyalanarak saniyeler içinde entegre edilebilir.

Ekip Çalışması: Farklı geliştiriciler farklı modüller üzerinde aynı anda çalışabilir, bu da iş verimliliğini artırır.

4. Hata Yönetimi Olmayan Bir Sistemde Ne Olur?
Hata yönetimi (try-except), sistemin "emniyet kemeri"dir. Hata yönetimi olmayan bir sistemde:

Sistem Çökmesi: Beklenmedik bir veri (örneğin boş bir mesaj) programın aniden durmasına (crash) neden olur.

Güvenlik Riskleri: Ham hata mesajları sistemin dosya yollarını dışarıya sızdırabilir.

Kötü Kullanıcı Deneyimi: Kullanıcı işlemin neden başarısız olduğunu anlamaz. Bizim sistemimizdeki ValueError kontrolü, kullanıcıya hatasını nazikçe bildirerek programın akışını korur.

Esma AYDAR
