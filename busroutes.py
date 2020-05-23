import numpy as np
import pandas as pd

routes = pd.read_csv("data/hktransit-all-routes.csv")
stops = pd.read_csv("data/hktransit-all-stops.csv")

def cart_to_gps_dist(cart_dist):
	"""Compute approx. lat/long dist equivalent to Cartesian dist (in km)."""
	deg_per_km = 0.00905711
	return cart_dist * deg_per_km

def nearby_stops(lat, lng, radius=1):
	"""
	Get list of IDs of stops within radius of (lat, lng).

	Keyword arguments:
	radius -- in km
	"""
	rad_filter = np.sqrt((stops["lat"] - lat)**2 + \
		(stops["lng"] - lng)**2) < cart_to_gps_dist(radius)
	
	return stops[rad_filter].reset_index()

if __name__ == "__main__":
	nearby = nearby_stops(22.218108, 114.212509, radius=0.2)
