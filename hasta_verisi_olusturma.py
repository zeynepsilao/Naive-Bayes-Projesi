import pandas 
import numpy 

#Bu kısımda değişkenimizi tanımladık
veri = []

#Bu kısımda belirtileri belirledik
belirtiler = ['Gozde Kizariklik','Burun Tikanikligi','Nefes Darligi','Ayakta Uyusma','Elde Uyusma',
              'His Kaybi','Bas Agrisi','Kusma','Ishal','Koku Kaybi','Tat Kaybi',
              'Sislik','Ates', 'Uykusuzluk', 'Oksuruk', 'Halsizlik', 'Karin Agrisi',
              'Goz Yanmasi','Hapsuruk',' Deride Kizariklik']

#Bu kısımda hastalıkları belirledik
hastaliklar = ['Diyabet','Tuberkuloz','Kolera','Hepatit C','Noravirus','Dizanteri',
               'Bagirsak Enfeksiyonu','Opucuk Hastaligi','Menenjit','Sucicegi',
               'Kirmizi Goz','El, Ayak, Agiz Hastaligi','Bademcik Efeksiyonu','Mide Gribi'
               ,'Soguk Alginligi','Grip', 'Nezle', 'Bronsit', 'Apandisit', 'Gastrit']

#Kodu her çalıştırdığımızda aynı rastgele değerleri versin diye seed ekledik
numpy.random.seed(50) 


#Bu kısımda rastgele belirtli ve hastalik seçerek hasta oluşturduk ve bunu 100k kez yapmasını istedik

for i in range(0,100000):
    ornek = {}
    for belirti in belirtiler:
        ornek[belirti] = numpy.random.randint(0, 2) 
    ornek['TESHIS'] = numpy.random.choice(hastaliklar)  
    veri.append(ornek)
    


#Burda da hastaları dosyamıza ekledik ve satır no eklemesini istemedik
pandas.DataFrame(veri).to_csv('hasta_verileri.csv')