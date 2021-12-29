////// Overview of comments web tags  

// SHOW MORE COMMENTS
// div tag will have style="display: none;" if there are no more comments
// otherwise it is displayed <div class="vf-load-more-con" style="display: none;">
<a href="#" class="vf-load-more vf-text-small vf-strong">Show More</a>
</div> 

// SHOW REPLIES
// div tag will have style="display: none;" if there are no more comments
// otherwise it is displayed <div class="vf-comment-replies hidden">
<a class="vf-replies-button vf-strong vf-text-small" href="#">Show <span class="vf-replies">0</span> older replies</a>

// SHOW MORE COMMENT TEXT
// tag is displayed only when comment has hidden text
// otherwise the tag is not present <a href="#" class="vf-show-more" data-action="more">» more</a>

//STEPS 1, 2, 3 to get complete web page that can be downloaded

//STEP 1 - pages with 1000's of comments gets slower 
// and show button exceeds 5000 ms so requires manual rerun of script

function getMore() {
    moreDiv = document.getElementsByClassName('vf-load-more-con')[0];
    if(moreDiv.style.display === "none") {
        console.log('vf-load-more comments finished');
        clearInterval(timer);
        return;
    }
    console.log('More comments');
    moreDiv.childNodes[0].nextElementSibling.click();
}
var timer = setInterval(getMore, 5000);

//Version 2
function getMore() {
    moreDiv = document.getElementsByClassName('vf-load-more-con')[0];
    if(moreDiv.style.display === "none") {
        console.log('button hidden');
        //return;
    } else {
        console.log('button clicked');
        moreDiv.childNodes[0].nextElementSibling.click();
    }
}
var timer = setInterval(getMore, 5000);

//Version 3
var buttons = document.getElementsByClassName('vf-load-more');
for(var i = 0; i <= buttons.length; i++) { buttons[i].click(); }

//Version 4
moreDiv = document.getElementsByClassName('vf-load-more-con')[0];
if (moreDiv.style.display !== "none") {
    moreDiv.childNodes[0].nextElementSibling.click();
    console.log(moreDiv.style.display);
}

//STEP 2 - vf-replies-button - loops to auto show all comments' replies
var buttons = document.getElementsByClassName('vf-replies-button');
console.log(buttons.length, 'vf-replies-button');
for(var i = 0; i <= buttons.length; i++) { buttons[i].click(); console.log('click', i, 'of',buttons.length) }
console.log('vf-rreplies-button finished');

// also the new replies links might need to do this too?
var new_replies = document.getElementsByClassName('vf-rt-reply-text');
console.log(new_replies.length, 'vf-rt-reply-text');
for(var i = 0; i <= new_replies.length; i++) { new_replies[i].click(); console.log('click', i, 'of',new_replies.length) }
console.log('vf-rt-reply-text finished');

//STEP 3 - vf-show-more - loops to show all commments' text
var buttons = document.getElementsByClassName('vf-show-more');
console.log(buttons.length, 'vf-show-more buttons')
for(var i = 0; i <= buttons.length; i++) { buttons[i].click(); console.log('click', i, 'of',buttons.length) }
console.log('vf-show-more comment text finished');


////// Archive

$('.vf-load-more').ready(function() {
    console.log('More comments');
    var buttons = document.getElementsByClassName('vf-load-more');
    for(var i = 0; i <= buttons.length; i++) { buttons[i].click(); }
});

var existCondition = setInterval(function() {
    if ($('.vf-load-more').length) {
        console.log('More comments');
        var buttons = document.getElementsByClassName('vf-load-more');
        for(var i = 0; i <= buttons.length; i++) { buttons[i].click(); }
        clearInterval(existCondition);
    }
}, 1000); // check every 1000ms
console.log('vf-load-more comments finished');