from django.shortcuts import render
from production.models import Sb1010, Sd3010
from django.db.models import F
from django.db.models.functions import Concat, Substr
from django.db import connection
from django.http import HttpResponse

def list_production(request):
   
    


    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl not in (select d3_loteprt from sd3010 where  d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        not_started = cursor.fetchall()
   
 
    
   
   

    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4) from sd3010,sb1010 where b1_cod=d3_cod and d3_quant=0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' and d3_lotectl in (select d3_loteprt from sd3010 where d3_loteprt<>'' and sd3010.d_e_l_e_t_<>'*' group by d3_loteprt) order by substr(d3_op,9,3) desc;""")
        started = cursor.fetchall()

      


    with connection.cursor() as cursor:
        cursor.execute( """select d3_cod,b1_desc,d3_lotectl,substr(d3_emissao,7,2)||'/'||substr(d3_emissao,5,2)||'/'||substr(d3_emissao,1,4)  from sd3010,sb1010 where b1_cod=d3_cod and d3_emissao>='20230801' and d3_quant>0 and d3_tm='100' and sd3010.d_e_l_e_t_<>'*' order by substr(d3_op,9,3) desc;""")
        concluded = cursor.fetchall()

    
    
    return render(request,'production/list.html', context={'not_started':not_started, 'started':started, 'concluded':concluded,}
)





