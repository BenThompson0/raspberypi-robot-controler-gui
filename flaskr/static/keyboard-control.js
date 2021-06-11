$(window).keypress(function (e) {
    //use e.which
    var keyCode = e.which;
    //console.log(e, keyCode, e.which)
    if (keyCode == 119) {
        console.log("W");
        e.preventDefault()
        $.getJSON('/api/forword',
            function(data) {
                return(x = 5)
        });
        return false;
    }
    else if (keyCode == 115) {
        console.log("S")
        e.preventDefault()
        $.getJSON('/api/backwords',
            function(data) {
                return(X)
        });
        return false;
    }
    else if (keyCode == 97) {
        console.log("A")
        e.preventDefault()
        $.getJSON('/api/left',
            function(data) {
                return(X)
        });
        return false;
    }
    else if (keyCode == 100) {
        console.log("D")
        e.preventDefault()
        $.getJSON('/api/forword',
            function(data) {
                return(X)
        });
        return false;
    }
});

