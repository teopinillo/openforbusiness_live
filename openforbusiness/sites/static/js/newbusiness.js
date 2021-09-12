document.addEventListener('DOMContentLoaded', function() {
    
    //e stand for Element
    //b stand for business
    eSelect = document.querySelector('#color-change');
    eCard = document.getElementById('bCard');
    eBusinessName = document.getElementById('businessName');
    eSelect.style.backgroundColor = document.getElementById('option-201').style.backgroundColor;
    
    eSelect.onchange = function () {
        //console.log (this.options[this.selectedIndex].text);
        cardBackground = this.options[this.selectedIndex].dataset.background;
        topBackground = this.options[this.selectedIndex].dataset.topbackground;
        textColor = this.options[this.selectedIndex].dataset.text;
        bottomBackGround = this.options[this.selectedIndex].dataset.bottombackground;
        iconsColor  = this.options[this.selectedIndex].dataset.iconscolor;
        console.log("");
        console.log ("cardBackground :" + cardBackground);
        console.log ("topBackground :" + topBackground);

        eSelect.style.backgroundColor = cardBackground;
        eBusinessName.style.backgroundColor = topBackground;
        eCard.style.backgroundColor = cardBackground;
   }
}
)
