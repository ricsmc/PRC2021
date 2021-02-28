import json
import rdflib 
from rdflib import Graph, Literal, RDF, URIRef, BNode
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
import os


with open('ucs.json') as f:
  data = json.load(f)

g = rdflib.Graph()
ds = rdflib.Dataset()
url = "http://di.uminho.pt/prc2021/ucs"
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
#################################################################
#    Object Properties
#################################################################


g.add((
  rdflib.URIRef(url+"#ensina"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#ensina"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#éEnsinadaPor")
))
g.add((
  rdflib.URIRef(url+"#ensina"),
  RDFS.domain,
  rdflib.URIRef(url+"#Professor")
))
g.add((
  rdflib.URIRef(url+"#ensina"),
  RDFS.range,
  rdflib.URIRef(url+"#UnidadeCurricular")
))
g.add((
  rdflib.URIRef(url+"#frequenta"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#frequenta"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#éFrequentadaPor")
))
g.add((
  rdflib.URIRef(url+"#frequenta"),
  RDFS.domain,
  rdflib.URIRef(url+"#Aluno")
))
g.add((
  rdflib.URIRef(url+"#frequenta"),
  RDFS.range,
  rdflib.URIRef(url+"#UnidadeCurricular")
))
g.add((
  rdflib.URIRef(url+"#éAlunoDe"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#éAlunoDe"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#éProfessorDe")
))
g.add((
  rdflib.URIRef(url+"#éEnsinadaPor"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#éFrequentadaPor"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#éProfessorDe"),
  RDF.type,
  OWL.ObjectProperty
))
first = BNode()
rest=BNode()
g.add((
  rest,
  RDF.first,
  rdflib.URIRef(url+"#éFrequentadaPor")
))
g.add((
  first,
  RDF.first,
  rdflib.URIRef(url+"#ensina")
))
g.add((
  first,
  RDF.rest,
  rest
))
g.add((
  rdflib.URIRef(url+"#éProfessorDe"),
  OWL.propertyChainAxiom,
  first
))


#################################################################
#    Data properties
#################################################################

g.add((
  rdflib.URIRef(url+"#anoLetivo"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#nome"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#descrição"),
  RDF.type,
  OWL.DatatypeProperty
))

#################################################################
#    Classes
#################################################################

g.add((
  rdflib.URIRef(url+"#Aluno"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Professor"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#UnidadeCurricular"),
  RDF.type,
  OWL.Class
))

#################################################################
#    Individuals
#################################################################



for i in data:



    #################################################################
    #    UC
    #################################################################
    g.add((
      rdflib.URIRef(url+"#" + i['codigo']),
      RDF.type,
      rdflib.URIRef(url+"#UnidadeCurricular")
    ))
    g.add((
      rdflib.URIRef(url+"#" + i['codigo']),
      RDF.type,
      OWL.NamedIndividual
    ))
    g.add((
      rdflib.URIRef(url+"#" + i['codigo']),
      URIRef(url + "#anoLetivo"),
      Literal(i["ano"])
    ))
    des = i['designacao'].encode('utf-8')
    
    g.add((
      rdflib.URIRef(url+"#" + i['codigo']),
      URIRef(url+"#designação"),
      Literal(des.decode())
    ))
    
    #################################################################
    #    Professores
    #################################################################

    k = i['professor']


    g.add((
      rdflib.URIRef(url + "#" + k['codigo']),
      RDF.type,
      rdflib.URIRef(url+"#Professor")
    ))
    g.add((
      rdflib.URIRef(url+"#" + k['codigo']),
      RDF.type,
      OWL.NamedIndividual
    ))
    g.add((
      rdflib.URIRef(url+"#" + k['codigo']),
      URIRef(url+"#nome"),
      Literal(k["nome"])
    ))
    g.add((
      rdflib.URIRef(url+"#" + k['codigo']),
      URIRef(url+"#ensina"),
      rdflib.URIRef(url+"#" + i['codigo'])
    ))


    #################################################################
    #    Alunos
    #################################################################

    for j in i["alunos"]:
      g.add((
        rdflib.URIRef(url+"#" + j['_id']),
        RDF.type,
        rdflib.URIRef(url+"#Aluno")
      ))
      g.add((
        rdflib.URIRef(url+"#" + j['_id']),
        RDF.type,
        OWL.NamedIndividual
      ))
      g.add((
        rdflib.URIRef(url+"#" + j['_id']),
        rdflib.term.URIRef(url+"#nome"),
        Literal(j["nome"])
      ))
      
      g.add((
        rdflib.URIRef(url+"#" + j['_id']),
        rdflib.term.URIRef(url+"#frequenta"),
        rdflib.URIRef(url+"#" + i['codigo'])
      ))

pr = g.serialize(format="turtle")
g.serialize(destination='output.ttl',format="turtle")
f.close()