document.addEventListener('DOMContentLoaded', function() {
    
    //e stand for Element
    //b stand for business
    
    eCard = document.getElementById('bCard');
    businessName = document.getElementById('label_new_name');
    business_name_cont = document.getElementById('label_new_name_div');
    input_img_cntr = document.getElementById('input_img_cntr');

    pre_fst_ph = document.getElementById('phone_1_pre');    
    pre_snd_ph = document.getElementById('phone_2_pre');

    eCardStyle = document.getElementById('card_style');
    
    divAddress = document.getElementById('div_address_id');
    services1 = document.getElementById('services_1');
    services2 = document.getElementById('services_2');
    services3 = document.getElementById('services_3');
    services4 = document.getElementById('services_4');

    des_ctnr = document.getElementById('des_ctnr');
    phone_ctr = document.getElementById('phone_ctnr');  
    pre_reviews = document.getElementById('pre_reviews');     
    showCardStyle (eCardStyle);   
 }
 )

 let showCardStyle = function ( element ) {
    
    bg_top = element.options[element.selectedIndex].dataset.bg_top;    
    txt_top = element.options[element.selectedIndex].dataset.txt_top;
    //center
    bg_center = element.options[element.selectedIndex].dataset.bg_center;    
    txt_center = element.options[element.selectedIndex].dataset.txt_center;
    //bottom
    bg_bottom = element.options[element.selectedIndex].dataset.bg_bottom;
    txt_bottom = element.options[element.selectedIndex].dataset.txt_bottom;

    iconsColor  = element.options[element.selectedIndex].dataset.iconscolor;
    
    //card style selector
    eCardStyle.style.backgroundColor = bg_top;
    eCardStyle.style.color = txt_top;
    
    //top business name
    businessName.style.backgroundColor = bg_top;        
    businessName.style.color = txt_top;
    business_name_cont.style.backgroundColor = bg_top;

    //center
    des_ctnr.style.backgroundColor = bg_center;
    input_img_cntr.style.backgroundColor = bg_center;
    pre_reviews.style.color = txt_center;
    pre_fst_ph.style.color = txt_bottom;
    pre_snd_ph.style.color = txt_bottom;

    changeColor (services1, txt_center, bg_center);
    changeColor (services2, txt_center, bg_center);
    changeColor (services3, txt_center, bg_center);
    changeColor (services4, txt_center, bg_center);

    //phones container
    changeColor (phone_ctrn, txt_bottom, bg_bottom);    
}

function changeLabelName ( element, container){    
    document.getElementById(container).innerText = element.value;   
}

function changeColor (element, txt_color, bg_color){
    element.style.backgroundColor = bg_color;
    element.style.color = txt_color;
}