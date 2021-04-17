import rdflib 
from rdflib import Graph, Literal, RDF, URIRef, BNode
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
import os


import xml.etree.ElementTree as ET
tree = ET.parse('jcrpubs.xml')
root = tree.getroot()

tags = []

g = rdflib.Graph()
url = "http://di.uminho.pt/prc2021/tpc5"
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
#################################################################
#    Object Properties
#################################################################


g.add((
  rdflib.URIRef(url+"#autor_de"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#autor_de"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#escrito_por")
))
g.add((
  rdflib.URIRef(url+"#autor_de"),
  RDFS.domain,
  rdflib.URIRef(url+"#Autor")
))
g.add((
  rdflib.URIRef(url+"#autor_de"),
  RDFS.range,
  rdflib.URIRef(url+"#Livro")
))

g.add((
  rdflib.URIRef(url+"#editor_de"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#editor_de"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#editado_por")
))
g.add((
  rdflib.URIRef(url+"#editor_de"),
  RDFS.domain,
  rdflib.URIRef(url+"#Autor")
))
g.add((
  rdflib.URIRef(url+"#editor_de"),
  RDFS.range,
  rdflib.URIRef(url+"#Livro")
))

g.add((
  rdflib.URIRef(url+"#escrito_por"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#editado_por"),
  RDF.type,
  OWL.ObjectProperty
))

#################################################################
#    Data properties
#################################################################
g.add((
  rdflib.URIRef(url+"#type"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#pdf_url"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#uri"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#volume"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#school"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#number"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#howpublished"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#issn"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#journal"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#isbn"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#publisher"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#pages"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#chapter"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#month"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#doi"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#year"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#booktitle"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#nome"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#title"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#address"),
  RDF.type,
  OWL.DatatypeProperty
))


#################################################################
#    Classes
#################################################################

g.add((
  rdflib.URIRef(url+"#Autor"),
  RDF.type,
  OWL.Class
))

g.add((
  rdflib.URIRef(url+"#Livro"),
  RDF.type,
  OWL.Class
))

#################################################################
#    Individuals
#################################################################

for child in root:
    g.add((
      rdflib.URIRef(url+"#" + child.attrib['id']),
      RDF.type,
      rdflib.URIRef(url+"#Livro")
    ))
    g.add((
      rdflib.URIRef(url+"#" + child.attrib['id']),
      RDF.type,
      OWL.NamedIndividual
    ))
    g.add((
        rdflib.URIRef(url+"#" + child.attrib['id']),
        URIRef(url + "#type"),
        Literal(child.tag)
    ))
    for ch in child:
        if (ch.tag == 'author' or ch.tag == 'author-ref'):
            if (ch.tag == 'author'):
                author_id = ch.attrib['id']
            else:
                author_id = ch.attrib['authorid']
            g.add((
                rdflib.URIRef(url+"#" + author_id),
                RDF.type,
                rdflib.URIRef(url+"#Autor")
            ))
            g.add((
                rdflib.URIRef(url+"#" + author_id),
                RDF.type,
                OWL.NamedIndividual
            ))
            g.add((
                rdflib.URIRef(url+"#" + author_id),
                URIRef(url+"#autor_de"),
                rdflib.URIRef(url+"#" + child.attrib['id'])
            ))
            if (ch.text):
                g.add((
                    rdflib.URIRef(url+"#" + author_id),
                    URIRef(url+"#nome"),
                    Literal(ch.text)
                ))
        elif (ch.tag == 'editor' or ch.tag == 'editor-ref'):
            if (ch.tag == 'editor'):
                editor_id = ch.attrib['id']
            else:
                editor_id = ch.attrib['authorid']
            g.add((
                rdflib.URIRef(url+"#" + editor_id),
                RDF.type,
                rdflib.URIRef(url+"#Autor")
            ))
            g.add((
                rdflib.URIRef(url+"#" + editor_id),
                RDF.type,
                OWL.NamedIndividual
            ))
            g.add((
                rdflib.URIRef(url+"#" + editor_id),
                URIRef(url+"#editor_de"),
                rdflib.URIRef(url+"#" + child.attrib['id'])
            ))
            if (ch.text):
                g.add((
                    rdflib.URIRef(url+"#" + editor_id),
                    URIRef(url+"#nome"),
                    Literal(ch.text)
                ))
        
        elif(ch.tag == 'deliverables'):
            g.add((
                rdflib.URIRef(url+"#" + child.attrib['id']),
                URIRef(url + "#pdf_url"),
                Literal(ch[0].attrib['url'])
            ))
        else:
            g.add((
                rdflib.URIRef(url+"#" + child.attrib['id']),
                URIRef(url + "#" + ch.tag),
                Literal(ch.text)
            ))

pr = g.serialize(format="turtle")
g.serialize(destination='output.ttl',format="turtle")
