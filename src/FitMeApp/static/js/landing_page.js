$(document).ready(function () {
  $('#wf-form-Download-Form').on('submit', handleInitialDetailsSubmit);
  $( "#formSubmitMsg" ).hide();
  var isdCodes = ['+91', '+1', '+65', '+44', '+971', '+968', '+973', '+965', '+966'];
  isdCodes.forEach(function (item) {
    $("#isdCode").append('<option value="' + item + '">' + item + '</option>');
  });
  // Required if there is 'Others' in 'isdCode'
  // $("#isdCode").change(function () {
  //   var value = this.value;
  //   if (value === 'Others') {
  //     $("#phonenumber")
  //       .prop('pattern', new RegExp(/^\+[1-9]{1,3}[0-9]{10,15}$/))
  //       .prop('placeholder', 'Enter phone number with ISD prefix')
  //       .prop('title', 'Phone number should be at least 10 digit long, ISD prefix should be in the correct format(eg. +1)');
  //   } else {
  //     $("#phonenumber")
  //       .prop('pattern', new RegExp(/[0-9]{10,15}/))
  //       .prop('placeholder', 'Enter your phone number')
  //       .prop('title', 'Phone number should be at least 10 digit long');
  //   }
  // });
});

function handleInitialDetailsSubmit(ev) {
  // prevent form submission
  $('#lead-gerneration-submit').prop('disabled', true);
  ev.preventDefault();
  var self = this;
  var user = {
    name: this.name.value,
    email: this.email.value,
    phoneNumber: this.phonenumber.value,
    isdCode: this.isdCode.value,
    source: window.$$leadSource,
  }
  try {
    var lead = {
      email_id: user.email,
      phone_number: user.phoneNumber,
      source: user.source,
      lead_data: {
        name: user.name,
        isd_code: user.isdCode,
      }
    };
    httpPost(lead, function (err) {
      window.sessionStorage.setItem('leadUser', JSON.stringify(user));
      if (window.$$leadSource === 'home-page') {
        fbq('track', 'Lead');
        $("#formSubmitMsg").fadeIn(300).delay(5000).fadeOut(400);
        $( '#wf-form-Download-Form' ).each(function(){
          this.reset();
      });
      $('#lead-gerneration-submit').prop('disabled', false);
      } else {
        window.location.href = "/weightloss/success";
      }
    });
  }
  catch (e) {
    throw e;
  }
}

function httpPost(data, callback) {
  var http = new XMLHttpRequest();
  http.open("POST", "/api/v1/loose-lead/create");
  http.setRequestHeader("Content-type", "application/json");
  http.send(JSON.stringify(data)); // Make sure to stringify
  http.onreadystatechange = function () {
    if (this.readyState === 4 && this.status > 200 && this.status < 400) {
      callback(null);
    }
    if (this.readyState == 4 && this.status >= 400) {
      callback({ status: this.status, error: this.statusText });
    }
  };
  http.onerror = function (err) {
    callback(err);
  };
}