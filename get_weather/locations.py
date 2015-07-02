import easy_ui
import xml.etree.cElementTree as ET
import os

class ApiKeys:
    def __init__(self):
        if not os.path.exists("apikeys.xml"):
            root = ET.Element("root")
            tree = ET.ElementTree(root)
            tree.write("apikeys.xml")
        self.tree = ET.parse('apiKeys.xml')
        self.root = self.tree.getroot()
    
    def list(self):
        """
        Returns the apiKey object if it exists, otherwise returns None.
        """
        cur = []
        for i in self.root:
            cur.append(i)
        return cur
    
    def add(self, name, key):
        attrib={
            "name": name,
            "key": key,
        }
        ET.SubElement(self.root, "apikey", attrib)
    
    def modify(self, name, key):
        attrib={
            "name": name,
            "key": key,
        }
        for i in self.root:
            if i.get("name") == name:
                i.set("key", key)
    
    def remove(self, alias):
        for i in self.root:
            if i.get('name') == alias:
                self.root.remove(i)
                return True
        return False
    
    def close(self):
        self.tree.write("apikeys.xml")
    
    def __del__(self):
        self.close()


def addKey(name, key):
    d=ApiKeys()
    e=d.list()
    d.add(name, key)
    if len(e) < len(d.list()):
        print "success!"
        return
    print "failure"

def removeKey(name):
    d = ApiKeys()
    e=d.list()
    d.remove(name)
    if len(e) > len(d.list()):
        print "Success!"
        return
    print "failure."

def listKeys():
    print "\n".join([i.get('name') for i in ApiKeys().list()]) #this code ain't supposed to be readable man. It joins the names of the keys with \n

def modifyKey(name, key):
    d=ApiKeys()
    d.modify(name, key)

if __name__ == '__main__':
    ui={
        "add api key" : (
            addKey,
            (str, "the name"),
            (str, "the api key"),
        ),
        "remove key" : (
            removeKey,
            (str, "the name of the key"),
        ),
        "list keys" : (
            listKeys,
        ),
        "modify key" : (
            modifyKey,
            (str, "Name"),
            (str, "New api key"),
        ),
    }
    easy_ui.Ui(ui)