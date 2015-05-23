from labrab2.models import Sportsmen, Contest, Contestant

Sportsmen.objects.all().delete()
Contest.objects.all().delete()
sportsman1 = Sportsmen.objects.create(fio='Sportsman #1', country='Russia', bdate = '1990-11-30')

sportsman2 = Sportsmen.objects.create(fio='Sportsman #2', country='not_Russia', bdate = '1992-09-03')
sportsman2.save()
sportsman3 = Sportsmen.objects.create(fio='Sportsman #3', country='USA', bdate = '1991-01-25')
sportsman3.save()

contest1 = Contest.objects.create(pk=1, place='City#1', type='Marathon')
contest2 = Contest.objects.create(pk=2, place='City#2', type='Marathon')
contest3 = Contest.objects.create(pk=3, place='City#3', type='Sprint')

contestant1 = Contestant.objects.create(contestant=sportsman1, contest=contest1, contestant_place=1)
contestant2 = Contestant.objects.create(contestant=sportsman2, contest=contest1, contestant_place=2)
contestant3 = Contestant.objects.create(contestant=sportsman3, contest=contest3, contestant_place=4)
