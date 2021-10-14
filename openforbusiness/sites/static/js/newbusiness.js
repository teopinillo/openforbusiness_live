document.addEventListener('DOMContentLoaded', function() {
    
    //e stand for Element
    //b stand for business
    
    eCard = document.getElementById('bCard');
    businessName = document.getElementById('businessName');
    eCardStyle = document.getElementById('card_style');
    eCardStyle.style.backgroundColor = document.getElementById('option-201').style.backgroundColor;
    divAddress = document.getElementById('div_address_id');
    description1 = document.getElementById('description1');
    description2 = document.getElementById('description2');
    address_label = document.getElementById('address_label_id');
    address_label.style.color = '#e60000';
            
    eCardStyle.onchange = function () {
        //v = eCardStyle.options[eCardStyle.selectedIndex].value;
        //s = eCardStyle.options[eCardStyle.selectedIndex].text;
        //console.log ("select change: " + s + v)
        //eCard.style.backgroundColor = "#345623";
        //console.log (this.options[this.selectedIndex].text);
        middle_back = this.options[this.selectedIndex].dataset.background;
        top_back = this.options[this.selectedIndex].dataset.topbackground;
        top_text = this.options[this.selectedIndex].dataset.text;
        bottom_back = this.options[this.selectedIndex].dataset.bottombackground;
        iconsColor  = this.options[this.selectedIndex].dataset.iconscolor;
        //console.log("");
        //console.log ("cardBackground :" + cardBackground);
        //console.log ("topBackground :" + topBackground);

        eCardStyle.style.backgroundColor = middle_back;
        businessName.style.backgroundColor = top_back;        
        businessName.style.color = bottom_back;
        eCard.style.backgroundColor = middle_back;
        description1.style.backgroundColor = middle_back;
        description2.style.backgroundColor = middle_back;
        divAddress.style.backgroundColor = bottom_back;
        address_label.style.color = top_back;


   }
}
)

