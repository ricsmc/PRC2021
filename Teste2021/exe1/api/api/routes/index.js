var express = require('express');
var router = express.Router();
var axios = require('axios');

var prefixes = `
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX noInferences: <http://www.ontotext.com/explicit>
  PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
  PREFIX p: <http://di.uminho.pt/prc2021/teste#>
    `
/* GET home page. */
router.get('/api/emd', function(req, res, next) {
  var query = `
  select * where { 
    ?atleta rdf:type p:Atleta.
    ?atleta p:apelido ?nome.
    ?atleta p:exame_feito_em ?id.
    ?id p:dataEMD ?data. 
    ?id p:resultado ?resultado.}
  `

  if (req.query.res == 'OK') {
    query = `
    select * where { 
      ?emd rdf:type :EMD.
      ?emd :resultado true
  }`
  }
  var encoded = encodeURIComponent(prefixes  + query)
  console.log(encoded)
  axios.get('http://localhost:7200/repositories/EMD' + "?query=" + encoded)
    .then(data => res.status(200).jsonp(data.results))
    .catch(err => { res.status(500).jsonp(err)
                  console.log(err)})
  

});

router.get('/api/emd/:id', function(req, res, next) {
  var query = `
  select * where { 
    p:` + req.params.id + ` :resultado ?resultado.
	  p:` + req.params.id + ` :dataEMD ?dataEMD.
}
  `
  var encoded = encodeURIComponent(prefixes  + query)
  console.log(encoded)
  axios.get('http://localhost:7200/repositories/EMD' + "?query=" + encoded)
    .then(data => res.status(200).jsonp(data.results.bindings))
    .catch(err => { res.status(500).jsonp(err)
                  console.log(err)})
  

});

router.get('/api/modalidades', function(req, res, next) {
  var query = `
  select * where { 
    ?modal rdf:type p:Modalidade.
}
  `
  var encoded = encodeURIComponent(prefixes  + query)
  console.log(encoded)
  axios.get('http://localhost:7200/repositories/EMD' + "?query=" + encoded)
    .then(data => res.status(200).jsonp(data.results.bindings))
    .catch(err => { res.status(500).jsonp(err)
                  console.log(err)})
  

});

router.get('/api/modalidades/:id', function(req, res, next) {
  var query = `
  select * where { 
    ?`+ req.params.id +` p:emd_com_modalidade ?modal.
}
  `
  var encoded = encodeURIComponent(prefixes  + query)
  console.log(encoded)
  axios.get('http://localhost:7200/repositories/EMD' + "?query=" + encoded)
    .then(data => res.status(200).jsonp(data.results.bindings))
    .catch(err => { res.status(500).jsonp(err)
                  console.log(err)})
  

});


router.get('/api/atletas', function(req, res, next) {
  var query ;

  if (req.query.gen) {
    
    query = `
    select * where { 
      ?atl rdf:type p:Atleta.
      ?atl p:género `+ req.query.gen + `.
  } ORDER BY ASC(?atl)
  `
  }

  if(req.query.clube){
    query = `
    select ?atl where { 
      ?atl rdf:type p:Atleta.
      ?atl p:inscrito_no_clube ?clube.
      ?clube p:nome_clube `+ req.query.clube +`.
  } ORDER BY ASC(?atl)
  `
  }
  
  var encoded = encodeURIComponent(prefixes  + query)
  console.log(encoded)
  axios.get('http://localhost:7200/repositories/EMD' + "?query=" + encoded)
    .then(data => res.status(200).jsonp(data.results.bindings))
    .catch(err => { res.status(500).jsonp(err)
                  console.log(err)})
  

});

module.exports = router;
