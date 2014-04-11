from geojson import Feature, Polygon, FeatureCollection
import json
import re
import glob

regex = re.compile("M(?P<megye>\d{2})/(?P<oevk>\d{2})/T(?P<telepules>\d{3})/(?P<szavazokor>\d{3})\.js")
whitespace = re.compile("")

def minify(text):
	output = ",".join(text.split(", "))
	return ":".join(output.split(": "))

def js_to_object(text):
	return json.loads(text.split("=")[1])

def filename_to_meta(filename="http://valasztas.hu/dyn/pv14/map/oevk/M01/01/T001/011.js"):
	meta = regex.search(filename).groupdict()
	meta["id"] = filename.split("oevk/")[1].split(".")[0]
	return meta

def object_to_feature(object, id, meta):
	points = [(float(item["lat"][0:7]), float(item["lng"][0:7])) for item in object["items"]]
	return Feature(geometry=Polygon([points]), id=id, properties=meta)

def filename_to_feature(filename):
	meta = filename_to_meta(filename)
	js = open(filename,"r").read()
	return object_to_feature(js_to_object(js), meta["id"], meta)

if __name__ == '__main__':
	collection = []
	for filename in glob.glob("../raw/js/valasztas.hu/dyn/pv14/map/oevk/M??/??/T???/???.js"):
		collection.append(filename_to_feature(filename))
	print minify(str(FeatureCollection(collection)))
