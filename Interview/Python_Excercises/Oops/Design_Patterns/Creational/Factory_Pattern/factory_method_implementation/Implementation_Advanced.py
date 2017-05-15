Data comes in many forms. There are two main file categories for storing/retrieving data: human-readable files and binary files. Examples of human-readable files are XML, Atom, YAML, and JSON. Examples of binary files are the .sq3 file format used by SQLite and the .mp3 file format used to listen to music.

In this example, we will focus on two popular human-readable formats: XML and JSON. Although human-readable files are generally slower to parse than binary files, they make data exchange, inspection, and modification much easier. For this reason, it is advised to prefer working with human-readable files, unless there are other restrictions that do not allow it (mainly unacceptable performance and proprietary binary formats).

In this problem, we have some input data stored in an XML and a JSON file, and we want to parse them and retrieve some information. At the same time, we want to centralize the client's connection to those (and all future) external services. We will use the Factory Method to solve this problem. The example focuses only on XML and JSON, but adding support for more services should be straightforward.

First, let's take a look at the data files. The XML file, person.xml, is based on the Wikipedia example [j.mp/wikijson] and contains information about individuals (firstName, lastName, gender, and so on) as follows:

Copy
<persons>
  <person>
    <firstName>John</firstName>
    <lastName>Smith</lastName>
    <age>25</age>
    <address>
      <streetAddress>21 2nd Street</streetAddress>
      <city>New York</city>
      <state>NY</state>
      <postalCode>10021</postalCode>
    </address>
    <phoneNumbers>
      <phoneNumber type="home">212 555-1234</phoneNumber>
      <phoneNumber type="fax">646 555-4567</phoneNumber>
    </phoneNumbers>
    <gender>
      <type>male</type>
    </gender>
  </person>
  <person>
    <firstName>Jimy</firstName>
    <lastName>Liar</lastName>
    <age>19</age>
    <address>
      <streetAddress>18 2nd Street</streetAddress>
      <city>New York</city>
      <state>NY</state>
      <postalCode>10021</postalCode>
    </address>
    <phoneNumbers>
      <phoneNumber type="home">212 555-1234</phoneNumber>
    </phoneNumbers>
    <gender>
      <type>male</type>
    </gender>
  </person>
  <person>
    <firstName>Patty</firstName>
    <lastName>Liar</lastName>
    <age>20</age>
    <address>
      <streetAddress>18 2nd Street</streetAddress>
      <city>New York</city>
      <state>NY</state>
      <postalCode>10021</postalCode>
    </address>
    <phoneNumbers>
      <phoneNumber type="home">212 555-1234</phoneNumber>
      <phoneNumber type="mobile">001 452-8819</phoneNumber>
    </phoneNumbers>
    <gender>
      <type>female</type>
    </gender>
  </person>
</persons>
The JSON file, donut.json, comes from the GitHub account of Adobe [j.mp/adobejson] and contains donut information (type, price/unit that is, ppu, topping, and so on) as follows:

Copy
[
  {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
      "batter": [
        { "id": "1001", "type": "Regular" },
        { "id": "1002", "type": "Chocolate" },
        { "id": "1003", "type": "Blueberry" },
        { "id": "1004", "type": "Devil's Food" }
      ]
    },
    "topping": [
      { "id": "5001", "type": "None" },
      { "id": "5002", "type": "Glazed" },
      { "id": "5005", "type": "Sugar" },
      { "id": "5007", "type": "Powdered Sugar" },
      { "id": "5006", "type": "Chocolate with Sprinkles" },
      { "id": "5003", "type": "Chocolate" },
      { "id": "5004", "type": "Maple" }
    ]
  },
  {
    "id": "0002",
    "type": "donut",
    "name": "Raised",
    "ppu": 0.55,
    "batters": {
      "batter": [
        { "id": "1001", "type": "Regular" }
      ]
    },
    "topping": [
      { "id": "5001", "type": "None" },
      { "id": "5002", "type": "Glazed" },
      { "id": "5005", "type": "Sugar" },
      { "id": "5003", "type": "Chocolate" },
      { "id": "5004", "type": "Maple" }
    ]
  },
  {
    "id": "0003",
    "type": "donut",
    "name": "Old Fashioned",
    "ppu": 0.55,
    "batters": {
      "batter": [
        { "id": "1001", "type": "Regular" },
        { "id": "1002", "type": "Chocolate" }
      ]
    },
    "topping": [
      { "id": "5001", "type": "None" },
      { "id": "5002", "type": "Glazed" },
      { "id": "5003", "type": "Chocolate" },
      { "id": "5004", "type": "Maple" }
    ]
  }
]
We will use two libraries that are part of the Python distribution for working with XML and JSON: xml.etree.ElementTree and json as follows:

Copy
import xml.etree.ElementTree as etree
import json
The JSONConnector class parses the JSON file and has a parsed_data() method that returns all data as a dictionary (dict). The property decorator is used to make parsed_data() appear as a normal variable instead of a method as follows:

Copy
class JSONConnector:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data
The XMLConnector class parses the XML file and has a parsed_data() method that returns all data as a list of xml.etree.Element as follows:

Copy
class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
The connection_factory() function is a Factory Method. It returns an instance of JSONConnector or XMLConnector depending on the extension of the input file path as follows:

Copy
def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)
The connect_to() function is a wrapper of connection_factory(). It adds exception handling as follows:

Copy
def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory
The main() function demonstrates how the Factory Method design pattern can be used. The first part makes sure that exception handling is effective as follows:

Copy
def main():
    sqlite_factory = connect_to('data/person.sq3')