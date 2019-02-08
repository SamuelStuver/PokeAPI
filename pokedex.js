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
	}

}


p = new Pokemon({"name":"pikachu", "type":"electric"});
p.show();
