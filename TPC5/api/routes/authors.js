var express = require('express');
var router = express.Router();
var axios = require('axios');
const { urlencoded } = require('express');

var prefixes = `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX noInferences: <http://www.ontotext.com/explicit>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX : <http://di.uminho.pt/prc2021/tpc5#>
`

var link = "http://epl.di.uminho.pt:8738/api/rdf4j/query/A84302-TPC5?query=" 
var link2 = "http://epl.di.uminho.pt:8738/api/rdf4j/update/A84302-TPC5?query=" 


/* GET home page. */
router.get('/', function(req, res, next) {
  var query = `SELECT * WHERE { ?s rdf:type :Autor. } `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
    res.status(200).jsonp(dados.data.results.bindings)
    })
    .catch(err => 
    res.status(500).jsonp(err)
    )
});

router.get('/:id', function(req, res, next) {
    var query = `SELECT * WHERE { :${req.params.id} ?p ?o. } `
  
    axios.get(link + encodeURIComponent(prefixes + query))
      .then(dados => {
        res.status(200).jsonp(dados.data.results.bindings)
      })
      .catch(err => 
        res.status(500).jsonp(err)
        )
  
  });

module.exports = router;
