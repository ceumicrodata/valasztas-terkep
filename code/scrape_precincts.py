from urllib.request import urlopen
import os, csv, re

os.chdir('/Users/laszlosandor/Documents/githubcode/valasztas-terkep/consistent/')

header = ('id','atjelentkezettek','oevk','szavazokor','szavazok','reszvetel','mcp','haza_nem_elado','sms','fkgp','udp','fidesz','sem','lmp','jesz','ump','munkaspart','szocdemek','kti','egyutt2014','zoldek','osszefogas','kormanyvaltok','jobbik','osszes_listas','egyeni_fidesz','egyeni_kormanyvaltok','egyeni_jobbik','egyeni_lmp')

fin = open('/Users/laszlosandor/Documents/githubcode/valasztas-terkep/code/szavazokorok_results.txt','r')

fout = open('vote_counts_precincts.csv','w')
writer = csv.writer(fout)
writer.writerow(header)

for rowin in fin:
    html = urlopen(rowin).read().decode('latin2')
    m1 = re.search('M\d{2}/T\d{3}/', rowin)
    m2 = re.search('\d{3}(?=\.)', rowin)
    id = m1.group(0)+m2.group(0)
    atjelentkezettek = re.search('megszámlálására',html)!=None
    oevk = re.search('.*(?=\.számú szavazókör)',html).group(0)
    szavazokor = re.search('[A-Z].*(?=\.számú egyéni választókerületi szavazás)',html).group(0)
    szavazok = re.search('(?<=<td>&nbsp;).*?(?=&nbsp;<br>[\d\.]* %)',html).group(0)
    reszvetel = re.search('[\d\.]*(?= %)',html).group(0)
    egyeni_fidesz = re.search('(?<=d>FIDESZ-KDNP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    egyeni_kormanyvaltok = re.search('(?<=d>MSZP-EGYÜTT-DK-PM-MLP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    egyeni_jobbik = re.search('(?<=d>JOBBIK</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    egyeni_lmp = re.search('(?<=d>LMP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    mcp = re.search('(?<=">MCP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    haza_nem_elado = re.search('(?<=">A HAZA NEM ELADÓ MOZGALOM PÁRT</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    sms = re.search('(?<=">SERES MÁRIA SZÖVETSÉGESEI</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    fkgp = re.search('(?<=">FÜGGETLEN KISGAZDAPÁRT</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    udp = re.search('(?<=">ÚDP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    fidesz = re.search('(?<=">FIDESZ-KDNP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    sem = re.search('(?<=">SEM</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    lmp = re.search('(?<=">LMP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    jesz = re.search('(?<=">JESZ</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    ump = re.search('(?<=">ÚMP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    munkaspart = re.search('(?<=">MUNKÁSPÁRT</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    szocdemek = re.search('(?<=">SZOCIÁLDEMOKRATÁK</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    kti = re.search('(?<=">KTI</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    egyutt2014 = re.search('(?<=">EGYÜTT 2014</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    zoldek = re.search('(?<=">ZÖLDEK PÁRTJA</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    osszefogas = re.search('(?<=">ÖSSZEFOGÁS</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    kormanyvaltok = re.search('(?<=">MSZP-EGYÜTT-DK-PM-MLP</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    jobbik = re.search('(?<=">JOBBIK</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    osszes_listas = re.search('(?<=összesen:</td>\s{3}<td style="text-align:right;">&nbsp;).*?(?=&nbsp;<)',html).group(0)
    rowout = id,atjelentkezettek,oevk,szavazokor,szavazok, reszvetel,mcp,haza_nem_elado,sms,fkgp,udp,fidesz,sem,lmp,jesz,ump,munkaspart,szocdemek,kti,egyutt2014,zoldek,osszefogas,kormanyvaltok,jobbik,osszes_listas,egyeni_fidesz,egyeni_kormanyvaltok,egyeni_jobbik,egyeni_lmp
    writer.writerow(rowout)
