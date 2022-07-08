function romanToInteger(s){
    var lastNum = 0;
    var sum = 0;
    var current_num;
    for(var i=s.length-1; i >= 0  ; i-- ){
        if(s[i] == "I"){
            current_num = 1;
        }else if(s[i] == "V"){
            current_num = 5;
        }else if(s[i] == "X"){
            current_num = 10;
        }else if(s[i] == "L"){
            current_num = 50;
        }else if(s[i] == "C"){
            current_num = 100;
        }else if(s[i] == "D"){
            current_num = 500;
        }else if(s[i] == "M"){
            current_num = 1000;
        }else{
            console.log("Not a valid roman number");
        }

        if(lastNum > current_num){
            sum = sum - current_num;
            lastNum = current_num;
        }else{
            sum = sum + current_num;
            lastNum = current_num;
        }

    }
    console.log(sum);
}

romanToInteger("IV");