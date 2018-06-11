from django.contrib import admin
from import_export import resources
from .models import Person, Upload
from import_export.admin import ImportExportModelAdmin


class PersonResource(resources.ModelResource):

	class Meta:
		model = Person 

admin.site.register(Person)

@admin.register(Upload)
class Uploadadmin(admin.ModelAdmin):
    list_display = ('file','created_at')




@admin.register(PartnerAuxiliar)
class PartnerUpdateAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fan_dun','grupo_especial','activo')


# def upload_csv(request):
#     try:
#         csv_file = request.FILES["csv_file"]
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return reverse
#         if csv_file.multiple_chunks():
#             messages.error(request,"uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#             return redirect
#         file_data = csv_file.read().decode("utf-8")
#         lines=file_data.split("\n")
#         for line in lines:
#             fields= line.split(".")
#             data_dict={}
#             data_dict=["nombre"]= fields[0]
#             data_dict["fan_dun"]=fields[1]
#             data_dict["grupo_especial"]=fields[2]
#             data_dict["activo"]=fields[3]
#             try:
#                 form=



# with open('test_excel_2.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     header = next(reader)
#     for r in row[4]:
#         if r =="True":
#             return True
#         elif r =="False":
#             return False
#     for r in row[3]:

           
#     PartnerAuxiliar.objects.bulk_create([
#         PartnerAuxiliar(nombre=row[0], 
#                         fan_dun=row[1],
#                         grupo_especial=row[4],
#                         activo=row[5]) 
#         ])

# from distutils.util import strtobool

# def rows():
# with open('test_excel_2.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     header = next(reader)
#     list_in = list(reader)
#     print list_in
#     for row in reader:
#         for r in row[4]:
#             if r == "True":
#                 r= True              
#                 print r
#             elif r=="False":
#                 r=False
#                 print r

# with open('test_excel_2.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     header = next(reader)
#     list_in = list(reader)
#     print list_in
#     for r in reader[4]:
#         if r == "True":
#             r= True              
#             print r
#         elif r=="False":
#             r=False
#             print r


# f = open('test_excel_2.csv')
# reader = csv.reader(f, delimiter=',')
# header = next(reader)
# list_in = list(reader)
# print list_in
# for row in reader:
#     if row[2] =="1":
#         print row
      
    
# with open("test_excel.csv") as file:
#     reader = csv.reader(file)
#     next(reader)
#     data=[r for r in reader]
#     print data
#     for element in data[1]:
#         print element
#         print type(element)
#         for i in element[1]: 
#             print i
#             print type(i)


# import csv, sys
# filename = 'some.csv'
# with open(filename, 'rb') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print row
#     except csv.Error as e:
#         sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


# import csv, sys
# filename = 'test_excel.csv'
# with open(filename, 'rb') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print row
#              """ convert strings from CSV file to valid Bolean Values
#              before interaction with DB
#             """
#             if row[2]=="True":
#                 print ("hello")
#                 row[2]=True
#                 print row[2]
#             elif row[2]=="False":
#                 row[2]=False
#                 print row[2]
#             if row[3]=="True":
#                 row[3]==True
#                 print row[3]
#             elif row[3]=="False":
#                 row[3]=False
#                 print row[3]
#             print row
#             PartnerAuxiliar.objects.bulk_create([
#             PartnerAuxiliar(nombre=row[0], 
#                         fan_dun=row[1],
#                         grupo_especial=row[2],
#                         activo=row[2]) 
#         ])
#     except csv.Error as e:
#      sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

#  ''' try'''
# import csv, sys
# filename = 'test_excel.csv'
# f= open(filename, 'rb')
# reader = csv.reader(f)
# header = next(reader)
# qs = PartnerAuxiliar.objects.values('nombre').distinct()
# try:
#     for col in reader:
#         print col
#         if col[2]=="True":
#             col[2]=True
#             print col[2]
#         elif col[2]=="False":
#             col[2]=False
#             print col[2]
#         if col[3]=="True":
#             col[3]==True
#             print col[3]
#         elif col[3]=="False":
#             col[3]=False
#             print col[3]
#         print col
#         for name in qs:
#             if name ==col[0]:
#                 print col[0]

#         PartnerAuxiliar.objects.bulk_create([
#         PartnerAuxiliar(nombre=col[0], 
#                     fan_dun=col[1],
#                     grupo_especial=col[2],
#                     activo=col[3]) 
#     ])
# except csv.Error as e:
#  sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

import csv, sys
filename = 'test_excel.csv'
f= open(filename, 'rb')
reader = csv.reader(f)
header = next(reader)
qs_partner = PartnerAuxiliar.objects.values('nombre').distinct()
qs_fan_dun = PartnerAuxiliar.objects.values('fan_dun').distinct().exclude(fan_dun__isnull=True).exclude(fan_dun__exact='')
try:
    for row in reader:
        print row[0]
        if row[2]=="True":
            row[2]=True
            # print row[2]
        elif row[2]=="False":
            row[2]=False
            # print row[2]
        if row[3]=="True":
            row[3]==True
            # print row[3]
        elif row[3]=="False":
            row[3]=False
            # print row[3]
        print row
        for name in qs_partner:
            print name['nombre']
            if name['nombre'] ==row[0]:

                print 'coincidence for this name \n'
                

except csv.Error as e:
 sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


#  Partner.objects.filter(name__icontains=)
