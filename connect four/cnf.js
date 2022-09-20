var player1 = prompt('player One : Enter your name and you will be player One');
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt('player Two : Enter your name and you will be player Two');
var player2Color = 'rgb(86, 151, 255)';

var game_on = true;
var table = $('table tr');

// function to report a win
function reportWin(rowNum, colNum){
    console.log("you won starting at this row, col");
    console.log(rowNum);
    console.log(colNum);
}


//function to change a color of a given table cell to a specific color

function changeColor(rowIndex, colIndex, color){
    // how to get a table cell by index using jquery
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

// function to return color of a given cell 
function returnColor(rowIndex, colIndex){
    // how to get a table cell by index using jquery
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

//function to return the bottom row that is still grey
function checkBottom(colIndex){
    var colorReport = returnColor(5,colIndex);
    for (var row = 5; row>= -1; row--){
        colorReport = returnColor(row, colIndex);
        if (colorReport === 'rgb(128, 128, 128)'){
           return row;
        }
    }
}



// to check matching colors
function colorMatchcheck(one,two,three,four){
    return (one === two && one === three && one === four && one !=='rgb(128, 128, 128)' && one !== undefined );
}


// check for horizontal wins
function horizontalWinCheck(){
    for (var row=0; row< 6; row++){
        for (var col = 0; col<4; col++){
            if (colorMatchcheck(returnColor(row,col), returnColor(row,col+1), returnColor(row,col+2), returnColor(row,col+3))){
                console.log('horiz');
                return true;
            } else{
                continue;
            }
            
        }
    }
}

function verticalWinCheck(){
    for (var col=0; col< 7; col++){
        for (var row = 0; col<3; row++){
            if (colorMatchcheck(returnColor(row,col), returnColor(row+1,col), returnColor(row+2,col), returnColor(row+3,col))){
                console.log('vertical');
                return true;
            } else{
                continue;
            }            
        }
    }
}

var currentPlayer = 1;
var currentName = player1;
var currentColor= player1Color;

$('h3').text(player1+" it is your turn to pick a colum to drop a piece")
$('.board button').on('click', function(){
    var col = $(this).closest('td').index();

    var bottomAvail = checkBottom(col);

    changeColor(bottomAvail, col, currentColor);
    if (horizontalWinCheck() || verticalWinCheck()){
        $('h1').text(currentName + 'yOu have won');
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');
    }

    currentPlayer = currentPlayer * -1;

    if (currentPlayer === 1){
        currentName = player1;

        $('h3').text(currentName + ' it is your turn ');
        currentColor = player1Color;
    } else {
        currentName = player2;
        $('h3').text(currentName + ' it is your turn ');
        currentColor = player2Color;
    }

})
