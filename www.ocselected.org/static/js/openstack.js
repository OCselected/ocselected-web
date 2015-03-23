// Script for Cloud Openstack download buttons

$("#openstack-base-click").click(function(event) {
  this.toggle = !this.toggle;event.preventDefault();
  $("#openstack-base-link").toggle('slow');
  $("#raw-base-link").stop().fadeTo(600, this.toggle ? 0.3 : 1);
});

$("#openstack-cont-click").click(function(event) {
  this.toggle = !this.toggle;event.preventDefault();
  $("#openstack-cont-link").toggle('slow');
  $("#raw-cont-link").stop().fadeTo(600, this.toggle ? 0.3 : 1);
});