import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Function to convert JSON array to XML
def json_to_xml(json_array):
    # Create the root element for the XML
    root = ET.Element('data')

    # Iterate through each item in the JSON array
    for item in json_array:
        # Create a new XML element for each item
        element = ET.SubElement(root, 'item')

        # Iterate through the key-value pairs in the JSON item
        for key, value in item.items():
            # Create sub-elements in the XML for each key-value pair
            sub_element = ET.SubElement(element, key)
            sub_element.text = str(value)  # Set the text content for the XML sub-element

    # Convert the XML tree to a string with UTF-8 encoding
    xml_string = ET.tostring(root, encoding='utf-8')

    # Parse the XML string and format it for pretty printing
    parsed_xml = minidom.parseString(xml_string)
    pretty_xml = parsed_xml.toprettyxml(indent='  ')

    return pretty_xml

# Example JSON array
json_array = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Convert JSON array to XML
xml_output = json_to_xml(json_array)

# Print the generated XML
print(xml_output)
