from gempaterkini import GempaTerkini
import gempaterkini
if __name__ == '__main__':
    gempa = GempaTerkini('https://bmkg.go.id/')
    print('Deskripsi : ', gempa.description)
    gempa.run()



    gempa_dunia= GempaTerkini('https://climate.com')
    print('Deskripsi : ', gempa_dunia.description)
    gempa.run()

