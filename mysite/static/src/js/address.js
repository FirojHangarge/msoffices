$("#id_district").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-taluka-url");
  var districtId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'district': districtId
    },
    success: function (data) {
      $("#id_taluka").html(data);
    }
  });

});
$("#id_taluka").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-taluka-url");
  var talukaId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'taluka': talukaId
    },
    success: function (data) {
      $("#id_village").html(data);
    }
  });

});
