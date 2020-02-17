const express = require('express');
const router = express.Router();

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'iot.abbindustrigymnasium.se',
  user     : 'grupptre',
  password : 'trampulingitarr',
  database : 'grupptre'
});
 
connection.connect(function(err){
    if (err){
        throw error;
    }
    else
        console.log("Working");
});

router.get('/', (req, res, next) => {
    
    connection.query('SELECT * FROM simon', function (error, results, fields) {
        if (error) throw error;
        res.status(200).json({
            message: 'Handling get request to /products',
            result: results});
        console.log('The solution is: ', results[0].name);
      });
});

router.post('/', (req, res, next) => {
    const product = {
        id: req.body.id,
        temp:req.body.temp,
        hum :req.body.hum
    };

    var createProducts = function(){
        return new Promise(function(resolve, reject){
            
            var theProduct = [product.id, product.temp, product.hum];
            console.log(theProduct);
            
            connection.query('INSERT INTO simon(Id,Tempratur,Fukt) VALUES ?', [[theProduct]], function (error, results) {
                if (error) 
                return reject(error);
                else
                return resolve(theProduct);
            });
        });
    }

createProducts().then(theProduct => {
    res.status(201).json ({
        message: "succses",
        product: theProduct
    });

}).catch(error => {
    res.status(500).json({
        error: error
    });
});    

});

router.get('/:productName',(req, res, next) => {
    const name = req.params.productName;

    var getProducts = function(){
        return new Promise(function(resolve, reject){
            
            connection.query('SELECT * FROM products Where Id = ?', [name], function (error, results) {
                if (error) 
                return reject(error);
                else
                return resolve(results);
              });
        });
    }

    getProducts().then(results => {
        if (results.length!=0){
            res.status(200).json (results);

        }
        else 
            
            res.status(404).json({
                message:"Error 404 no item found"
            });

    }).catch(error => {
        res.status(500).json({
            error: error
        });
    });    
});

router.patch('/:productName',(req, res, next) => {

    const product = {
        id: req.body.id,
        temp: req.body.temp,
        hum: req.body.hum
    };
    
    var updateProducts = function(){
        return new Promise(function(resolve, reject){
            
            connection.query('UPDATE `simon` SET `Tempratur`= ? AND `Fukt` = ? WHERE `Id` = ?', [product.temp, product.hum, product.id], function (error, results) {
                if (error) 
                return reject(error);
                else
                return resolve(results);
              });
        });
    }

    updateProducts().then(results => {

        res.status(200).json (results);
        if (results.affectedRows>0){
            res.status(200).json (results);

        }
        else 
            
            res.status(404).json({
                message:"Error 404 cant update"
            });

    }).catch(error => {
        res.status(500).json({
            error: error
        });
    });    
});

router.delete('/:productName',(req, res, next) => {
    const name = req.params.productName;
    
    var deleteProducts = function(){
        return new Promise(function(resolve, reject){
            
            connection.query('DELETE FROM simon Where Id = ?', [name], function (error, results) {
                if (error) 
                return reject(error);
                else
                return resolve(results);

              });
        });
    }

    deleteProducts().then(results => {
        if (results.length!=0){
            res.status(200).json (results);
        }
        else 
            res.status(404).json({
                message:"Error 404 no item found"
            });

    }).catch(error => {
        res.status(500).json({
            error: error
        });
    });    
});

module.exports = router;

/*
const express = require("express");
const router = express.Router();

var mysql = require("mysql");
var con = mysql.createConnection({
    host : "iot.abbindustrigymnasium.se",
    user : "grupptre",
    password : "trampulingitarr",
    database : "grupptre",
});

con.connect(function(error) {
    if (error) {throw error;}
    else console.log("Working");
});

router.get("/", (req, res) => {
//    con.query("SELECT * FROM simon", function (error, results) {
//        if (error) throw error;
//        res.status(200).json({message: "Getter", result: results});

console.log(req.body);
var getTempratur = function() {
    return new Promise(function(reject) {
        con.query("SELECT * FROM simon", function (error, results) {
            if(error){
                return reject(error);
            }else{
                return resolve(result);
            }
        });
    });
}

getTempratur().then(result => {
    if (result.length==0)
        res.status(404).json({message: "somthing went wrong"});
    else
        res.status(200).json(result);
})

.catch(error => {
    res.status(500).json({
        error: error
        });
    });
});

router.get("/:simonTempratur", (req, res) => {
    const Temp = req.params.simonTempratur;
    var getTempratur = function() {
        return new Promise(function(resolve, reject) {
            con.query("SELECT * FROM simon  WHERE `Tempratur` = ?", [Temp], function (err, result) {
                if(err){                
                    return reject(err);
                }else{              
                    return resolve(result);
                }
        });
    });
}

getTempratur().then(result => {
    if (result.length==0)
        res.status(404).json({message: "somthing went wrong"});
    else
        res.status(200).json(result);
})

.catch(error => {
    res.status(500).json({
        error: error
        });
    });
});

module.exports = router;
*/