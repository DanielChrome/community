function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("content-tab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" is-active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " is-active";
}

function clickMenu(evt, menuName) {
    var i, x, menulinks;
    x = document.getElementsByClassName("content-menu-about");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    menulinks = document.getElementsByClassName("menu-about");
    for (i = 0; i < x.length; i++) {
        menulinks[i].className = menulinks[i].className.replace(" is-active", "");
    }
    document.getElementById(menuName).style.display = "block";
    //evt.currentTarget.getElementsByClassName("menu-about"). className += " is-active";
    menulinks = evt.currentTarget.getElementsByClassName("menu-about");
    for (i = 0; i < x.length; i++) {
        menulinks[i].className = menulinks[i].className += " is-active";
    }
}

function accept(event, u, a) {
    window.location.replace('/social/'+u+'/acceptconnection?accept='+a);
}
