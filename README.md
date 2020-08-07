Wordpress plugins as RPM
=========================

This repository is to collect various Wordpress plugins in zip ball,
and build RPM for easier package management.

The default installation path is
/usr/share/wordpress/wp-content/plugins/


How to build
-----------
Copy this repository to your ~/rpmbuild folder, and run: 
cd ~/rpmbuild && rpmbuild -bb SPECS/plugin.spec
