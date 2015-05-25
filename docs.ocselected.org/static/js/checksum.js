var checksums = {
  'Fedora-Live-Workstation-x86_64-21-5.iso':'../../static/checksums/Fedora-Workstation-21-x86_64-CHECKSUM',
  'Fedora-Live-Workstation-i686-21-5.iso':'../../static/checksums/Fedora-Workstation-21-i386-CHECKSUM',
  'Fedora-Server-DVD-x86_64-21.iso':'../../static/checksums/Fedora-Server-21-x86_64-CHECKSUM',
  'Fedora-Server-netinst-x86_64-21.iso':'../../static/checksums/Fedora-Server-21-x86_64-CHECKSUM',
  'Fedora-Server-DVD-i386-21.iso':'../../static/checksums/Fedora-Server-21-i386-CHECKSUM',
  'Fedora-Server-netinst-i386-21.iso':'../../static/checksums/Fedora-Server-21-i386-CHECKSUM',
  'Fedora-Cloud-Base-20141203-21.x86_64.qcow2':'../../static/checksums/Fedora-Cloud-Images-x86_64-21-CHECKSUM',
  'Fedora-Cloud-Base-20141203-21.x86_64.raw.xz':'../../static/checksums/Fedora-Cloud-Images-x86_64-21-CHECKSUM',
  'Fedora-Cloud-Atomic-20141203-21.x86_64.qcow2':'../../static/checksums/Fedora-Cloud-Images-x86_64-21-CHECKSUM',
  'Fedora-Cloud-Atomic-20141203-21.x86_64.raw.xz':'../../static/checksums/Fedora-Cloud-Images-x86_64-21-CHECKSUM',
  'Fedora-Cloud-Base-20141203-21.i386.qcow2':'../../static/checksums/Fedora-Cloud-Images-i386-21-CHECKSUM',
  'Fedora-Cloud-Base-20141203-21.i386.raw.xz':'../../static/checksums/Fedora-Cloud-Images-i386-21-CHECKSUM'
}
var fallback = '../../verify.html';

window.onload = function(){
  var path = window.location.toString().split('/');
  var checksum = checksums[path[path.length-1]];
  var links = document.getElementsByClassName('checksum');
  for (var i = 0; i<links.length; i++) {
      links[i].href = (checksum === undefined) ? fallback : checksum;
  }
}