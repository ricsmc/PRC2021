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
    PREFIX el: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
`

var link = "http://localhost:7200/repositories/prc2021-tpc4" + "?query=" 

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/elements' , function(req,res){ 
  var query = `SELECT * WHERE { ?s ?p el:Element. } `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      
      var el = dados.data.results.bindings.map(bind => bind.s.value.split('#')[1] )
      res.render('els', {elems: el})
    
    })
    .catch(err => console.log(err))

})

router.get('/elements/:el' , function(req,res){ 
  var query = `SELECT * WHERE { el:` + req.params.el +` ?p ?o. } `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      console.log(dados.data.results.bindings)
      var el = dados.data.results.bindings.map(bind => {return({
        p:bind.p.value.split('#')[1],
        o: (bind.o.type == 'literal') ? bind.o.value : bind.o.value.split('#')[1]
      })
                                                 })
      res.render('el', {elems: el})
    
    })
    .catch(err => console.log(err))

})


router.get('/groups' , function(req,res){ 
  var query = `SELECT * WHERE { ?s ?p el:Group. }  `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      
      var el = dados.data.results.bindings.map(bind => bind.s.value.split('#')[1] )
      res.render('grupos', {elems: el})
    
    })
    .catch(err => console.log(err))

})

router.get('/groups/:g' , function(req,res){ 
  var query = `SELECT * WHERE { el:` + req.params.g +` ?p ?o }  `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      
      var el = dados.data.results.bindings.map(bind => {return({
        p:bind.p.value.split('#')[1],
        o: (bind.o.type == 'literal') ? bind.o.value : bind.o.value.split('#')[1]
      })})
      res.render('grupo', {elems: el})
    
    })
    .catch(err => console.log(err))

})



router.get('/periods' , function(req,res){ 
  var query = `SELECT * WHERE { ?s ?p el:Period. } `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      
      var el = dados.data.results.bindings.map(bind => bind.s.value.split('#')[1] )
      res.render('per', {elems: el})
    
    })
    .catch(err => console.log(err))

})

router.get('/periods/:p' , function(req,res){ 
  var query = `SELECT * WHERE { el:` + req.params.p +` ?p ?o } `

  axios.get(link + encodeURIComponent(prefixes + query))
    .then(dados => {
      
      var el = dados.data.results.bindings.map(bind => {return({
        p:bind.p.value.split('#')[1],
        o: (bind.o.type == 'literal') ? bind.o.value : bind.o.value.split('#')[1]
      })})
      res.render('peri', {elems: el})
    
    })
    .catch(err => console.log(err))

})

module.exports = router;
