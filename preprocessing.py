import pandas as pd

import json
import os
import pdb

def write_company_routes_csv(json_file):
	"""Write csv representation of company routes json file."""
	with open(json_file) as f:
		json_routes = json.loads(f.read())["data"]

		df = pd.DataFrame(json_routes)
		df.to_csv(os.path.splitext(json_file)[0] + ".csv", index=False)

def write_hktransit_csv(json_file):
	"""
	Write csv representation of hktransit all routes/stops json file.
	Automatically detects whether input is stops or routes based on file name.
	"""
	with open(json_file) as f:
		if "routes" in json_file:
			json_routes = json.loads(f.read())["routes"]
		elif "stops" in json_file:
			json_routes = json.loads(f.read())["stops"]
		else:
			raise Exception("Cannot tell if file name is stops or routes")
		
		df = pd.DataFrame(json_routes)
		df.to_csv(os.path.splitext(json_file)[0] + ".csv", index=False)

def write_routes_per_stop(routes_csv, stops_csv):
	"""
	Write csv file of list of routes per stop.

	Arguments:
	routes_csv -- path to routes csv file
	stops_csv -- path to stops csv file
	"""
	routes_df = pd.read_csv(routes_csv)
	stops_df = pd.read_csv(stops_csv)

	routes_per_stop_df = stops_df["stopId"].copy()
	pdb.set_trace()
	
	for i, route in routes_df.iterrows():
		for path in route["paths"]:
			for stop in path:
				continue

def preprocess():
	write_company_routes_csv("data/citybus-routes.json")
	write_company_routes_csv("data/nwfb-routes.json")
	write_hktransit_csv("data/hktransit-all-routes.json")
	write_hktransit_csv("data/hktransit-all-stops.json")

	write_routes_per_stop("data/hktransit-all-routes.csv", \
		"data/hktransit-all-stops.csv")

if __name__ == "__main__":
	preprocess()
