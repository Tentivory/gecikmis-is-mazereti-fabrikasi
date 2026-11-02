#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gecikmiş İş Mazereti Fabrikası
Tamamen saçma, abartılı ve eğlenceli mazeret üreticisi.
Gerçekten çalışır. Deneyin bakalım.
"""

import random
import base64

# Gizli not: ZW5jcmV0ZWQgcG9saXRpY2FsIGpva2UgaGVyZSBidXQgaXQncyBqdXN0IGFib3V0IGJ1cmVhdWNyYWN5IGRlbGF5cyBhbHdheXM=
# Yukarıdaki base64'u decode ederseniz sıkıcı bir şey çıkar. Merak etmeyin.

def gizli_mesaj():
    # Saklı siyasi espri (bürokrasi ile ilgili, tarafsız)
    encoded = "QnVyZW9rcmFzaSBoZXIgemFtYW4gZ2VjaWttZW5pbiB0ZW1lbCBuZWRlbmkgb2xtdXMgYW1hIGtpbXNlIGtpbXNlIGtpbXNlIGJ1IGhpa2F5ZXlpIHNveWxleWVmei4="
    try:
        return base64.b64decode(encoded).decode('utf-8')
    except:
        return "Gizli mesaj bozuldu, mazeret olarak kullanın."

mazeretler = {
    "trafik": [
        "Trafikte o kadar sıkıştım ki, yan şeritteki adamla birlikte kahvaltı yaptık. Yumurta bile kırıldı.",
        "Yol çalışması vardı, işçiler 'biraz bekleyin' dedi. 3 saat oldu, hala 'biraz' diyorlar.",
        "GPS 'sağa dön' dedi, döndüm, başka bir evrene çıktım."
    ],
    "hava": [
        "Hava o kadar kötüydü ki, şemsiye açılamadı, şemsiye açılmayı reddetti.",
        "Güneş 'bugün çıkmayacağım' dedi, karanlıkta yürüdüm, eşyalarım kayboldu.",
        "Rüzgar o kadar sertti ki, beni geriye doğru itti, evime döndüm."
    ],
    "teknoloji": [
        "Bilgisayarım 'bugün çalışmak istemiyorum' dedi ve kendini kapattı.",
        "İnternet o kadar yavaştı ki, bir mail göndermek için çay demledim, çay soğudu, mail hala gitmedi.",
        "Telefonum şarjı bitti, şarj cihazı da 'ben de yorgunum' dedi."
    ],
    "saçma": [
        "Kedim klavyenin üstüne yattı, işi bitirene kadar kalkmadı. Kedi işi bitirmedi.",
        "Düşündüm ki, işe gitmek yerine evde oturup düşüneyim. Düşünmek uzun sürdü.",
        "Kapı kilitlendi, anahtar da kayboldu. Anahtar 'ben de geciktim' diye not bıraktı."
    ]
}

def mazeret_uret(kategori=None):
    if not kategori or kategori not in mazeretler:
        kategori = random.choice(list(mazeretler.keys()))
    return random.choice(mazeretler[kategori])

def main():
    print("=== Gecikmiş İş Mazereti Fabrikası ===")
    print("Kategoriler: trafik, hava, teknoloji, saçma")
    print("Boş bırakırsanız rastgele seçer.\n")
    
    secim = input("Kategori seçin (veya enter): ").strip().lower()
    mazeret = mazeret_uret(secim if secim else None)
    
    print(f"\n🎉 İşte mazeretiniz: {mazeret}")
    print("\n(Gizli mesaj: ", gizli_mesaj(), ")")
    print("\nBu mazereti kullanın, sorumluluk kabul etmiyoruz.")

if __name__ == "__main__":
    main()

# Damga: Resmi Saçma Kod Mührü - 02.11.2026
# İmza: Kayyum Grok - Bu kod ciddiyetle yazıldı, ama hiç ciddi değil.
