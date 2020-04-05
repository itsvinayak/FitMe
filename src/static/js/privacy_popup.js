const popupNode = $('#popup-wrapper');
popupNode.hide();
const acceptButtonNode = $('#accept-btn');
const termsAccepted = localStorage.getItem('privacy_terms_accepted');

let popupTimer;

if (!termsAccepted) {
  popupTimer = setTimeout(() => {
    popupNode.show();
  }, 2000);
}

acceptButtonNode.on('click', () => {
  popupTimer && clearTimeout(popupTimer);
  popupNode.hide();
  localStorage.setItem('privacy_terms_accepted', true)
});

const readMoreButton = $('#read-more');
readMoreButton.on('click', () => {
  $("#popup-text").html("We use cookies and other tracking technologies to improve your browsing experience on our website, to show you personalized content and targeted ads, to analyze our website traffic, and to understand where our visitors are coming from. By browsing our website, you consent to our use of cookies and other tracking technologies. You can check out terms of services <a href='/privacy' id='link' target='_blank'>here</a>.");
});