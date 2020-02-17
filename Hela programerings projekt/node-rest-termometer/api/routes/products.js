const express = require("express");
const router = express.Router();

var mysql = require("mysql");
var connection = mysql.createConnection({
    host : "iot.abbindustrigymnasium.se",
    user : "grupptre",
    password : "trampulingitarr",
    database : "grupptre"
});

connection.connect(function(error) {
    if (error){
        throw error;
    }
    else
    console.log("Thats all there is to it");
});

router.get("/", (req, res, next) => {
    connection.query("SELECT * FROM simon", function (error, results, fields) {
        if (error) throw error;
        res.status(200).json({
            message: "Getter",
            result: results});
        console.log("The solution is: ", results[0].name);
    });
});

router.post("/", (req, res, next) => {
    const product = {
        id: req.body.id,
        temp: req.body.temp,
        hum: req.body.hum,
    };

    
    var createdProduct = function() {
        return new Promise(function(resolve, reject){
            var theProduct = [product.id, product.temp, product.hum];
            console.log(theProduct);

            connection.query("INSERT INTO simon(Id,Tempratur,Fukt) VALUES ?", [[theProduct]], function (error, results) { //hade fields
                if (error)
                return reject(error);
                else
                return resolve(theProduct);
            });
        });
    }

createdProduct().then(theProduct => {
    res.status(201).json({
        message: "Successfully added",
        Product: theProduct
    });
}).catch(error => {
    res.status(500).json({
        error: error
    });
});
});

router.get("/:productName", (req, res, next) => {
    const name = req.params.productName;

    var getProducts = function(){
        return new Promise(function(resolve, reject){

            connection.query("SELECT * FROM simon WHERE Id = ?", [name], function (error, results) {
                if(error)                
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
        res.status(404).json({message:"Error 404"});

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
        hum: req.body.hum,
    };

    var UpdateProducts = function(){
        return new Promise(function(resolve, reject){    
        connection.query("UPDATE `simon` SET `Tempratur`= ? AND `Fukt` = ? WHERE `Id` =  ?", [product.temp, product.hum, product.id], function (error, results) {  
        if(error)                
        return reject(error);
        else              
        return resolve(results);
      });
    });
  }

UpdateProducts().then(results => {
    if (results.affectedRows>0){
        res.status(200).json (results);
    }
    else
        res.status(404).json({message: "Error 404"}); 
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
            console.log(name)
            connection.query("DELETE FROM simon WHERE Id = ?", [name], function (error, results) {
                if(error)                
                return reject(error);
                else              
                return resolve(results);
            });
        });
    }
  
    deleteProducts().then(results => {
        if (results.length!=0){
            res.status(200).json(results);
        }
        else
        res.status(404).json({message: "Error 404"}); 
        }).catch(error => {
            res.status(500).json({
                error: error
        });
    });
});

module.exports = router;