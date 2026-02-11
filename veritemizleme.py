text= "Hello,      world!  ,   2035  "
#metinde fazladan bulunan boşlukları tek bir boşluk yaparak temizleyelim
temizlenmis_text = " ".join(text.split())
#" ". tekrar birleştrirken aralarına ne koyacağunı belirler boşluk koycn
print("Orijinal metin:", text)
print("Temizlenmiş metin:", temizlenmis_text)
#büyük -> küçük harfe çevirme 
kucuk_harf_text = temizlenmis_text.lower()
print("Küçük harfe çevrilmiş metin:", kucuk_harf_text)
#noktalama işaretlerini temizleme
import string
text2= "Hello world! This is a test. Do you like it?"
cleaned_text = text2.translate(str.maketrans("", "", string.punctuation))
#1.parametre değişcekler 2.parmetre hedefler 3.parametre silinecekler
#translate: metin içindeki belli karakterleri toplu biçimde değiştrimek veya silmek için 
#string .punctuation: tüm noktalama işaretlerini içeren bir dize sağlar
#"","" bu ise hiçbir karakteri değiştirmeden bırakmak için kullanılır,
#str.maketrans hangi karakterin eşleşceğini hangi karakterin silinceği belirtmek için kullanılır 
#burda str.make trans ile neyin silinceğini belirrtik 
print("Noktalama işaretleri temizlenmiş metin:", cleaned_text)
#özel karakterleri temizleme
import re
#düzenli ifadeler kütüphanesi
text3 = "Hello@world#2025$"
cleaned_text2 = re.sub(r'[^A-Za-z0-9\s]', '', text3)
#1.parametre arananlar 2.parametre yerine koyulacak şey "" hiç demek yani sil demek 3.parametre ise hangi metin üzerinde işlem yapılacak
#re.sub: metin içerisindeki başka bir kalıba yada hiçbirşeyi yani silerek değiştriri 
#r'[^A-Za-z0-9\s]': bu düzenli ifade, metindeki özel karakterleri tanımlar.
# tüm büyük ve küçük harfler (A-Z, a-z), rakamlar (0-9) ve boşluk karakterleri (\s) dışındaki karakterleri eşleştirir.   
print("Özel karakterler temizlenmiş metin:", cleaned_text2)
#yazım hatalarını düzeltme
from textblob import TextBlob
#textblob npl de basitlik odaklı önemli bir kütüphane
#karmaşık algoritmalarla uğraşmak yerine sanki bir metin dosyasıyla oynuyormuşsun gibi dil analizi yapmana imkan sağlar 
text4 = "I havv a speling eror."
cleaned_text3 = str(TextBlob(text4).correct())
#textblo.correct text hatalarını otomatiik düzeltmeye yarar 
print("Yazım hataları düzeltilmiş metin:", cleaned_text3)
#html yada url temizleme
from bs4 import BeautifulSoup
#beautifulsoup html ve xml belgelerini ayrıştırmak için kullanılan bir python kütüphanesidir
text5 = "<html><body><h1>Hello, world!</h1><p>This is a test.</p></body></html>"
#beautifulsoup ile html yapısını parse et , get_text ile text kısmını çek 
cleaned_text4 = BeautifulSoup(text5, "html.parser").get_text()
#beatfulsoup(text5, "html.parser") ile henüz temiz bir metin oluşturmazsın anlyabilmesi için düzenlenmiş bir nesne 
#vardır get_text ile temiz metne çekersin ve get_text bs nin özel bir metodurdur
print("HTML temizlenmiş metin:", cleaned_text4)