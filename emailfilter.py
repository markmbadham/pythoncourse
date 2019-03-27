emails = ''' pillayav@state.gov
thomasonrr@state.gov
buchwaldms@state.gov
vermaakmx@state.gov
orangeca@state.gov
ramafigj@state.gov
mabenazx@state.gov
sellomol@nedbank.co.za
daniel.green@necsa.co.za
dawid.dippenaar@necsa.co.za
francois.vandermerwe@necsa.co.za
michael.hayes@necsa.co.za
warren.phillips@necsa.co.za
Mamelitsoe.Mojapela@za.man-mn.com
Yolanda.Freitag@exxaro.com
rene.dutoit@exxaro.com
maepannie@gmail.com
bradleyC@bankservafrica.com
BusiswaM@bankservafrica.com
Yougandrie.oosthuizen@angloamerican.com
annekegeringer@gmail.com
kefilwe.mphake@gauteng.gov.za 
mnqobi.ngcobo@dst.co.za
camambala@gmail.com
pebane2015@breakthru.com
Buki@bnvconsult.co.za
stebodi@yahoo.com
batsile.molebatsi@gmail.com
s.garland@rcon.co.za
d.naidoo@rcon.co.za
lmakhosa@stoncor.com
khumo@itsago.co.za
bonganin@marketphotoworkshop.co.za
Kieran.Nienaber@premierfoods.com
maxi@jian.co.za
nondumiso.matiwane@absa.co.za
tsakani@makolegroup.co.za
mutswako@gmail.com
salthiel.maybye@liberty.co.za
chemane@ymail.com
tosinoduyemi@gmail.com
bonolo@bluemoon.co.za
hayley@ledge.co.za
Pieter.Nel2@transnet.net '''
company = set()
for email in emails.split('\n'):
    company.add((email.split('@')[1]).split('.')[0])
company = list(company)
company.sort()
print '\n'.join(company)

