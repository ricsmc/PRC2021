var express = require('express');
var router = express.Router();
var axios = require('axios');

var prefixes = `
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://ontotext.com/explicit>
    PREFIX skos: <htpp://www.w3.org/2004/02/skos/core#>
    `


/* GET home page. */
router.get('/' || '/reps', function(req, res, next) {
  axios.get('http://localhost:7200/rest/repositories')
    .then(data => res.render('index', { reps: data.data }))
    .catch(err => res.render('error', {message:'erro', error:err}))
  
});


router.get('/reps/:id' , function(req, res, next){
  var query = `SELECT * WHERE { ?s rdf:type owl:Class}`
  var encoded = encodeURIComponent(prefixes  + query)
  console.log('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
  axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
    .then(data => res.render ('rep', {rep:data.data.results.bindings, id:req.params.id}))
    .catch(err => res.render('error', {message:'erro', error:err}))
  
})

router.get('/reps/:id/:class' , function(req, res, next){
  var query = `SELECT * WHERE { ?s rdf:type owl:Class}`
  var encoded = encodeURIComponent(prefixes  + query)
  console.log('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
  axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
    .then(data => {
      query = `select * where { 
        ?s a <` + data.data.results.bindings[parseInt(req.params.class)].s.value +`>
      }`
      encoded = encodeURIComponent(prefixes  + query)
      axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
        .then(da => res.render ('class', {cla: req.params.class, ide:req.params.id ,rep:da.data.results.bindings, id:data.data.results.bindings[parseInt(req.params.class)].s.value.split('#')[1]}))
        .catch(e => res.render('error', {message:'erro', error:e}))
    })
    .catch(err => res.render('error', {message:'erro', error:err}))
  
})

router.get('/reps/:id/:class/:ind' , function(req, res, next){
  var query = `SELECT * WHERE { ?s rdf:type owl:Class}`
  var encoded = encodeURIComponent(prefixes  + query)
  console.log('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
  axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
    .then(data => {
      query = `select * where { 
        ?s a <` + data.data.results.bindings[parseInt(req.params.class)].s.value +`>
      }`
      encoded = encodeURIComponent(prefixes  + query)
      axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
        .then(da => {
          query = `select * where { 
            <` + da.data.results.bindings[parseInt(req.params.ind)].s.value +`> ?a ?p.
          }`
          encoded = encodeURIComponent(prefixes  + query)
          axios.get('http://localhost:7200/repositories/' + req.params.id + "?query=" + encoded)
            .then(d => res.render ('ind', {rep:d.data.results.bindings, id:da.data.results.bindings[parseInt(req.params.ind)].s.value.split('#')[1]}))
            .catch(er => res.render('error', {message:'erro', error:er}))
        })
        .catch(e => res.render('error', {message:'erro', error:e}))
    })
    .catch(err => res.render('error', {message:'erro', error:err}))
  
})

module.exports = router;
