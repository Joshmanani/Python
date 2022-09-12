//restart button
var restart = document.querySelector("#b")

// grab all squares

var squares = document.querySelectorAll('td')

// check all squares
function clearBoard(){
    for (var i = 0; i< squares.length; i++){
        squares[i].textContent = '';
    }
}
restart.addEventListener('click',clearBoard);

//check square marker
function changeMarker(){
    if(this.textContent === ''){
        this.textContent= 'X'
    }else if(this.textContent=== 'X'){
        this.textContent = 'O'
    }else{
        this.textContent = '';
    }
}

for (var i = 0; i< squares.length; i++){
    squares[i].addEventListener('click', changeMarker)
}
// add event listeners to squares