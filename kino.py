import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

mylist = raw_input('balte ti lista sas: ')
mylist = [int(t) for t in mylist.split(',')]




if(len(mylist)==10):
	def compare_lists(l1,l2):
		s=0
		for i in l1:
			if i in l2:
				s+=1
		return s
	x= 0
	for i in range(11):
		cur_date= cur_date - datetime.timedelta(days=1)
		date_str= cur_date.strftime("%d-%m-%Y")
		url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		data = response.read()
		data=json.loads(data)
		klhrwseis= data['draws']['draw']
		r=[]
		for k in klhrwseis:
			tmp=k["results"]
			r.append(compare_lists(mylist,tmp))
		print "apotelesmata",date_str
		if (max(r) > 4):
			print max(r),"epityxia"
			if (max(r)>x):
				x=max(r)
				y=date_str
		else:
			print "atyxia"
		print 20*"-"
	print "H megalyterh epityxia htan : ",(x) 		
	print "pragmatopoihthike stis : ", (y)
else:
	print "balte mia lista 10 arithmon"