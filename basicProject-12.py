# interviewee screening
applicant={
  'raj':{'exprience':2,
       'languages':['python', 'c++','java'],
       'proj_superVions':False
       },
  'ramu':{'exprience':6,
       'languages':['python', 'c++','ruby'],
       'proj_superVions':False
       },
   'ruhal':{'exprience':5,
       'languages':['python', 'c++','java'],
       'proj_superVions':True
       },
    'salman':{'exprience':8,
       'languages':['python', 'c++','java'],
       'proj_superVions':True
       }
} 

exprience_required = 4 
languages_required=['python','java']

for name , cv_dict in applicant.items():
  if cv_dict['exprience'] >= exprience_required and \
    (set(languages_required).issubset(set(cv_dict['languages'])) or
    cv_dict['proj_superVions']):
     print(name+ ' pass the screen')