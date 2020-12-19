function myFunction(){
    var x = document.getElementById("top-menu");
        if(x.className === "top-menu"){
            x.className += " responsive";
        }else{
            x.className = "top-menu";
        }
}