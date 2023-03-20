import os
import classes

#Funzione per trovare e filtare tutti i file (.fastq.gz o .csv) al interno della cartella di origine 
def crea_lista_file(path_da_scansionare):
    list_files = []
    for root, _, files in os.walk(path_da_scansionare):
        for nome_del_file in files:
            path_del_file = os.path.join(root, nome_del_file) 
            if nome_del_file.endswith(".fastq.gz") or nome_del_file.endswith(".csv"):
                file_corrente = classes.DettagliFile(path_del_file)
                list_files.append(file_corrente)
    return list_files

def compare_liste(lista1, lista2):
    lista_elementi_mancanti = []

    for elemento_lista1 in lista1:

        trovato = False

        for elemento_lista2 in lista2:
            if elemento_lista1.compare(elemento_lista2):
               if trovato == False:
                   trovato  = True

        if trovato == False:
            lista_elementi_mancanti.append(elemento_lista1)

        
        
    return lista_elementi_mancanti
            
def build_report(lista,path_report):
    with open('Report.csv', 'w') as Report:
        Report.writelines('Numero elementi mancanti: ' + str(len(lista)) + '\n')
        for elm in lista:
            Report.writelines(elm.name + ',  ' + elm.path + '\n') 


path_src ="C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\CartellaOrigine"
path_dst = 'C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\CartellaDestinazione'
path_report = 'C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\Report'

lista_file_src = crea_lista_file(path_src)
lista_file_dst = crea_lista_file(path_dst)
lista_mancanti = compare_liste(lista_file_src,lista_file_dst)


build_report(lista_mancanti,path_report)


##PULISCO IL PERCORSO FILE DALLA LISTA 
#for el in O_filelist:
#      O_final_filelist.append(el.split("\\")[-1])
#
#
#path ="C:\\Users\\GiulioNocco\\Desktop\\ITS\\Python\\TEST_17Marzo\\cartelle prova\\CartellaDestinazione"
##we shall store all the file names in this list
#D_allfilelist = []
#D_filelist = []
#D_final_filelist = []
#Elementi_Mancanti =[]
#
##PRENDO TUTTI I FILE PRESENTI NALLA CARTELLA DI DESTINAZIONE (BACKUP)
#for root, dirs, files in os.walk(path):
#	for file in files:
#        #append the file name to the list
#		D_allfilelist.append(os.path.join(root,file))
#
##PRENDO I FILE FORMATO .fastq.gz e .csv
#for x in D_allfilelist:
#    if x.endswith(".fastq.gz") or x.endswith(".csv"):
#        # Prints only text file present in My Folder
#        D_filelist.append(x)
#
##PULISCO IL PERCORSO FILE DALLA LISTA 
#for el in D_filelist:
#      D_final_filelist.append(el.split("\\")[-1])
#
#print(D_final_filelist)
#
#print("--------------------------------------------------------------------------------------------------")
#
##FILE NON PRESENTI NELLA CARTELLA DI BACK UP
#for elm in O_final_filelist:
#      if elm not in D_final_filelist:
#             Elementi_Mancanti.append(elm)
#
#print(Elementi_Mancanti)
#
#File_Report = open('File_Report.txt', 'w')
#if Elementi_Mancanti.len == 0:
#    File_Report.write('Tutto OK nessun elemento mancante')
#else:
#    File_Report.write('!!ATTENZIONE!! Numero elementi non trovati:' + str(Elementi_Mancanti.len)) 