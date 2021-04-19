import rdflib 
from rdflib import Graph, Literal, RDF, URIRef, BNode
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
import os

import csv

g = rdflib.Graph()
url = "http://di.uminho.pt/prc2021/avaliacao1"
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
#################################################################
#    Object Properties
#################################################################

g.add((
  rdflib.URIRef(url+"#receita_de"),
  RDF.type,
  OWL.ObjectProperty
))

g.add((
  rdflib.URIRef(url+"#propriedade_de"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#propriedade_de"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#dono_de")
))
g.add((
  rdflib.URIRef(url+"#foi_pago_por"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#foi_pago_por"),
  OWL.inverseOf,
  rdflib.URIRef(url+"#pagou")
))
g.add((
  rdflib.URIRef(url+"#dono_de"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#pagou"),
  RDF.type,
  OWL.ObjectProperty
))
g.add((
  rdflib.URIRef(url+"#não_pagou"),
  RDF.type,
  OWL.ObjectProperty
))

#################################################################
#    Data properties
#################################################################

g.add((
  rdflib.URIRef(url+"#permilagem"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#valor"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#data"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#descrição"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#mensalidade"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#telefone"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#email"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#nome"),
  RDF.type,
  OWL.DatatypeProperty
))
g.add((
  rdflib.URIRef(url+"#entidade"),
  RDF.type,
  OWL.DatatypeProperty
))
#################################################################
#    Classes
#################################################################


g.add((
  rdflib.URIRef(url+"#Pagamentos"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Jan"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Jan"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Fev"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Fev"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Mar"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Mar"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Abr"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Abr"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Mai"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Mai"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Jun"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Jun"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Jul"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Jul"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Ago"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Ago"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Sete"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Sete"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Out"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Out"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Nov"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Nov"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))
g.add((
  rdflib.URIRef(url+"#Dez"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Dez"),
  RDFS.subClassOf,
  rdflib.URIRef(url+"#Pagamentos")
))

g.add((
  rdflib.URIRef(url+"#Despesa"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Receita"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Fração"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Fração"),
  RDF.type,
  OWL.Class
))  

g.add((
  rdflib.URIRef(url+"#Proprietário"),
  RDF.type,
  OWL.Class
))
g.add((
  rdflib.URIRef(url+"#Condomínio"),
  RDF.type,
  OWL.Class
))

with open('fracao.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader: 
        g.add((
        rdflib.URIRef(url+"#" + row[0]),
        RDF.type,
        rdflib.URIRef(url+"#Fração")
        ))
        g.add((
        rdflib.URIRef(url+"#" + row[0]),
        RDF.type,
        OWL.NamedIndividual
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#descrição"),
            Literal(row[1])
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#permilagem"),
            Literal(row[2])
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#mensalidade"),
            Literal(row[3], datatype=XSD.integer)
        ))

with open('receitas-despesas.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile) 
    for row in spamreader:
        g.add((
        rdflib.URIRef(url+"#" + row[0]),
        RDF.type,
        rdflib.URIRef(url+"#" + row[1])
        ))
        g.add((
        rdflib.URIRef(url+"#" + row[0]),
        RDF.type,
        OWL.NamedIndividual
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#data"),
            Literal(row[2])
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#valor"),
            Literal(row[3], datatype=XSD.integer)
        ))
        g.add((
            rdflib.URIRef(url+"#" + row[0]),
            URIRef(url + "#descrição"),
            Literal(row[5])
        ))
        if(row[1] == "Receita"):
            g.add((
                rdflib.URIRef(url+"#" + row[0]),
                URIRef(url + "#receita_de"),
                rdflib.URIRef(url+"#" + row[4])
            ))
        else:
            g.add((
                rdflib.URIRef(url+"#" + row[0]),
                URIRef(url + "#entidade"),
                Literal(row[4])
            ))


with open('mapa-pagamentos.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile) 
    list_row = []
    for row in spamreader:
        list_row.extend(row)
        break
    for row in spamreader:
        
        i = 0
        print
        for month in row:
            if(month == '1'):
                g.add((
                    rdflib.URIRef(url+"#" + row[0]),
                    URIRef(url + "#pagou"),
                    rdflib.URIRef(url+"#" + list_row[i])
                ))
            elif(list_row[i] != 'Fração'):
                g.add((
                    rdflib.URIRef(url+"#" + row[0]),
                    URIRef(url + "#não_pagou"),
                    rdflib.URIRef(url+"#" + list_row[i])
                ))
            i += 1





pr = g.serialize(format="turtle")
g.serialize(destination='output.ttl',format="turtle")