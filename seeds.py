from app import db
from app.models.tables import Atividade
from datetime import date

a1 = Atividade(nome='Oficina GitHub', tipo='Oficina', data=date(2019, 10, 2), carga_horaria='8', arquivo='/1/487483.pdf', usuario_id=1)
a2 = Atividade(nome='BigData', tipo='Palestra', data=date(2020, 2, 10), carga_horaria='4', arquivo='1/938452.pdf', usuario_id=1)
a3 = Atividade(nome='Oficina Jekyll', tipo='Oficina', data=date(2020, 2, 12), carga_horaria='12', arquivo='/1/389943.pdf', usuario_id=1)

db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()