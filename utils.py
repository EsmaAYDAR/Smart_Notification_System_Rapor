#utils.py
import random
from datetime import datetime

def generateMessage():
    """Rastgele bir bildirim mesajı üretir."""
    mesajlar = [
        "Sisteme yeni bir giriş yapıldı.",
        "Proje raporunuz onay bekliyor.",
        "Haftalık veri analizi tamamlandı.",
        "Yeni bir mesajınız var."
    ]
    secilenMesaj = random.choice(mesajlar)
    zaman = datetime.now().strftime("%H:%M:%S")
    return f"{secilenMesaj} (Oluşturulma: {zaman})"

def send_notifications(notification_list):
    """Polimorfizm örneği: Listeyi döner ve send() metodunu çalıştırır."""
    for n in notification_list:
        n.send()