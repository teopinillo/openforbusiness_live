document.addEventListener('DOMContentLoaded', function() {
    showStarsOnSelect();

});

function showStarsOnSelect(){    
    document.getElementsByName('score')[0].options[0].innerHTML = '★'
    document.getElementsByName('score')[0].options[1].innerHTML = '★★'
    document.getElementsByName('score')[0].options[2].innerHTML = '★★★'
    document.getElementsByName('score')[0].options[3].innerHTML = '★★★★'
    document.getElementsByName('score')[0].options[4].innerHTML = '★★★★★'
}