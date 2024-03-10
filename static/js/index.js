// Create Function in JavaScript
// function calculator(number1,number2, opration){
//  var a = 10;
// }

const calculator = (number1,number2,airthmeticOperation)=>{
    let result;
    switch(airthmeticOperation){
        case 'add':
            result = number1+number2;
            break;
        case 'substract':
            result = number1-number2;
            break;
        case 'multiply':
            result = number1 * number2;
            break;
        case 'divide':
            result = number1/number2;
            break;
        default:
            console.log('Invalid operation');
    }
    return result;
}



