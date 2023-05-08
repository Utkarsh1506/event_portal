function view(){
    if(document.getElementById("add_form").style.display=="none"){
        document.getElementById("add_form").style.display="block";
        document.getElementById("add_form").style.transition="0.2s";
    
    }
    else{
        document.getElementById("add_form").style.display="none";
    }
}


let btn = document.querySelector(".menu_btn");
let sidebar = document.querySelector(".sidebar");


btn.onclick= function(){
    sidebar.classList.toggle("active");
}



