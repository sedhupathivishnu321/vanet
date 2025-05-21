import pandas as pd
import xml.etree.ElementTree as ET

# Load the dataset from CSV
df = pd.read_csv("dataset.csv")

# Create the root XML element
root = ET.Element("TrafficSimulationData")

# Loop through the rows of the dataframe to create XML elements
for _, row in df.iterrows():
    entry = ET.SubElement(root, "TrafficEntry")

    # Add each field as a subelement of the entry
    for column in df.columns:
        ET.SubElement(entry, column).text = str(row[column])

# Convert the XML tree to a string
tree = ET.ElementTree(root)
tree.write("traffic_simulation_data.xml", encoding="utf-8", xml_declaration=True)

# Output the first few lines of the XML file for preview
with open("traffic_simulation_data.xml", "r") as f:
    print(f.read(500))  # Preview the first 500 characters of the XML
