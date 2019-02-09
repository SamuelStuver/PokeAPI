#! /usr/bin/env node

var baseUrl = "https://pokeapi.co/api/v2/"

function capitalize(word){

    if (typeof word != 'string'){
		return word;	
    } else {
		var newWord = word;
		for (var i=0; i < word.length; i++){
	    	var c = word[i];
	    	if (c.toLowerCase() != c.toUpperCase()){
				if (i == 0){
		    		newWord = c.toUpperCase() + word.substr(1,word.length-1);
				} else if (i < (word.length - 1)){
					newWord = word.substr(0, i) + c.toUpperCase() + word.substr(i+1, word.length-1);
				} else {
		    		newWord = word.substr(0, i-1) + c.toUpperCase();
				} 
				return newWord
	    	}
		}
		return newWord
    }

}

class Pokemon {

	constructor(dict){
		Object.assign(this,dict);
	}
	
	show() {
		console.log(this);
		console.log('-'.repeat(25));
		console.log(this.id + ' - ' + capitalize(this.name));
		console.log(this.types);
		console.log("Base Exp: " + this.base_experience);
		console.log("Height: " + this.height/10.0 + " m");
		console.log("Weight: " + this.weight/10.0 + " kg");
		console.log('-'.repeat(25));
	}

}


p = new Pokemon({"id":25,"name":"pikachu", "types":"electric", "base_experience":112, "height":4, "weight":60});
p.show();
