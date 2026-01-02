import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import gradio as g

# Burada hasta verilerini DataFrame e dönüştürdük daha sonra belirtileri x'e Hastalıkları y'ye atadık
df = p.read_csv('hasta_verileri.csv')

x = df.drop('TESHIS', axis=1)
y = df['TESHIS']


#Bu kısımda veriminiz %20'sini test verisi olarak ayırdık kalanını da eğitim verisi olarak ayırdık bu kısım overfitting engel olmak için var
xegitim, xtest, yegitim, ytest = train_test_split(
    x, y, test_size=0.2, random_state=50, stratify=y)


#BU kısımda ise model değişkeninne bernoulli navie bayes algoritmasını öğrettik, ve verilerimizle eğittik
model = BernoulliNB()
model.fit(xegitim, yegitim)

#Burada x değişkenimize atadığımız belirtileri bir listeye dönüştürdük
belirtiler = list(x.columns)

#Burada kullanıcının girdiği belirtilere göre 1 ve 0 değerleri belirtiler listesiyle eşlenip sözlüğe dönüştürülür
#Daha sonra model hesaplamaları yapar ve yaptığı ilk tahmini tahmin değişkenine atayıp geri döndürür
def tahmin_et(*girdiler):
    veri_dict = dict(zip(belirtiler, girdiler))
    veri_df = p.DataFrame([veri_dict])
    tahmin = model.predict(veri_df)[0]
    return f"Hastaliginiz: {tahmin}"

#burada her bir belirti için kullanıcının tıklayabileceği kutucuklar oluşturulur
inputs = [g.Checkbox(label=belirti) for belirti in belirtiler] 

#Bu fonksiyon kullanıcının işaretledikleri True ve False olarak algılar daha daha sonra bunları 1 ve 0 olacak şekilde dğeiştirir
def wrapper(*args):
    binary_inputs = [1 if arg else 0 for arg in args]
    return tahmin_et(*binary_inputs)


#Bu kısım ise arayüzün tanımlamasıdır
arayuz = g.Interface(
    fn=wrapper,
    inputs=inputs,
    outputs="text",
    title="Hastalık Tahmin Sitesi",
    description="Lütfen belirtilerinizi girin.",
    flagging_options=["Kaydet"],)

#Bu kısım ise Gradio arayüzünü başlatır ve bize bir link gönderir
if __name__ == "__main__":
    arayuz.launch(share=True)