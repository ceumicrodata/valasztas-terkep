import json
import unicodecsv

csv_file = unicodecsv.DictReader(open("../consistent/vote_counts_precincts.csv", "r"))
json_file = json.load(open("../consistent/szavazokorok.geojson"))

NUMERIC_FIELDS = ('szavazok','reszvetel','mcp','haza_nem_elado','sms','fkgp','udp','fidesz','sem','lmp','jesz','ump','munkaspart','szocdemek','kti','egyutt2014','zoldek','osszefogas','kormanyvaltok','jobbik','osszes_listas','egyeni_fidesz','egyeni_kormanyvaltok','egyeni_jobbik','egyeni_lmp')

class Searchable(object):
	# A hash table for fast left joins.
	def __init__(self, list, index_field):
		dct = {}
		for item in list:
			dct[item[index_field]] = item
		self.hash_table = dct

	def search(self, index_value):
		if index_value in self.hash_table:
			return self.hash_table[index_value]
		else:
			return None

def numeric_fields(dct):
	for key in dct.keys():
		if key in NUMERIC_FIELDS:
			if key=="reszvetel":
				dct[key] = float(dct[key])
			else:
				dct[key] = int(dct[key])
	return dct

if __name__ == '__main__':
	output_list = []
	geo_table = Searchable(list=json_file['features'], index_field='id')
	for item in csv_file:
		output = geo_table.search(item['id'])
		output['properties'].update(numeric_fields(item))
		output_list.append(output)
	print json.dumps(dict(features=output_list, type='FeatureCollection'))
