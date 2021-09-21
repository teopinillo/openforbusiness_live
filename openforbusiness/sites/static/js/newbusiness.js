document.addEventListener('DOMContentLoaded', function() {
    
    //e stand for Element
    //b stand for business
    
    eCard = document.getElementById('bCard');
    divBusinessName = document.getElementById('businessName');
    eCardStyle = document.getElementById('card_style');
    eCardStyle.style.backgroundColor = document.getElementById('option-201').style.backgroundColor;
        
    eCardStyle.onchange = function () {
        v = eCardStyle.options[eCardStyle.selectedIndex].value;
        s = eCardStyle.options[eCardStyle.selectedIndex].text;
        console.log ("select change: " + s + v)
        eCard.style.backgroundColor = "#345623";
        //console.log (this.options[this.selectedIndex].text);
        cardBackground = this.options[this.selectedIndex].dataset.background;
        topBackground = this.options[this.selectedIndex].dataset.topbackground;
        textColor = this.options[this.selectedIndex].dataset.text;
        bottomBackGround = this.options[this.selectedIndex].dataset.bottombackground;
        //iconsColor  = this.options[this.selectedIndex].dataset.iconscolor;
        //console.log("");
        //console.log ("cardBackground :" + cardBackground);
        //console.log ("topBackground :" + topBackground);

        //eSelect.style.backgroundColor = cardBackground;
        divBusinessName.style.backgroundColor = cardBackground;
        eCard.style.backgroundColor = cardBackground;
   }
}
)

