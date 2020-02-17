import React from 'react';
import { 
	StyleSheet,
	View,
	Text,
} from 'react-native';

export default class Homescreen extends React.Component {
    constructor(props) //define a Constructor
    {
        super(props);
			this.state = { //jag hade setState
			Name: "Simon",
			//Price: 254,
            products: []
        }
	}
		
	componentDidMount(){
		let self= this;
console.log("hej");
		fetch("http://10.22.2.67:3000/products", {
			method: "GET"
		}).then((response) => response.json()).then((responseJson)=>{ //hade responseJSON
			console.log(responseJson); //behövs inte men hade JSON
			var resultat = responseJson.result;
			if (responseJson.message = "GETTER"){ //Det var Handling Get request to / products 				hade if (message = "GETTER")
				if (response.Json.result.lenght!=0){ //Hade if (resultat.lenght!=0) //hade resultat
					self.setState({
						Name: responseJson.result[0].name, //JSON
						products: resultat
					})
				}
				else
				alert("Please add a Name in the bottom of the screen and try again"); //hade inget avslutande
				console.log(this.state); //hade this.setState
			}
		}).catch((error)=>{
			console.error(error); //hade ej catch
		});
	}

    WriteOutFromBackend(){
        return this.state.products.map((product) => { //hade setState 		hade product med c
            return ( //hade inge <View>
				<View> 
					<Text style={styles.componentrecentcontenttext}> 
						Name: {product.name} Price: {product.price}
					</Text>
				</View>
            )
        })
	}
	//comp1.js 62 - 82 wtf

/* onödigt right?
  	constructor(props) {
		super(props)
		this.state = {
			Name: '',
		 	Price: '12',
		}
	}
*/

    InsertDataToServer=() => {
        const {Name} = this.state;
        const {Price} = this.state;
		console.log("responseJSON");
            if (Name!=""){
                fetch("http://10.22.2.67:3000/products",{
                    method: "POST",
                    headers: {
                        "Accept": "application/jqson", //jqson har joakim jag hade json
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        name: Name,
                        price: Price
                    })
				}).then((response) => response.json()).then(responseJson => { //hade responseJSON
					console.log(responseJson.Product[0].name); // hade ej denna rad
                    console.log(responseJson); //hade responseJSON
                    alert(responseJson.message +", "+ responseJson.Product[0]); //hade responseJSON 			hade ej , 			ensamt Name
                }).catch((error)=>{
                    console.log(error);
                });
            }
            else
        alert("Name is empty");
    }


    UpdateDataToServer=() => {
        const {Name} = this.state;
        const {Price} = this.state;

            if (Name!=""){
				var adress="http://10.22.2.67:3000/products/"+Name; //hade inte denna "nödvändoga" saken
                fetch(adress, {
                    method: "PATCH",
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        name: Name,
                        price: Price
                    })
                }).then((response) => response.json()).then(responseJson => { //hade responseJSON
                    console.log(responseJson); //hade responseJson
                    alert("Update was successfull, "+Name);
                }).catch((error)=>{
                    console.error(error); //hade lkog
                });
        }
        else
        alert("Name is empty");
    }

    DeleteDataFromServer=() => { //hade inte nametest är det constructorn som ska vara använd här
        const {Name} = this.state;
        const {Price} = this.state;

            if (Name!=""){
				var adress="http://10.22.2.67:3000/products/"+Name; //hade inte denna rad
                fetch(adress,{
                    method: "Delete", //hade DELETE
                    headers: {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
					}, //hade ingen ,
					body: JSON.stringify({
						name: Name,
						price: Price,	 
						})
					   
					  }).then((response) => response.json())
						  .then((responseJson) => {
			   
					  console.log(responseJson);
						alert( "Delete was successfull, "+ Name);
					   
						  }).catch((error) => {
						  console.error(error);
						  });
					   
						 }
						 else
						 alert("Write a name and a price.")
						}
					/* detta var min
                }).then((response) => response.json()).then(responseJSON => {
                    console.log(responseJSON);
                    alert("Delete "+Name);
                }).catch((error)=>{
                    console.lkog(error);
                });
        }
        else
        alert("Name is empty");
    }
*/
	/*    
    constructor(props)
    {
        super(props);
			this.state = {
            termometer: []
        }
	}

	componentDidMount(){
		let self= this;
		fetch("http://10.22.2.67:3000/products", {
			method: "GET"
		}).then((response) => response.json()).then((responseJson)=>{
			console.log(responseJson);
			var resultat = responseJson.result;
			if (responseJson.message = "GETTER"){
				if (response.Json.result.lenght!=0){
					self.setState({
						Temp: responseJson.result[0].temp,
						termometer: resultat
					})
				}
				else
				alert("något gick fel too bad");
				console.log(this.state);
			}
		}).catch((error)=>{
			console.error(error);
		});
	}

    WriteOutFromBackend(){
        return this.state.termometer.map((termometer) => {
            return (
				<View> 
					<Text> 
						Tempratur: {termometer.temp} Fukt: {termometer.fukt}
					</Text>
				</View>
            )
        })
	}
*/
    render() {
        return (
			<View>
				<Text>
					hellow
				</Text>
			</View>
		);
    }
}

const styles = StyleSheet.create({

});