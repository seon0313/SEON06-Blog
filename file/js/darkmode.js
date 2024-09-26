function darkChange(){
    if (document.body.classList.contains('dark')){
        document.body.classList.remove('dark');
    } else {
        document.body.classList.add('dark');
    }
}

function setOSDark(){
    const dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (dark) {
        document.body.classList.add('dark');
    }
    return 0;
}

window.onload = function() {
    setOSDark();
}