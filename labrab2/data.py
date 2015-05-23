from labrab2.models import Sportsmen, Contest, Contestant
'''
sp1 = Sportsmen()
sp1.id = 1
sp1.fio = 'Sultan Suleyman'
sp1.country = 'Russia'
sp1.bdate = '1995-08-12'
sp1.save()

cont1 = Contest()
#cont1.cont_id = 1
cont1.place = 'Tomsk'
cont1.type = 'Marathon'
cont1.save()

contestant1 = Contestant()
contestant1.contestant = sp1
contestant1.contestant_place = 1
contestant1.save()
'''
sportsman1 = Sportsmen.objects.create(id=1, fio='Sportsman #1', country='sf', bdate = '1995-12-12')
sportsman2 = Sportsmen.objects.create(id=2, fio='df', country='sf', bdate = '1995-12-12')
sportsman3 = Sportsmen.objects.create(id=3, fio='df', country='sf', bdate = '1995-12-12')

contest1 = Contest.objects.create()
contest1 = Contest.objects.create()
contest1 = Contest.objects.create()

contestant2 = Contestant.objects.create(contestant=sp2, contestant_place=2)
contestant2 = Contestant.objects.create(contestant=sp2, contestant_place=2)
contestant2 = Contestant.objects.create(contestant=sp2, contestant_place=2)
