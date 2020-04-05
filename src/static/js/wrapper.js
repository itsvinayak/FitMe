function _ga(category, action, label) {
    ga('send', 'event', category, action, window.location.pathname + ' ' + label);
};

function _ga_coaches(action, label) {
    ga('send', 'event', window.location.pathname, action, label + ' ' + window.location.pathname);
}