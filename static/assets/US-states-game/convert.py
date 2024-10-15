import pandas as pd

# Define canvas size
canvas_width = 500
canvas_height = 450

# Real coordinates for each state
state_coordinates = {
    "Alabama": (32.806, -86.791),
    "Alaska": (61.370, -152.404),
    "Arizona": (33.729, -111.431),
    "Arkansas": (34.969, -92.373),
    "California": (36.116, -119.681),
    "Colorado": (39.059, -105.311),
    "Connecticut": (41.597, -72.755),
    "Delaware": (39.349, -75.514),
    "Florida": (27.766, -81.686),
    "Georgia": (33.040, -83.643),
    "Hawaii": (21.094, -157.498),
    "Idaho": (44.240, -114.478),
    "Illinois": (40.349, -88.986),
    "Indiana": (39.849, -86.258),
    "Iowa": (42.011, -93.210),
    "Kansas": (39.011, -98.484),
    "Kentucky": (37.668, -84.670),
    "Louisiana": (31.169, -91.867),
    "Maine": (44.693, -69.381),
    "Maryland": (39.063, -76.802),
    "Massachusetts": (42.230, -71.531),
    "Michigan": (43.326, -84.536),
    "Minnesota": (45.368, -93.900),
    "Mississippi": (32.741, -89.678),
    "Missouri": (38.456, -92.288),
    "Montana": (47.02458049677925, -109.5063266461478),
    "Nebraska": (41.492, -99.901),
    "Nevada": (38.505, -117.055),
    "New Hampshire": (43.193, -71.572),
    "New Jersey": (40.298, -74.521),
    "New Mexico": (34.840, -106.248),
    "New York": (42.165, -74.948),
    "North Carolina": (35.630, -79.806),
    "North Dakota": (47.528, -99.784),
    "Ohio": (40.388, -82.764),
    "Oklahoma": (35.565, -96.928),
    "Oregon": (43.933, -120.558),
    "Pennsylvania": (40.590, -77.209),
    "Rhode Island": (41.680, -71.510),
    "South Carolina": (33.856, -80.945),
    "South Dakota": (44.299, -99.438),
    "Tennessee": (35.747, -86.692),
    "Texas": (31.394584400587494, -98.82145967573905),
    "Utah": (40.150, -111.862),
    "Vermont": (44.045, -72.710),
    "Virginia": (37.769, -78.169),
    "Washington": (47.400, -121.490),
    "West Virginia": (38.491, -80.954),
    "Wisconsin": (43.784, -88.787),
    "Wyoming": (43.075, -107.290),
}

# Normalize coordinates to the canvas size
min_latitude = min(lat for lat, lon in state_coordinates.values())
max_latitude = max(lat for lat, lon in state_coordinates.values())
min_longitude = min(lon for lat, lon in state_coordinates.values())
max_longitude = max(lon for lat, lon in state_coordinates.values())

normalized_coordinates = {}

for state, (latitude, longitude) in state_coordinates.items():
    # Normalize latitude and longitude to canvas coordinates
    x = (longitude - min_longitude) / (max_longitude - min_longitude) * canvas_width
    y = (latitude - min_latitude) / (max_latitude - min_latitude) * canvas_height
    normalized_coordinates[state] = (int(x), int(canvas_height - y))  # Invert y-axis for proper display

# Convert to DataFrame and save to CSV
df = pd.DataFrame.from_dict(normalized_coordinates, orient='index', columns=['x', 'y']).reset_index()
df.rename(columns={'index': 'state'}, inplace=True)

# Save to CSV
df.to_csv('50_states_normalized.csv', index=False)
print("Normalized coordinates saved to 50_states_normalized.csv")