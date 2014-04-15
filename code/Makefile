szavazokor-lista:
	parallel wget -O ../raw/oevk-{1}-{2}.js http://valasztas.hu/dyn/pv14/map/oevk/M{1}/{2}/oevk.js ::: {01..20} ::: {01..99}
	find ../raw -size 0 -name "*.js" | xargs rm -f
	touch $@

terkep-lista.txt: szavazokor-lista
	python szavazokorok.py > terkep-lista.txt

terkepek: terkep-lista.txt
	wget -x -P ../raw/js -i terkep-lista.txt
	touch $@

../consistent/szavazokorok-szavazatokkal.geojson.gz: ../consistent/vote_counts_precincts.csv ../consistent/szavazokorok.geojson merge-csv-to-geojson.py
	python merge-csv-to-geojson.py > ../consistent/szavazokorok-szavazatokkal.geojson
	gzip ../consistent/szavazokorok-szavazatokkal.geojson
