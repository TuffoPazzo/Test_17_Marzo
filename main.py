# Using the special variable
import functiones

# Defining main function
def main():
    print("Start")
    path_src ="C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\CartellaOrigine"
    path_dst = 'C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\CartellaDestinazione'
    path_report = 'C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\Report'

    lista_file_src = functiones.crea_lista_file(path_src)
    lista_file_dst = functiones.crea_lista_file(path_dst)
    lista_mancanti = functiones.compare_liste(lista_file_src,lista_file_dst)


    functiones.build_report(lista_mancanti,path_report)
    print('Stop')




# __name__
if __name__=="__main__":
    main()

