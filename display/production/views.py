from django.shortcuts import render, redirect
from production.models import  Sd3010
from django.db import connection
from django.contrib import messages





from django.urls import path


# Retorna os valores das colunas da Home
def list_production(request):
   
    

    #Retorna os valores da coluna dos elementos criados
    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl not in (select d3_loteprt from sd3010 where  d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        not_started = cursor.fetchall()
   
 
    
   
   
    #Retorna os valores da coluna dos elementos iniciados
    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl in (select d3_loteprt from sd3010 where d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        started = cursor.fetchall()

      

    #Retorna os valores da coluna dos elementos concluídos
    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4)  from sd3010,sb1010 where b1_cod=d3_cod and d3_emissao>='20230801' and d3_quant>0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' order by substr(d3_op,9,3) desc;""")
        concluded = cursor.fetchall()

    
    
    return render(request,'production/list.html', context={'not_started':not_started, 'started':started, 'concluded':concluded,}
)




#Busca e retorna os valores para a página dos produtos criados
def production_started(request):

    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl not in (select d3_loteprt from sd3010 where  d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        not_started = cursor.fetchall()
   


    return render(request, 'production/criados.html', context={'not_started':not_started,})


#Implementação das condições para o elemento mudar de status no banco de dados
def change_status_production_to_started(request):
    if request.method == 'POST':
        cod_production=request.POST.get('code_product_not_started', '')
        if cod_production=='':
            raise Exception('cod production not found')
        
        try:
            
            
            sd3010 = Sd3010.objects.filter(d3_lotectl=cod_production).first()
            sd3010.d3_loteprt = cod_production
            sd3010.save()
            
            return redirect('productions:production_started')
        except:
            raise Exception('Producton not found')
    
    raise Exception('not permission method get')


#Busca e retorna os valores para a página dos produtos iniciados
def concluded(request):

    with connection.cursor() as cursor:
        cursor.execute("""select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl in (select d3_loteprt from sd3010 where d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        started = cursor.fetchall()
   


    return render(request, 'production/iniciados.html', context={'started':started,})


#Implementação das condições para o elemento mudar de status no banco de dados
def change_status_production_concluded(request):
    if request.method == 'POST':
        cod_production=request.POST.get('code_product_started', '')
        if cod_production=='':
            raise Exception('cod production not found')
        
        try:
            
        
            sd3010 = Sd3010.objects.filter(d3_lotectl=cod_production).first()
            sd3010.d3_emissao ='20230802' 
            sd3010.d3_quant ='1'
            sd3010.save()
            
            return redirect('productions:concluded')
        except:
            raise Exception('Producton not found')
    
    raise Exception('not permission method get')





