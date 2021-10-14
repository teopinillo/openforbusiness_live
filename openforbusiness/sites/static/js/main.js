function favorite_org(element) {

    post_id = element.dataset.post_id;
    liked = element.dataset.like;
    total_likes_element = document.querySelector('#total_likes' + post_id);
    //console.log(`total_likes_element: ${total_likes_element}`)
    if (liked === "True") {
      element.dataset.like = "False";
      element.innerHTML = "thumb_down";
      set_like = 1; //True
    } else {
      element.dataset.like = "True";
      element.innerHTML = "thumb_up";
      set_like = 0;  //False
    }
    updateLikes(post_id, set_like).then(result => {
      //update the total of likes 
      total_likes_element.innerHTML = result.total_likes;
  
    }).catch(error => {
      console.error(error);
      alert(error);
    });
  
    return false;
  }

  function setFavorite (element, id ) {

    b_id = id;
    console.log ('element:'+ element);
    console.log('id:' + id);
    favorite = element.dataset.favorite;
    
    if (favorite === "True") {
        element.dataset.favorite = "False";
        element.className = "fa fa-heart-o"; 
    } else {
        element.dataset.favorite = "True";      
        element.className = "fa fa-heart heart"; 
    }
    /*updateLikes(post_id, set_like).then(result => {
      //update the total of likes 
      total_likes_element.innerHTML = result.total_likes;
  
    }).catch(error => {
      console.error(error);
      alert(error);
    });
    */
    return false;
  }

  function setRating (element, id, rating){    
    parent = element.parentNode;    
    //console.log ('parent:'+ parent );
    //console.log ('element:'+ element);
    var childrens = parent.childNodes;
    //console.log('childrens: '+ childrens);
    console.log('rating: '+rating);  
    c=1;
    for (i = 3; i <= childrens.length - 1; i=i+2) {
      children = childrens[i];
      console.log ('children: ' + children);
      if (c<=rating) {
        children.className = "fa fa-star checked"
      } else {
        children.className = "fa fa-star"
      }
      c++; 
      console.log('c:'+c);     
    }     
    return false;
  }